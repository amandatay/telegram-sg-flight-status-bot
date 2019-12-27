
def format_search_res_output(res_list):
    if len(res_list) > 3:
        out = ['{} results found; showing top 3 results only\n'.format(len(res_list))]
    else:
        out = ['{} results found:\n'.format(len(res_list))]

    res_len = min(len(res_list), 3)

    for _ in range(res_len):
        out.append('''--- \nStatus: {}\nEstimated {} time: {}\nFlight Code: {}\nAirline: {}'''.
                   format(res_list[_]['flight_status'],
                          res_list[_]['flight_status'],
                          res_list[_]['estimated_time'],
                          res_list[_]['flight_code'],
                          res_list[_]['airline']))
    return out