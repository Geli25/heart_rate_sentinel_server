from flask import Flask, jsonify, request
import sendgrid
import os
import datetime
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
    Returns the string "Hello, world" to the caller
    """
    return "Welcome to hr sentinel server"


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    try:
        patient_raw = request.get_json()
        patient = validate_patient_data(patient_raw)
        all_patients.append(patient.copy())
        return "Successful"
    except:
        return"Something went wrong"


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    try:
        hr = request.get_json()
        timestamp = datetime.datetime.now()
        patient_hr = validate_heart_rate(hr, timestamp)
        for patient in all_patients:
            for key in patient:
                if patient_hr["patient_id"] == patient[key]:
                    hr_copy = patient_hr["heart_rate"].copy()
                    patient["heart_rate"].append(hr_copy)
                    if patient_hr["heart_rate"][0] > 100:
                        bool_t = check_tachycardia(patient)
                        print(bool_t[0])
                        if bool_t[0] is True:
                            sg = sendgrid.SendGridAPIClient(apikey=
                                                            os.environ.get(
                                                                'SENDGRID_'
                                                                'API_KEY'))
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
                                        "value": ("Patient {0}'s latest"
                                                  "heart rate entry"
                                                  " as of {1}"
                                                  " indicated tachycardia"
                                                  .format(
                                                    patient_hr["patient_id"],
                                                    patient["heart_rate"][1]
                                                    [1]))
                                    }
                                ]
                            }
                            response = sg.client.mail.send.post(request_body=data)
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
    for patient in all_patients:
        if patient["patient_id"] == patient_id:
            result = calculate_avg(patient["heart_rate"])
            return jsonify(result)
    return "No patient data found"


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_avg(patient_id):
    heart_rates = []
    for patient in all_patients:
        if patient["patient_id"] == patient_id:
                hr_data = patient["heart_rate"]
                for hr in hr_data:
                    heart_rates.append(hr[0])
                return jsonify(heart_rates)
    return "No patient data found"


@app.route("/api/heart_rate/interval_average", methods=["POST", "GET"])
def interval_average():
    try:
        interval_raw = request.get_json()
        interval = validate_time_interval(interval_raw)
        print(interval)
        interval_time = interval["heart_rate_average_since"]
        for patient in all_patients:
            if patient["patient_id"] == interval["patient_id"]:
                hr = patient["heart_rate"]
                r = calculate_interval_avg(hr, interval_time)
                return jsonify(r)
    except:
        return "Something went wrong"


if __name__ == "__main__":
    app.run(host='127.0.0.1')
