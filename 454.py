import tkinter as tk
from tkinter import messagebox

# Функции для окна регистрации
def close_window():
    root.destroy()

def close_and_redirect():
    root.destroy()
    # Добавьте здесь код для перехода на другую страницу

# Создание окна регистрации
def open_registration_window():
    registration_window = tk.Toplevel()
    registration_window.title("Окно регистрации")

    tk.Label(registration_window, text="Имя:").pack()
    name_entry = tk.Entry(registration_window)
    name_entry.pack()

    tk.Label(registration_window, text="Email:").pack()
    email_entry = tk.Entry(registration_window)
    email_entry.pack()

    tk.Label(registration_window, text="Пароль:").pack()
    password_entry = tk.Entry(registration_window, show="")
    password_entry.pack()

    close_button = tk.Button(registration_window, text="Закрыть окно", command=close_window)
    close_button.pack()

    redirect_button = tk.Button(registration_window, text="На главную", command=close_and_redirect)
    redirect_button.pack()

# Создание главного окна
root = tk.Tk()
root.title("Пример простого сайта")

# Элементы веб-страницы
title_label = tk.Label(root, text="Добро пожаловать на сайт")
title_label.pack()

# Кнопка для открытия окна регистрации
register_button = tk.Button(root, text="Регистрация", command=open_registration_window)
register_button.pack()

root.mainloop()
def open_dogs_shelter_window():
    dogs_shelter_window = tk.Toplevel()
    dogs_shelter_window.title("Приют для собак")

    dogs_list_label = tk.Label(dogs_shelter_window, text="Список собак в приюте")
    dogs_list_label.pack()

    # Здесь можно добавить список зарегистрированных собак

    close_button = tk.Button(dogs_shelter_window, text="Закрыть окно", command=close_window)
    close_button.pack()
# Создание главного окна
root = tk.Tk()
root.title("Приют для собак")

# Элементы веб-страницы
title_label = tk.Label(root, text="Добро пожаловать в приют для собак")
title_label.pack()

# Кнопка для открытия окна регистрации
register_button = tk.Button(root, text="Регистрация", command=open_registration_window)
register_button.pack()

# Кнопка для открытия окна приюта для собак
dogs_shelter_button = tk.Button(root, text="Приют для собак", command=open_dogs_shelter_window)
dogs_shelter_button.pack()

root.mainloop()
# В начале программы, перед созданием главного окна, загрузите изображения собак
dog_image1 = tk.PhotoImage(file="собака.jpeg")
dog_image2 = tk.PhotoImage(file="собака2.jpg")

# Затем обновите функцию open_dogs_shelter_window() следующим образом:
def open_dogs_shelter_window():
    dogs_shelter_window = tk.Toplevel()
    dogs_shelter_window.title("Приют для собак")

    dogs_list_label = tk.Label(dogs_shelter_window, text="Список собак в приюте")
    dogs_list_label.pack()

    # Добавьте изображения собак на страницу
    dog_label1 = tk.Label(dogs_shelter_window, image=dog_image1)
    dog_label1.pack()

    dog_label2 = tk.Label(dogs_shelter_window, image=dog_image2)
    dog_label2.pack()

    close_button = tk.Button(dogs_shelter_window, text="Закрыть окно", command=close_window)
    close_button.pack()
