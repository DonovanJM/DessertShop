def load_employees():
    file = open("employees.csv")
    employee_data = file.read()
    lines = employee_data.split("-")
    print(lines)
    print("\n\n\n\n\n")
    for i in range(len(lines) - 1):
        if i == 0:
            first_num = lines[0]
            lines.pop(0)
            lines[0] = first_num + "-" + lines[0]
        else:
            previous_string = lines[i-1]
            previous_num = previous_string[-2] + previous_string[-1]
            lines[i] = previous_num + "-" + lines[i]
    for i in range(len(lines) - 1):
        lines[i] = lines[i][:-2]
        lines[i].strip()
    print(lines)


def main():
    load_employees()


if __name__ == "__main__":
    main()
