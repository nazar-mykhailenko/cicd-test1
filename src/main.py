def read_file(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
    return lines
