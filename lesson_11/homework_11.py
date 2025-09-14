import csv
import json
import xml.etree.ElementTree as ET
from pathlib import Path
import logging

logging.basicConfig(
    filename='json__Smetaniuk.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

csv_folder = Path('ideas_for_test/work_with_csv')
csv_files = list(csv_folder.glob('*.csv'))

if len(csv_files) < 2:
    raise Exception("У теці має бути принаймні два CSV файли!")

rows_set = set()
all_rows = []

for file in csv_files[:2]:  # беремо перші два файли
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in rows_set:
                rows_set.add(row_tuple)
                all_rows.append(row)

with open('result_Smetaniuk.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(all_rows)

print("Завдання 1: CSV оброблено, файл result_Smetaniuk.csv створено.")

json_folder = Path('ideas_for_test/work_with_json')
for file in json_folder.glob('*.json'):
    try:
        with open(file, encoding='utf-8') as f:
            json.load(f)
    except Exception as e:
        logger.error(f"Файл {file.name} не валідний JSON: {e}")

print("Завдання 2: Валідація JSON завершена. Невалідні файли у лог-файлі.")


def find_timing_by_group_number(xml_file, group_number):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(group_number):
            timing = group.find('timingExbytes/incoming')
            if timing is not None:
                return timing.text
    return None


xml_file = Path('ideas_for_test/work_with_xml/groups.xml')
group_number_to_find = 1
timing_value = find_timing_by_group_number(xml_file, group_number_to_find)
if timing_value:
    logger.info(f"Timing для групи {group_number_to_find}: {timing_value}")
    print(f"Timing для групи {group_number_to_find}: {timing_value}")
else:
    logger.info(f"Групу з number={group_number_to_find} не знайдено.")
    print(f"Групу з number={group_number_to_find} не знайдено.")
