import pytest
from validate_patient_data import validate_patient_data
from validate_heart_rate import validate_heart_rate
from validate_time_interval import validate_time_interval
from calculate_avg import calculate_avg
from calculate_interval_avg import calculate_interval_avg
from check_tachycardia import check_tachycardia
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
        "heart_rate": []
     }), ({
        "id": 1,
        "email": "suyash.kumar@duke.edu",
        "age": 50,
     }, {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
        "heart_rate": []
     }), ({
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": "50",
     }, {
        "patient_id": "1",
        "attending_email": "suyash.kumar@duke.edu",
        "user_age": 50,
        "heart_rate": []
     }), ({
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": "50",
     }, {
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": 50,
         "heart_rate": []
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
    ({
         "patient_id": "1",
         "attending_email": "suyash.kumar@duke.edu",
         "user_age": -50,
     }, "ValueError"),
    ({1}, "TypeError")
])
def test_validate_patient_data(data, expected):
    d = validate_patient_data(data)
    assert d == expected


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
    ({
         "patient_id": "1",
         "heart_rate": -100
     }, (2018, 11, 15, 21, 43, 19, 235776),
     "ValueError"),
])
def test_validate_heart_rate(data, time, expected):
    d = validate_heart_rate(data, time)
    assert d == expected


@pytest.mark.parametrize("data, expected", [
    ({
        "patient_id": "1",
        "heart_rate_average_since": "2018-03-09 11:00:36.372339",
    }, {
        "patient_id": "1",
        "heart_rate_average_since": "2018-03-09 11:00:36.372339",
    }),             ({
        "patient_id": 1,
        "heart_rate_average_since": "2018-03-09 11:00:36.372339",
    }, {
        "patient_id": "1",
        "heart_rate_average_since": "2018-03-09 11:00:36.372339",
    }),             ({
        "patient_id": 1,
        "heart_rate_average_since": "2018/03/09 11:00:36.372339",
    }, "ValueError"),             ({
        "patient_id": 1,
        "heart_rate_average_since": 2,
    }, "ValueError")
])
def test_validate_time_interval(data, expected):
    d = validate_time_interval(data)
    assert d == expected


@pytest.mark.parametrize("data, expected", [
    ([[1, "2018/03/09"], [2, "2"], [100, "2"]], 34),
    ("hi", "ValueError"),
    ([["hi", 2], [3, 5]], "ValueError"),
    ([[], []], "IndexError"),
])
def test_calculate_avg(data, expected):
    assert calculate_avg(data) == expected


@pytest.mark.parametrize("data,interval,expected", [
    ([[1, 3], [2, 10], [50, 20]], 0, "IndexError"),
    ([[1, 3], [2, 10], [50, 20]], 20, 50),
    ([[100, 2], [78, 3], [51, 4]], 3, 64),
])
def test_calculate_interval_avg(data, interval, expected):
    d = calculate_interval_avg(data, interval)
    assert d == expected


@pytest.mark.parametrize("data,expected", [
    ({
        "patient_id": "1",
        "user_age": 50,
        "heart_rate": [[110, 10], [50, 20]],
    }, (True, 20)),    ({
        "patient_id": "1",
        "user_age": 10,
        "heart_rate": [[100, 10], [50, "20"]],
    }, (False, "20")),    ({
        "patient_id": "1",
        "user_age": 12,
        "heart_rate": [[120, 10], [50, 20]],
    }, (True, 20)),    ({
        "patient_id": "1",
        "user_age": 1,
        "heart_rate": [[70, 20], [151, 10]],
    }, (False, 10))
])
def test_check_tachycardia(data, expected):
    d = check_tachycardia(data)
    assert d == expected
