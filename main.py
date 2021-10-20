row_num = int(input("Number of rows:\n> "))
row_list = []

def generating_rows(row_list, row_num):
    for i in range(0,row_num):
        row_list.append(list())

def adding_parametrs(row_list, row_num):
    for i in range(0,row_num):
        parametrs = input("Enter parametrs of augmented matrix:\n> ")

        if parametrs == "":
            print("You didn't enter any value, try again.")
        else:
            for num in parametrs.split():
                if num.isdigit():
                    row_list[i].append(int(num))

def printing_matrix(row_list):
    string = ""
    for i in row_list:
        for entry in i:
            string = string + str(entry) + "|"
        string = string + "\n"
    print(string)



def sorting_rows(row_list):
    leading_entry = 0
    for i in range(0,len(row_list)):
        if row_list[i][leading_entry] != 0:
            if i == 0:
                pass

            else:
                reserve = row_list[leading_entry]
                row_list[leading_entry] = row_list[i]
                row_list[i] = reserve
                leading_entry += 1

generating_rows(row_list, row_num)
adding_parametrs(row_list, row_num)
sorting_rows(row_list)
printing_matrix(row_list)
