import PySimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt",'w') as file:
        pass


sg.theme("LightGreen2")
label1 = sg.Text("Type in the To-Do")
clock = sg.Text(key="clock")
input_box1 = sg.InputText(tooltip="Enter Todo",
                          key="todo")
add_button = sg.Button("Add",size=8)
exit_button = sg.Button('Exit',size=8)
listbox = sg.Listbox(values=functions.get_todos(),
                     key="todos",
                     enable_events=True,
                     size=[45, 10])
edit_button = sg.Button("Edit",size=8)
complete_button = sg.Button("Complete")


window = sg.Window('To Do List', layout=[[clock],
                    [label1],
                    [input_box1],
                    [listbox],
                    [add_button,
                     edit_button,
                     complete_button,
                     exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values=window.read(timeout=200)
    window['clock'].update(value=time.strftime("%B %d, %Y %H:%M:%S"))
    print(f"event: {event}, values: {values}")
    print(1,values['todo'])
    print(2,values['todos'])


    match event:
        case 'Add':
            local_todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            local_todos.append(new_todo)
            functions.write_todos(local_todos)
            window['todos'].update(values=local_todos)

        case "todos":
            edit_todo = values['todos'][0]
            window['todo'].update(value=edit_todo)

        case "Edit":
            try:
                local_todos = functions.get_todos()
                new_todo = values['todo']
                edit_todo = values['todos'][0]
                if new_todo != edit_todo :
                    index=local_todos.index(edit_todo)
                    local_todos[index]=new_todo + '\n'
                    functions.write_todos(local_todos)
                    window['todos'].update(values=local_todos)
            except IndexError:
                    sg.popup("Please Select the Item",font=("Helvetica", 12),modal=True)
        case "Complete":
            try:
                local_todos = functions.get_todos()
                delete_todo = values['todos'][0]
                if delete_todo != " ":
                    local_todos.remove(delete_todo)
                    functions.write_todos(local_todos)
                    window['todos'].update(values=local_todos)
                    window['todo'].update(value="")
            except IndexError:
                sg.popup("Please Select the Item", font=("Helvetica", 12), modal=True)
        case sg.WIN_CLOSED:
            break
        case 'Exit':
            break


window.close()

