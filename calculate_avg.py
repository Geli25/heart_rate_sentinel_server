import logging


def calculate_avg(hr_data):
    """This function calculates the average bpm based on all
    user heart rate.

    Args:
        hr_data(list): An array containing arrays of heart rate data.

    Returns:
        int: The average of based on all heart rates in the array.
    """
    try:
        if isinstance(hr_data, list):
            heart_rates = []
            for heart_rate in hr_data:
                if isinstance(heart_rate, list):
                    if type(heart_rate[0]) is str:
                        heart_rate[0] = int(heart_rate[0])
                    if type(heart_rate[0]) is int:
                        heart_rates.append(heart_rate[0])
                    else:
                        raise ValueError
                else:
                    raise ValueError
            avg = sum(heart_rates)/heart_rates.__len__()
            avg_int = int(avg)
            # Clear array after calculation
            heart_rates = []
            print(avg_int)
            return avg_int
        else:
            raise ValueError
    except ValueError:
        logging.error("Input must be array containing arrays of int")
        return "ValueError"
    except IndexError:
        logging.error("No input detected, array is empty")
        return "IndexError"
