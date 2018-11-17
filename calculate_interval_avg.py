import logging
import pandas as pd


def calculate_interval_avg(hr, interval):
    """This function calculates the average bpm based on user
    specified timestamp.

    Args:
        hr(list): An array containing arrays of heart rate data.
        interval(string): A string containing a valid datetime
            timestamp.

    Returns:
        int: The average of based on user specified timestamp.
    """
    try:
        if isinstance(hr, list):
            for heart_rate in hr:
                if isinstance(heart_rate, list):
                    if type(heart_rate[0]) is not int:
                        if type(heart_rate[0]) is str:
                            heart_rate[0] = int(heart_rate[0])
                        else:
                            raise ValueError
                else:
                    raise ValueError
            df = pd.DataFrame(hr, columns=['heart_rate', 'time'])
            print(df)
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
