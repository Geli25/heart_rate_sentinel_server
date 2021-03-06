import logging
import re

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "attending_email",
    "user_age"
]

patient_data = {}


def validate_patient_data(data_raw):
    """This function checks for invalid data when posting a
    new patient info.

    The function takes user input and check for errors. It can
    accommodate some mistakes such as typing the "id" instead of
    patient_id, entering a string instead of a number, etc.

    Args:
        data_raw(dict): A dictionary containing user information.

    Returns:
        dict: A dictionary containing validated user information.
    """
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
                    p_id = data_raw["patient_id"]
                    age = data_raw["user_age"]
                    email = data_raw["attending_email"]
                    if key == "patient_id":
                        if type(p_id) is int:
                            data_raw["patient_id"] = str(p_id)
                        if data_raw["patient_id"].isdigit() is False:
                            logging.error("The id must be a number")
                    if key == "attending_email":
                        if type(email) is str:
                            if re.match('[^@]+@[^@]+\.[^@]+', email) is None:
                                logging.error("The email format is not valid")
                                raise ValueError
                    if key == "user_age":
                        if type(age) is not int:
                            if type(age) is str:
                                data_raw["user_age"] = int(age)
                            else:
                                raise ValueError
                        if data_raw["user_age"] < 0:
                            raise ValueError
                    patient_data[key] = data_raw[key]
                else:
                    raise ValueError
            patient_data["heart_rate"] = []
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
