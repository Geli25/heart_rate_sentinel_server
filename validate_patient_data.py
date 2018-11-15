import logging

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "attending_email",
    "user_age"
]

patient_data = {}


def validate_patient_data(data):
    try:
        if type(data) == dict:
            for key in data.keys():
                if key in REQUIRED_REQUEST_KEYS:
                    patient_data[key] = data[key]
                else:
                    raise ValueError
            print(patient_data)
            return patient_data
        else:
            raise TypeError
    except TypeError:
        logging.error("The input value must be a dictionary")
    except ValueError:
        logging.error("Missing required fields or fields have typos, ensure they are correct")


if __name__ == '__main__':
    data = {
        "patient_id": "1",
        "email": "suyash.kumar@duke.edu",
        "user_age": 50,
    }
    validate_patient_data(data)
