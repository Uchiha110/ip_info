from datetime import datetime


def date_time_func():
    current_datetime = datetime.now()
    date_time = f"{current_datetime.day}{current_datetime.month}{current_datetime.year}{current_datetime.hour}{current_datetime.minute}{current_datetime.second}"
    return date_time


def name_file_func(response, date_time):
    name_file = f"{response[3]}_{response[5]}_{response[8]}_{response[9]}_{response[1]}_{date_time}"
    return name_file
