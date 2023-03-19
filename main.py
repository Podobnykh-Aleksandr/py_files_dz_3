# работа с тремя файлами и вывод в один новый

def read_from_file():
    list_files_in_dir = ['1.txt', '2.txt', '3.txt']
    string_from_files = []
    for file in list_files_in_dir:
        with open (file, 'r', encoding='utf-8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            string_from_files.append(temp)
    string_from_files.sort(key=len)

    file = 'comp_text.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for string in string_from_files:
            for i in string:
                f.writelines(i + '\n')
    return

read_from_file()



