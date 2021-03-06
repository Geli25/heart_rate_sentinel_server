import logging
import datetime as dt

REQUIRED_REQUEST_KEYS = [
    "patient_id",
    "heart_rate_average_since"
]

patient_time_interval = {}


def validate_time_interval(hr_data):
    """This function checks for invalid data when a user posts
    a time interval from which to calculate the average bpm.

    Args:
        hr_data(dict): A dictionary containing an user id and
            a timestamp with the datetime.datetime format.

    Returns:
        dict: A dictionary containing validated interval info.
    """
    try:
        if type(hr_data) is dict:
            if "id" in hr_data.keys():
                hr_data["patient_id"] = hr_data.pop("id")
            for key in hr_data.keys():
                if key in REQUIRED_REQUEST_KEYS:
                    p_id = hr_data["patient_id"]
                    interval = hr_data["heart_rate_average_since"]
                    if key == "patient_id":
                        if type(p_id) is int:
                            str_id = str(p_id)
                            hr_data["patient_id"] = str_id
                        if hr_data["patient_id"].isdigit() is False:
                            logging.error("The id must be a number")
                    if key == "heart_rate_average_since":
                        if isinstance(interval, dt.datetime) is False:
                            if type(interval) is str:
                                tf = "%Y-%m-%d %H:%M:%S.%f"
                                dt.datetime.strptime(interval, tf)
                            else:
                                raise ValueError
                    patient_time_interval[key] = hr_data[key]
                else:
                    raise ValueError
            print(patient_time_interval)
            return patient_time_interval
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
