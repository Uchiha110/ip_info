import os.path


def permanent_output_func(path):
    file_path = f"{path}"
    if os.path.exists(file_path):
        with open(f"{path}", "r") as f:
            return f.read()
    else:
        with open(f"{path}", "w") as f:
            f.write("True")
        with open(f"{path}", "r") as f:
            return f.read()
