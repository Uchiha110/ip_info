import os
from pyfiglet import Figlet
import keyboard


def main_delete_file():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("IP INFO DELETE"))

    dir_html_one = "html_output_file\\html_output_file_one"
    dir_html_all = "html_output_file\\html_output_file_all"
    dir_json_one = "json_output_file\\json_output_file_one"
    dir_json_all = "json_output_file\\json_output_file_all"
    dir_exel_one = "exel_output_file\\exel_output_file_one"
    dir_exel_all = "exel_output_file\\exel_output_file_all"

    for f in os.listdir(dir_html_one):
        os.remove(os.path.join(dir_html_one, f))

    for f in os.listdir(dir_html_all):
        os.remove(os.path.join(dir_html_all, f))

    for f in os.listdir(dir_json_one):
        os.remove(os.path.join(dir_json_one, f))

    for f in os.listdir(dir_json_all):
        os.remove(os.path.join(dir_json_all, f))

    for f in os.listdir(dir_exel_one):
        os.remove(os.path.join(dir_exel_one, f))

    for f in os.listdir(dir_exel_all):
        os.remove(os.path.join(dir_exel_all, f))

    print('File deletion was successful!')

    print('Press Enter to exit')
    keyboard.wait('enter')
