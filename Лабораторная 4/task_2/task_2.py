import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as input_file:
        csv_data = csv.DictReader(input_file)
        data_list = [d for d in csv_data]

    with open(OUTPUT_FILENAME, "w") as output_file:
        json.dump(data_list, output_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
