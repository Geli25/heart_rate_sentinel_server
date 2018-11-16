import pytest
from validate_patient_data import validate_patient_data
from validate_heart_rate import validate_heart_rate
import datetime as dt


@pytest.mark.parametrize("data, expected", [
    ({
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
     }, {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
     }), ({
        "id": 1,
        "email": "suyash.kumar@duke.edu",
        "age": 50,
     }, {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
     }), ({
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": "50",
     }, {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
     }), ({
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": 50,
     }, {
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": "50",
     }), ({
         "patient_id": [1, 2],
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": 50,
     }, "ValueError"),
    ({
         "patient_id": 1,
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": 50.2,
     }, "ValueError"),
    ({
         "patient_id": 1,
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": [1, 2],
     }, "ValueError"),
    ({
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke@edu",
         "user_age": 50,
     }, "ValueError"),
    ({1}, "TypeError"), ([1, 2, 3], "TypeError"),
    ({
         "patients_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": 50,
     }, "ValueError"),
    ({1}, "TypeError")
])
def test_validate_patient_data(data, expected):
    validate_patient_data(data)


@pytest.mark.parametrize("data, time, expected", [
    ({
        "patient_id": "1",
        "heart_rate": 100
    }, dt.datetime(2018, 11, 15, 21, 43, 19, 235776),
    {
        "patient_id": "1",
        "heart_rate": [100,
                       '2018-11-15 21:43:19.235776']
    }),         ({
        "patient_id": 1,
        "heart_rate": "100"
    }, dt.datetime(2018, 11, 15, 21, 43, 19, 235776),
    {
        "patient_id": "1",
        "heart_rate": [100,
                       '2018-11-15 21:43:19.235776']
    }),
    ({
         "patient_id": [1, 2],
         "heart_rate": 100
     }, dt.datetime(2018, 11, 15, 21, 43, 19, 235776),
        "ValueError"),
    ({
         "patient_id": "1",
         "heart_rate": [1, 2]
     }, dt.datetime(2018, 11, 15, 21, 43, 19, 235776),
        "ValueError"),
    ({
         "patient_id": "1",
         "heart_rate": 100
     }, '2018-11-15 21:43:19.235776',
        "ValueError"),
])
def test_validate_heart_rate(data, time, expected):
    validate_heart_rate(data, time)
