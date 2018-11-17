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
    "heart_rate": 70
}

info3 = {
    "patient_id": 1,
    "heart_rate": 80
}

info1 = {
    "patient_id": "3",
    "heart_rate_average_since": "2018-11-17 16:41:47.420186",
}

url = "http://127.0.0.1:5000/api/heart_rate/interval_average"
# y = requests.post("http://vcm-7380.vm.duke.edu:5000/api/new_patient", json=info4)
# y = requests.post("http://vcm-7380.vm.duke.edu:5000/api/new_patient", json=info15)
# y = requests.post("http://vcm-7380.vm.duke.edu:5000/api/heart_rate", json=info3)
# y = requests.post("http://vcm-7380.vm.duke.edu:5000/api/heart_rate", json=info2)
# y = requests.post(url, json=info1)
print(y)
