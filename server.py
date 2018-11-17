from flask import Flask, jsonify, request
import sendgrid
import os
import datetime
import logging
from validate_patient_data import validate_patient_data
from validate_heart_rate import validate_heart_rate
from validate_time_interval import validate_time_interval
from calculate_avg import calculate_avg
from calculate_interval_avg import calculate_interval_avg
from check_tachycardia import check_tachycardia

app = Flask(__name__)

all_patients = []


@app.route("/", methods=["GET"])
def hello():
    """
    Welcome message.
    """
    return "Welcome to hr sentinel server"


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    """
    When user posts a new patient, append validated data onto
    a list of all patients
    """
    try:
        patient_raw = request.get_json()
        patient1 = validate_patient_data(patient_raw)
        if not all_patients:
            all_patients.append(patient1.copy())
            return "Successful"
        for patient in all_patients:
            if patient["patient_id"] == patient1[
                    "patient_id"]:
                        logging.error(
                            "This patient already exists")
                        raise ValueError
        all_patients.append(patient1.copy())
        return "Successful"
    except:
        return "Something went wrong"


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    """
    When user posts a new heart rate, append to the
    patient's heart rate list and send email if
    tachycardic.
    """
    try:
        hr = request.get_json()
        timestamp = datetime.datetime.now()
        patient_hr = validate_heart_rate(hr, timestamp)
        for patient in all_patients:
            if patient_hr["patient_id"] == patient["patient_id"]:
                hr_copy = patient_hr["heart_rate"].copy()
                patient["heart_rate"].append(hr_copy)
                if patient_hr["heart_rate"][0] > 100:
                    bool_t = check_tachycardia(patient)
                    print(bool_t[0])
                    if bool_t[0] is True:
                        sg = sendgrid.SendGridAPIClient(
                            apikey=os.environ.get(
                                'SENDGRID_API_KEY'))
                        data = {
                            "personalizations": [
                                {
                                    "to": [
                                        {
                                            "email": patient[
                                                "attending_email"]
                                        }
                                    ],
                                    "subject": "Tachycardia Alert"
                                }
                            ],
                            "from": {
                                "email": "alert@tachycardia.com"
                            },
                            "content": [
                                {
                                    "type": "text/plain",
                                    "value": ("Patient {0}'s"
                                              "submitted heart rate"
                                              "indicated tachycardia."
                                              "Latest entry: {1}"
                                              .format(
                                                patient_hr["patient_id"],
                                                patient["heart_rate"][1]
                                                [1]))
                                }
                            ]
                        }
                        response = sg.client.mail.send.post(
                            request_body=data)
                        print(response.status_code)
                        print(response.body)
                        print(response.headers)
        result = {
            "message": "Added heart rate to patient",
            "patient_id": patient_hr["patient_id"]
        }
        return jsonify(result)
    except:
        return "No patient data found"


@app.route("/api/status/<patient_id>", methods=["GET"])
def get_status(patient_id):
    """
    Return status of tachycardia and the latest heart
    rate entry of the specified patient id.
    """
    try:
        for patient in all_patients:
            if patient["patient_id"] == patient_id:
                    bool_t = check_tachycardia(patient)
                    if bool_t[0] is True:
                        r = {
                            "message": "Patient is tachycardic",
                            "time of last bpm entry": "{0}".format(bool_t[1])
                        }
                        rjson = jsonify(r)
                        return rjson
                    if bool_t[0] is False:
                        r = {
                            "message": "Patient is not tachycardic",
                            "time of last bpm entry": "{0}".format(bool_t[1])
                        }
                        rjson = jsonify(r)
                        return rjson
                    else:
                        return "Something went wrong"
    except:
        return "No patient data found"


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def get_heart_rate(patient_id):
    """
    Calculate and return average heart rate.
    """
    try:
        for patient in all_patients:
            if patient["patient_id"] == patient_id:
                result = calculate_avg(patient["heart_rate"])
                patient["average"] = result
                return jsonify(patient["average"])
        return "No patient data found"
    except:
        return "Something went wrong."


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_avg(patient_id):
    """
    Return all heart rates entered for that user.
    """
    try:
        heart_rates = []
        for patient in all_patients:
            if patient["patient_id"] == patient_id:
                    hr_data = patient["heart_rate"]
                    for hr in hr_data:
                        heart_rates.append(hr[0])
                    return jsonify(heart_rates)
        if not heart_rates:
            return "This patient has no bpm entry"
    except:
        return "Something went wrong"


@app.route("/api/heart_rate/interval_average", methods=["POST", "GET"])
def interval_average():
    """
    Returns interval average of user specified time.
    """
    try:
        interval_raw = request.get_json()
        interval = validate_time_interval(interval_raw)
        print(interval)
        interval_time = interval["heart_rate_average_since"]
        for patient in all_patients:
            if patient["patient_id"] == interval["patient_id"]:
                hr = patient["heart_rate"]
                r = calculate_interval_avg(hr, interval_time)
                patient["average"] = r
                print(r)
                return jsonify(r)
        return "No patient data found"
    except:
        return "Something went wrong"


if __name__ == "__main__":
    app.run(host='127.0.0.1')
