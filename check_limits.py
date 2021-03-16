battery_parameter = {"temperature": [0, 45, "Temperature", 5, 'Temperatur'],
                     "soc": [20, 80, "Soc", 5, "SOC"],
                     "charge_rate": [0, 0.8, "Charge Rate", 5, "Ladestrom"]}
language_text = {"failed": ["battery-{}: {} is out of range!",
                            "battery-{}: {} ist außerhalb der Reichweite!"],
                 "warning": ["Warning:battery-{}: {} is nearing the {} limit",
                             "Warnung:battery-{}: Der Wert {} nähert sich der Grenze {}"]}
language = "EN"
language_code = {"EN": 0, "DE": 1}
battery_status_list = {}


def battery_status(battery_parameter_name):
    parameter_range = battery_parameter[battery_parameter_name["battery_parameter"]]
    low = parameter_range[0]
    high = parameter_range[1]
    low_warning = parameter_range[0] + (parameter_range[1] * parameter_range[3]) / 100
    high_warning = parameter_range[1] * (100 - parameter_range[3]) / 100
    value = battery_parameter_name["value"]
    battery_no = battery_parameter_name["battery_number"]
    if value <= low or value >= high:
        print_error = language_text["failed"][language_code[language]]. \
            format(battery_no, parameter_range[2])
        battery_status_list[battery_no].append(print_error)
        report_details(print_error)
        return False
    compare_battery_param_value(low_warning, value, "lower", parameter_range, battery_no)
    compare_battery_param_value(value, high_warning, "higher", parameter_range, battery_no)
    return True


def consolidated_battery_report(battery_parameters):
    battery_status_list[battery_parameters[3]] = []
    battery_status({"battery_number": battery_parameters[3],
                    "battery_parameter": "temperature", "value": battery_parameters[0]})
    battery_status({"battery_number": battery_parameters[3],
                    "battery_parameter": "soc", "value": battery_parameters[1]})
    battery_status({"battery_number": battery_parameters[3],
                    "battery_parameter": "charge_rate", "value": battery_parameters[2]})


def compare_battery_param_value(lower_value, upper_value, boundary, parameter_range, battery_no):
    if lower_value >= upper_value:
        print_warning = language_text["warning"][language_code[language]]. \
            format(battery_no, parameter_range[2], boundary)
        battery_status_list[battery_no].append(print_warning)
        report_details(print_warning)


def report_details(print_string):
    print(print_string)

if __name__ == '__main__':
    consolidated_battery_report([50, 23, -1, '1234'])
    consolidated_battery_report([75, 10, 10, '1235'])
    consolidated_battery_report([25, 10, 1, '1234'])

    battery_status_list['3425'] = []
    assert (battery_status({"battery_number":'3425',"battery_parameter": "temperature", "value": 25}) )is True
    assert (battery_status({"battery_number":'3425', "battery_parameter": "temperature", "value": 50}) is False)
    assert (battery_status({"battery_number":'3425', "battery_parameter": "charge_rate", "value": 0}) is False)
    assert (battery_status({"battery_number":'3425', "battery_parameter": "soc", "value": 23}) is True)
    language = "DE"
    assert (battery_status({"battery_number":'3425', "battery_parameter": "soc", "value": 77}) is True)
    assert (battery_status({"battery_number":'3425', "battery_parameter": "temperature", "value": 50}) is False)
    del battery_status_list['3425']
    report_details(battery_status_list)
