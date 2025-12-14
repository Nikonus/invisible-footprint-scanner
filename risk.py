# risk.py
def calculate_risk(results):
    found = sum(results.values())

    if found == 0:
        return 0.0
    elif found <= 2:
        return 3.5
    elif found <= 4:
        return 6.2
    else:
        return 8.5
