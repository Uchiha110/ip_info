from main_write_db import main_write_db
from main_select_db import main_select_db
from main_delete_file import main_delete_file


def main():
    i = input("(write/select/delete): ")
    if i.lower() == "write":
        main_write_db()
    elif i.lower() == "select":
        main_select_db()
    elif i.lower() == "delete":
        main_delete_file()


if __name__ == '__main__':
    main()
