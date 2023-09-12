from pyfiglet import Figlet
import keyboard

from select_person_db import select_person_db_func
# from write_html_map import write_html_map_func
from write_json_file import write_json_file_func
# from write_exel_table import write_exel_table_func
from date_time_name_file import date_time_func, name_file_func


def main_select_db():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP INFO SELECT"))
    oneall = input("Do you want to interact with the whole table or just one person? (one/all): ").replace(" ", "")

    if oneall.lower() == 'one':
        column_name = input("Enter column name (person_id/query/status/continent/continentCode"
                            "/country/countryCode/region/regionName/city/district/zip/lat/lon"
                            "/timezone/offset/currency/isp/org/as/asname/mobile/proxy/hosting): ").replace(" ", "")
        date = input("Enter the search information in the column above: ")

        name_file_one = name_file_func(select_person_db_func(column_name=column_name, date=date, oneall=oneall), date_time_func())
        # write_html_map_func(name_file_one, select_person_db_func(column_name=column_name, date=date, oneall=oneall), oneall)
        write_json_file_func(name_file_one, select_person_db_func(column_name=column_name, date=date, oneall=oneall), oneall)
        # write_exel_table_func(name_file_one, select_person_db_func(column_name=column_name, date=date, oneall=oneall), oneall)

        print(select_person_db_func(column_name=column_name, date=date, oneall=oneall))
    elif oneall.lower() == 'all':
        write_json_file_func(date_time_func(), select_person_db_func(oneall=oneall), oneall)

    print('Press Enter to exit')
    keyboard.wait('enter')
