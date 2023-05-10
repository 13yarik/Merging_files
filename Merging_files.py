def files_open(file_names):
    with open('Итоговый файл.txt', 'w') as out_file:
        files_data = []  # список для хранения информации о файлах и их строках
        for f_name in file_names:
            with open(f_name) as in_file:
                file_lines = [line.strip() for line in in_file]  # читаем строки файла и удаляем символы перевода строки
                files_data.append((f_name, len(file_lines), file_lines))  # добавляем информацию о файле в список
        # сортируем список по количеству строк в файле (второй элемент кортежа)
        sorted_files_data = sorted(files_data, key=lambda x: x[1])
        # проходим по отсортированному списку и записываем содержимое файлов в результирующий файл
        for f_name, num_lines, file_lines in sorted_files_data:
            out_file.write(f"{f_name}\n{num_lines}\n")  # записываем информацию о файле
            for line in file_lines:
                out_file.write(f"{line}\n")  # записываем строки файла и символ перевода строки

file_names_list = files_open(['1.txt', '2.txt'])



