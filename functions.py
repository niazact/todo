FILEPATH="todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath) as file:
        data=file.readlines()
        return data


def write_todos(todos_data,filepath=FILEPATH) :
    with open(filepath ,"w") as file:
        file.writelines(todos_data)



if __name__ == "__main__" :
    data=get_todos() ;
    data.append(input("Enter Todo : ") + "\n")
    write_todos(data)
    print(get_todos())


