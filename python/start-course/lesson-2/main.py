""" Приложение Task Manager
    version 0.0.1
    создает  i/o функционал для ввода заметки
"""
collection = ["создать версию 1", "попить кофе"]
print("Приветствуем вас в приложении  TASK MANAGER")

while(True):
    print("1 - добавить задачу | 2 - просмотреть все задачи | 3 - выход из приложения")
    choice_user = input("Выберите действие: ")

    match choice_user:
        case"1":
            task = input("Дайте название задаче: ")
            collection.append(task)
        case"2":
            print(collection)
        case "3":
            print("Досвидания!")
            break
        case _:
            print("Такого пункта нет в меню!")