import logging
import datetime as dt

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "heart_rate"
]

patient_heart_rate = {}


def validate_heart_rate(hr_data, time):
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
