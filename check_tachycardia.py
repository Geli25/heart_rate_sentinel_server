import logging

timestamps = []


def check_tachycardia(data):
    age = data["user_age"]
    heart_rates = data["heart_rate"]
    try:
        if "heart_rate" in data:
            if age <= 2:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 151:
                        timestamps.append(heart_rate[1])
            if 2 < age <= 4:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 137:
                        timestamps.append(heart_rate[1])
            if 4 < age <= 7:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 133:
                        timestamps.append(heart_rate[1])
            if 7 < age <= 11:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 130:
                        timestamps.append(heart_rate[1])
            if 11 < age <= 15:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 119:
                        timestamps.append(heart_rate[1])
            if age > 15:
                for heart_rate in heart_rates:
                    if heart_rate[0] > 100:
                        timestamps.append(heart_rate[1])
            if len(timestamps) == 0:
                is_tachycardic = False
                print(is_tachycardic, heart_rates[-1][-1])
                return is_tachycardic, heart_rates[-1][-1]
            is_tachycardic = True
            print(is_tachycardic, heart_rates[-1][-1])
            return is_tachycardic, heart_rates[-1][-1]

        else:
            raise ValueError
    except ValueError:
        logging.error("This patient has no heart rate data")
