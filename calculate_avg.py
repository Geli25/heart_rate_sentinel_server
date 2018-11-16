heart_rates = []


def calculate_avg(data):
    for heart_rate in data:
        heart_rates.append(heart_rate[0])
    avg = sum(heart_rates)/heart_rates.__len__()
    print(avg)
    return avg
