batter_parameter = {"temperature": [0, 45, "Temperature", 5],
                    "soc": [20, 80, "Soc", 5],
                    "charge_rate": [0, 0.8, "Charge Rate", 5]}


def battery_status(battery_parameter_name):
    parameter_range = batter_parameter[battery_parameter_name["battery_parameter"]]
    low = parameter_range[0]
    high = parameter_range[1]
    low_warning = parameter_range[0] * (100 - parameter_range[3])
    high_warning = parameter_range[1] * (100 - parameter_range[3])
    value = battery_parameter_name["value"]
    if value <= low or value >= high:
        print('{} is out of range!'.format(parameter_range[2]))
        return False
    elif value <= low_warning:
        print('{} nearing low threshold value!'.format(parameter_range[2]))
    elif value >= high_warning:
        print('{} nearing high threshold value!'.format(parameter_range[2]))
        return True
    return True


if __name__ == '__main__':
    assert (battery_status({"battery_parameter": "temperature", "value": 25}) is True)
    assert (battery_status({"battery_parameter": "soc", "value": 70}) is True)
    assert (battery_status({"battery_parameter": "soc", "value": 21}) is True)
    assert (battery_status({"battery_parameter": "charge_rate", "value": 0.7}) is True)
    assert (battery_status({"battery_parameter": "temperature", "value": 50}) is False)
    assert (battery_status({"battery_parameter": "soc", "value": 85}) is False)
    assert (battery_status({"battery_parameter": "soc", "value": 19}) is False)
    assert (battery_status({"battery_parameter": "charge_rate", "value": 0}) is False)
