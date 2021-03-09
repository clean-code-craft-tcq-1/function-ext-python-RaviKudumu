battery_parameter = {"temperature": [0, 45, "Temperature", 5, 'Temperatur'],
                    "soc": [20, 80, "Soc", 5, "SOC"],
                    "charge_rate": [0, 0.8, "Charge Rate", 5, "Ladestrom"]}
language_text = {"failed": ["{} is out of range!", "{} ist außerhalb der Reichweite!"],
                 "warning": ["Warning: {} is nearing the {} limit",
                             "Warnung:Der Wert {} nähert sich der Grenze {}"]}

language_code = {"EN": 0, "DE": 1}
def battery_status(battery_parameter_name, language):
    parameter_range = battery_parameter[battery_parameter_name["battery_parameter"]]
    low = parameter_range[0]
    high = parameter_range[1]
    low_warning = parameter_range[0] + ( parameter_range[1] * parameter_range[3])/100
    high_warning = parameter_range[1] * (100 - parameter_range[3])/100
    value = battery_parameter_name["value"]
    if value <= low or value >= high:
        print(language_text["failed"][language_code[language]].format(parameter_range[2]))
        return False
    compare_battery_param_value(low_warning, value, "lower", parameter_range, language)
    compare_battery_param_value(value, high_warning, "higher",parameter_range,language)
    return True

def compare_battery_param_value(lower_value, upper_value, boundary,parameter_range, language):
    if lower_value >= upper_value:
        print(language_text["warning"][language_code[language]].format(parameter_range[2], boundary) )




if __name__ == '__main__':
    assert (battery_status({"battery_parameter": "temperature", "value": 25}, "EN") )is True
    assert (battery_status({"battery_parameter": "soc", "value": 77},"DE") is True)
    assert (battery_status({"battery_parameter": "soc", "value": 23},"EN") is True)
    assert (battery_status({"battery_parameter": "temperature", "value": 50}, "EN") is False)
    assert (battery_status({"battery_parameter": "temperature", "value": 50}, "DE") is False)
    assert (battery_status({"battery_parameter": "charge_rate", "value": 0}, 'EN') is False)
