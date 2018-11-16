import logging

heart_rates = []


def calculate_avg(data):
    try:
        if isinstance(data, list):
            for heart_rate in data:
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
