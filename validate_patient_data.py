import logging
import re

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "attending_email",
    "user_age"
]

patient_data = {}


def validate_patient_data(data_raw):
    try:
        if type(data_raw) is dict:
            if "id" in data_raw.keys():
                data_raw["patient_id"] = data_raw.pop("id")
            if "email" in data_raw.keys():
                data_raw["attending_email"] = data_raw.pop("email")
            if "age" in data_raw.keys():
                data_raw["user_age"] = data_raw.pop("age")
            for key in data_raw.keys():
                if key in REQUIRED_REQUEST_KEYS:
                    if key == "patient_id":
                        if type(data_raw["patient_id"]) is int:
                            data_raw["patient_id"] = str(data_raw["patient_id"])
                        if data_raw["patient_id"].isdigit() is False:
                            logging.error("The id must be a number")
                    if key == "attending_email":
                        if type(data_raw["attending_email"]) is str:
                            if re.match('[^@]+@[^@]+\.[^@]+',data_raw["attending_email"]) is None:
                                logging.error("The email address format is not valid")
                                raise ValueError
                    if key == "user_age":
                        if type(data_raw["user_age"]) is not int:
                            if type(data_raw["user_age"]) is str:
                                data_raw["user_age"] = int(data_raw["user_age"])
                            else:
                                raise ValueError
                    patient_data[key] = data_raw[key]
                else:
                    raise ValueError
            print(patient_data)
            return patient_data
        else:
            raise TypeError
    except TypeError:
        logging.error("TypeError: The input value must be a dictionary")
        return "TypeError"
    except ValueError:
        logging.error("ValueError: Required fields format incorrect")
        return "ValueError"
    except AttributeError:
        logging.error("ValueError: Required fields format incorrect")
        return "ValueError"
