import csv
import json

if __name__ == '__main__':
    try:
        with open('output.csv', 'r', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f)
            data_list = [line for line in csv_reader]

        with open('input.json','w') as f:
            json.dump(data_list, f, ensure_ascii = False, indent = 4)

    except Exception as ex:
        print(f'error: {str(ex)}')
