from flask import Flask, jsonify, request
import requests
import datetime
from validate_patient_data import validate_patient_data
from validate_heart_rate import validate_heart_rate
from validate_time_interval import validate_time_interval
from calculate_avg import calculate_avg
from calculate_interval_avg import calculate_interval_avg
from check_tachycardia import check_tachycardia

app = Flask(__name__)
all_patients = []


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    patient_raw = requests.get_json()
    patient = validate_patient_data(patient_raw)
    all_patients.append(patient)
    result = {
        "message": "Added patient {0} to list"
    }
    r = result.format(request.json["patient_id"])
    return jsonify(r), 200


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    hr = requests.get_json()
    timestamp = datetime.datetime.now()
    patient_hr = validate_heart_rate(hr, timestamp)


    for patient in all_patients:
        for key in patient:
            if patient_hr["patient_id"]==key:
                patient["heart_rate"]

    return 200


@app.route("/api/status/<patient_id>", methods=["GET"])
def get_status():
    print("tachycardic")
    # run check if tachycardic and return time stamp
    return "results"


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def get_heart_rate():
    print("heart_rate")
    # get all heart rate with time stamp (probably as json)
    return "results"


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def get_heart_avg():
    print("heart rate avg")
    # get all heart rate avg for everything
    return "results"


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_average():
    print("heart rate avg")
    # get all heart rate avg for everything
    return 200
