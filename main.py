
row_num = int(input("Numver of rows:\n> "))
row_list = []


def generating_rows(row_list, row_num):
    for i in range(0,row_num):
        row_list.append(list())

    for i in range(0,len(row_list)):
        parametrs = input("Enter parametrs of augmented matrix:\n> ")
        for num in parametrs.split():
            if num.isdigit():
                row_list[i].append(int(num))


def printing_matrix(row_list):
    string = ""
    for i in row_list:
        vertical_bar = "|"
        for entry in i:
            string = string + str(entry) + "|"
        string = string + "\n"
    print(string)

generating_rows(row_list, row_num)
printing_matrix(row_list)
