import hashlib
user_list = []
def add_user():
    print("Добавление нового пользователя:")
    user = {}
    user['Name'] = input("Имя: ")
    user['Surname'] = input("Фамилия: ")
    user['Age'] = input("Возраст: ")
    user['Address'] = input("Адрес: ")
    while True:
        email = input("Почта: ")
        if not any(u['Username'] == email for u in user_list):
            user['Username'] = email
            break
    else:
        print("Пользователь с такой почтой уже существует. Пож-та, введите уникальную почту.")
    while True:
        password = input("Пароль (минимум 8 символов): ")
        if len(password) >= 8:
            user['Password'] = hashlib.sha256(password.encode()) .hexdigest()
            break
        else:
            print("Пароль должен содержать 8 символов.")
    user_list.append(user)
    print("Пользователь успешно добавлен!")
def display_users():
    print("\nСписок пользователей:")
    for index, user in enumerate(user_list, 1):
        print(f"{index}. {user['Name']} {user['Surname']} ({user['Username']})")
def delete_user():
    display_users()
    if user_list:
        try:
            index = int(input("Введите номер пользователя для удаления: ")) - 1
            deleted_user = user_list.pop(index)
            print(f"Пользователь {deleted_user['Name']} {deleted_user['Surname']} удален.")
        except (ValueError,1 IndexError):
            print("Некорректный ввод.")
    else:
        print("Список пользователей пуст.")
while True:
    print("\nМеню:")
    print("1. Добавить нового пользователя")
    print("2. Посмотреть список пользователей")
    print("3. Удалить пользователя")
    print("4. Выйти")

    choice = input("Выберите действие (1-4):")
    if choice == "1":
        add_user()
    elif choice == "2":
        display_users()
    elif choice == "3":
        delete_user()
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Некорректный ввод. Пожадуйста, выберите от 1 до 4")
