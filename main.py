todos =[]

while True:
    user_action = input("Enter Add Or Show Or Exit: ")
    user_action = user_action.strip().lower()
    match user_action:
        case 'add':
            todo=input("Entere todo to Add :")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case whatever:
            break

print('bye..')
