import requests

info15 = {
    "patient_id": 1,
    "attending_email": "h1255513@gmail.com",
    "user_age": 24,
}

info4 = {
    "patient_id": 3,
    "attending_email": "h1255513@gmail.com",
    "user_age": 24,
}

info2 = {
    "patient_id": 3,
    "heart_rate": 120
}

info3 = {
    "patient_id": 3,
    "heart_rate": 50
}

info1 = {
    "patient_id": "3",
    "heart_rate_average_since": "2018-11-16 20:02:11.601642",
}

url = "http://127.0.0.1:5000/api/heart_rate/interval_average"
y = requests.post("http://127.0.0.1:5000/api/new_patient", json=info4)
y = requests.post("http://127.0.0.1:5000/api/new_patient", json=info15)
y = requests.post("http://127.0.0.1:5000/api/heart_rate", json=info3)
y = requests.post("http://127.0.0.1:5000/api/heart_rate", json=info2)
# y = requests.post(url, json=info1)
print(y)
