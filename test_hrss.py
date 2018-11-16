import pytest
from validate_patient_data import validate_patient_data

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
def test_import_data(data, expected):
    validate_patient_data(data)
