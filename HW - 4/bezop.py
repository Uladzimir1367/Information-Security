import csv
from collections import Counter

# Путь к файлу CSV
file_path = 'угрозы.csv'

# Загрузка данных из CSV-файла
with open(file_path, mode='r', encoding='utf-8') as file:
   reader = csv.reader(file)
# Пропустить заголовок
   next(reader)
# Считывание всех мер защиты из столбца H в список
   measures = [row[7] for row in reader]  # Индекс 7, так как индексация начинается с 0

# Подсчет вклада каждой меры защиты
   measures_count = Counter(measures)

# Сортировка мер защиты по убыванию 
   sorted_measures = sorted(measures_count.items(), key=lambda item: item[1], reverse=True)

# Запись результатов в файл
with open('результаты.txt', 'w', encoding='utf-8') as output_file:
   for measure, count in sorted_measures:
      output_file.write(f'{measure}: {count} баллов\n')

   print('Результаты в файле результаты.txt')