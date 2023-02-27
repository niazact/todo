import PySimpleGUI as sg
import functions
label1 = sg.Text("Type in the To-Do")
input_box1 = sg.InputText(tooltip="Enter Todo",
                          key="todo")
add_button = sg.Button("Add")
exit_button = sg.Button('Exit')
listbox = sg.Listbox(values=functions.get_todos(),
                     key="todos",
                     enable_events=True,
                     size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")


window = sg.Window('To Do List', layout=[[label1],
                    [input_box1,add_button],
                    [listbox,edit_button, complete_button],
                    [exit_button]],
                   font=('Helvetica', 12))
while True:
    event, values=window.read()
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
            local_todos = functions.get_todos()
            new_todo = values['todo']
            edit_todo = values['todos'][0]
            if new_todo != edit_todo :
                index=local_todos.index(edit_todo)
                local_todos[index]=new_todo + '\n'
                functions.write_todos(local_todos)
                window['todos'].update(values=local_todos)
        case "Complete":
            local_todos = functions.get_todos()
            delete_todo = values['todos'][0]
            if delete_todo != " ":
                local_todos.remove(delete_todo)
                functions.write_todos(local_todos)
                window['todos'].update(values=local_todos)
                window['todo'].update(value="")
        case sg.WIN_CLOSED:
            break
        case 'Exit':
            break


window.close()

