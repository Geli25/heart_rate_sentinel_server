import logging
import pandas as pd


def calculate_interval_avg(data, interval):
    try:
        if isinstance(data, list):
            for heart_rate in data:
                if isinstance(heart_rate, list):
                    if type(heart_rate[0]) is not int:
                        if type(heart_rate[0]) is str:
                            heart_rate[0] = int(heart_rate[0])
                        else:
                            raise ValueError
                else:
                    raise ValueError
            df = pd.DataFrame(data, columns=['heart_rate', 'time'])
            index = df.loc[df['time'] == interval].index[0]
            filtered_hr = df.loc[index:]["heart_rate"]
            print(filtered_hr)
            avg = int(filtered_hr.sum()/len(filtered_hr.index))
            print(avg)
            return avg
        else:
            raise ValueError
    except ValueError:
        logging.error("Input must be array containing arrays of int")
        return "ValueError"
    except IndexError:
        logging.error("The array or the interval does not exist")
        return "IndexError"
