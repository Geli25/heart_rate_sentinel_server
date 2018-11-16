import logging


def calculate_avg(data):
    try:
        if isinstance(data, list):
            heart_rates = []
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
            heart_rates = []
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

if __name__ == '__main__':
    print(calculate_avg(([[1, "2018/03/09"], [2, "2"], [100, "2"]])))
    print(calculate_avg([[1, "2018/03/09"], [2, "2"], [0, "2"]]))