import folium

from permanent_output import permanent_output_func


def write_html_map_func(name_file, response, oneall):
    if permanent_output_func("html_output_file\\permanent_output_html.txt") == "True":
        if oneall == 'one':
            area = folium.Map(location=[float(response[12]), float(response[13])])
            area.save(f"html_output_file\\html_output_file_one\\{name_file}.html")
        elif oneall == 'all':
            pass
    elif permanent_output_func("html_output_file\\permanent_output_html.txt") == "False":
        pass
