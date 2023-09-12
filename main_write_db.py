from pyfiglet import Figlet
import keyboard

from get_info_by_ip import get_info_by_ip_func
from write_person_db import write_person_db_func


def main_write_db():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP INFO WRITE"))
    ip = input("Please enter a target IP: ").replace(" ", "")

    write_person_db_func(get_info_by_ip_func(ip=ip))

    for k, v in get_info_by_ip_func(ip=ip).items():
        print(f'{k} : {v}')

    print('Press Enter to exit')
    keyboard.wait('enter')
