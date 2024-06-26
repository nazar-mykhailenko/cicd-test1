def read_file(file_path):
    with open(file_path, "r") as input_file:
        lines = input_file.readlines()
    return lines


def write_to_file(file_path, lines):
    with open(file_path, "w") as output_file:
        output_file.writelines(lines)


def filter_lines(lines, keyword):
    new_lines = []
    for line in lines:
        if keyword in line:
            new_lines.append(line)
    return new_lines


def main():
    lines = read_file("../input.txt")
    keyword = input("Enter keyword: ").strip().lower()
    filtered_lines = filter_lines(lines, keyword)
    write_to_file("filtered.txt", filtered_lines)


if __name__ == "__main__":
    main()
