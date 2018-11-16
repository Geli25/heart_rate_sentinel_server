from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
all_patients = []


@app.route("/api/new_patient", methods=["POST"])
def new_patient():
    patient_raw = requests.get_json()
    # validate data here validate(patient_raw)
    # patient_data = {
    #     "patient_id": patient_raw["patient_id"],
    #     "attending_email": patient_raw["attending_email"],
    #     "user_age": patient_raw["user_age"]
    # }
    all_patients.append()
    return 200


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    patient_heart_rate = requests.get_json()
    # patient_heart_dic = {
    #     "patient_id": patient_heart_rate.patient_id,
    #     "heart_rate": patient_heart_rate.heart_rate,
    # }

    for patient in all_patients:

        if patient.patient_id == patient_heart_rate.patient_id:
            # validate heart rate
            # data=[patient_heart_dic["heart_rate"],datetime.datetime.now()]
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
