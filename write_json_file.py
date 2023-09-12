import json

from permanent_output import permanent_output_func


def write_json_file_func(name_file, data, oneall):
    if permanent_output_func("json_output_file\\permanent_output_json.txt") == "True":
        if oneall == 'one':
            with open(f"json_output_file\\json_output_file_one\\{name_file}.json", "a",
                      encoding='utf-8') as f:
                json.dump(([{"person_id": data[0], "query": data[1], "status": data[2], "continent": data[3],
                             "continentCode": data[4], "country": data[5], "countryCode": data[6], "region": data[7],
                             "regionName": data[8], "city": data[9], "district": data[10], "zip": data[11],
                             "lat": data[12], "lon": data[13], "timezone": data[14], "offset": data[15],
                             "currency": data[16], "isp": data[17], "org": data[18], "as": data[19], "asname": data[20],
                             "mobile": data[21], "proxy": data[22], "hosting": data[23]}]), f, indent=4,
                          ensure_ascii=False)
        elif oneall == 'all':
            with open(f"json_output_file\\json_output_file_all\\all_data_person_{name_file}.json", "a",
                      encoding='utf-8') as f:
                json.dump(([{"person_id": d[0], "query": d[1], "status": d[2], "continent": d[3],
                             "continentCode": d[4], "country": d[5], "countryCode": d[6], "region": d[7],
                             "regionName": d[8], "city": d[9], "district": d[10], "zip": d[11], "lat": d[12],
                             "lon": d[13], "timezone": d[14], "offset": d[15], "currency": d[16], "isp": d[17],
                             "org": d[18], "as": d[19], "asname": d[20], "mobile": d[21], "proxy": d[22],
                             "hosting": d[23]} for d in data]), f, indent=4, ensure_ascii=False)
    elif permanent_output_func("json_output_file\\permanent_output_json.txt") == "False":
        pass
