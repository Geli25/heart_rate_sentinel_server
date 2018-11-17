import logging
import datetime as dt

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "heart_rate"
]

patient_heart_rate = {}


def validate_heart_rate(hr_data, time):
    """This function checks for invalid data when a user posts a heart rate.

    The function takes user input and check for errors. It can
    accommodate some mistakes such as typing the "id" instead of
    patient_id, entering a string instead of a number, etc.

    Args:
        hr_data(dict): A dictionary containing id data and heart rate.
        time (datetime.datetime): A time created using datetime.now().

    Returns:
        list: A list containing the entered heart rate and timestamp.
    """
    try:
        if isinstance(time, dt.datetime) is False:
            raise ValueError
        else:
            time = str(time)
        if type(hr_data) is dict:
            if "id" in hr_data.keys():
                hr_data["patient_id"] = hr_data.pop("id")
            for key in hr_data.keys():
                if key in REQUIRED_REQUEST_KEYS:
                    p_id = hr_data["patient_id"]
                    heart_rate = hr_data["heart_rate"]
                    if key == "patient_id":
                        if type(p_id) is int:
                            str_id = str(p_id)
                            hr_data["patient_id"] = str_id
                        if hr_data["patient_id"].isdigit() is False:
                            logging.error("The id must be a number")
                    if key == "heart_rate":
                        if type(heart_rate) is not int:
                            if type(heart_rate) is str:
                                heart_rate = int(heart_rate)
                            else:
                                raise ValueError
                        if heart_rate < 0:
                            raise ValueError
                    patient_heart_rate[key] = hr_data[key]
                    patient_heart_rate["heart_rate"] = [heart_rate, time]
                else:
                    raise ValueError
            print(patient_heart_rate)
            return patient_heart_rate
        else:
            raise TypeError
    except TypeError:
        logging.error("TypeError: The input value must be a dictionary")
        return "TypeError"
    except AttributeError:
        logging.error("ValueError: Required fields format incorrect")
        return "ValueError"
    except ValueError:
        logging.error("ValueError: Required fields format incorrect")
        return "ValueError"
    except KeyError:
        logging.error("ValueError: Required fields format incorrect")
        return "ValueError"
