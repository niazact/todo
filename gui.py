import PySimpleGUI as sg

label1 = sg.Text("Type in the To-Do")

input_box1 = sg.InputText(tooltip="Enter Todo")
add_button = sg.Button("Add")

window = sg.Window('To Do List', layout=[[label1],[input_box1,add_button]])
window.read()
window.close()

