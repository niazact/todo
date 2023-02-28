import zipfile
import pathlib

FILEPATH="todos.txt"
num =5
def get_todos(filepath=FILEPATH):
    with open(filepath) as file:
        data = file.readlines()
        return data


def write_todos(todos_data,filepath=FILEPATH) :
    with open(filepath ,"w") as file:
        file.writelines(todos_data)


def make_archive(dest_dir, filepaths):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filename in filepaths:
            filename = pathlib.Path(filename)
            archive.write(filename, arcname=filename.name)




if __name__ == "__main__" :
    data=get_todos() ;
    data.append(input("Enter Todo : ") + "\n")
    write_todos(data)
    print(get_todos())
    make_archive("dest",
                 ["gui.py", "main.py"])


