import csv


def filter_csv(input_file, output_file, keyword):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if keyword not in row[0]:  # Проверяем, содержит ли первый столбец ключевое слово
                writer.writerow(row)


# Пример использования: удалить строки, где первый столбец содержит "Mahindra Quanto C8"
input_file = 'quikr_car.csv'
output_file = 'output.csv'
keyword = 'Mahindra KUV100'

filter_csv(input_file, output_file, keyword)