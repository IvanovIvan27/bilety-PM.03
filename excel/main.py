import tkinter as tk
from tkinter import messagebox
import pandas as pd


# Шаблон сделан на первом билете

# Выводит все значения из файла во всплывающем окне
def print_file():
    with open('records.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        messagebox.showinfo('File Content', data)


# Создает новый .xlsx файл и добавляет в него все записи из records.txt, в которых номер зачетки равен введенному в
# текстовое поле
def show_in_excel(student_id):
    df = pd.read_csv('records.txt', delimiter=', ', engine='python')
    filtered_df = df[df['Номер зачетки'] == int(student_id)]
    if len(filtered_df) == 0:
        messagebox.showinfo('Записи не найдены', f'Нет студентов с номером зачетки: {student_id}')
    else:
        excel_filename = 'records_{}.xlsx'.format(student_id)
        filtered_df.to_excel(excel_filename, index=False)
        messagebox.showinfo('Успех', 'Excel файл с подходящими записями создан')


# Добавляет новую запись в records.txt

def add_record(date, student_id, full_name, group, discipline, grade):
    with open('records.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{date}, {student_id}, {full_name}, {group}, {discipline}, {grade}')
        messagebox.showinfo('Успех', 'Запись успешно добавлена')


def main():
    root = tk.Tk()
    root.title('Ведомость сдачи дисциплин')

    tk.Label(root, text='Дата:').grid(row=0, column=0)
    date_entry = tk.Entry(root)
    date_entry.grid(row=0, column=1)

    tk.Label(root, text='Номер зачетки:').grid(row=1, column=0)
    student_id_entry = tk.Entry(root)
    student_id_entry.grid(row=1, column=1)

    tk.Label(root, text='ФИО:').grid(row=2, column=0)
    full_name_entry = tk.Entry(root)
    full_name_entry.grid(row=2, column=1)

    tk.Label(root, text='Группа:').grid(row=3, column=0)
    group_entry = tk.Entry(root)
    group_entry.grid(row=3, column=1)

    tk.Label(root, text='Дисциплина:').grid(row=4, column=0)
    discipline_entry = tk.Entry(root)
    discipline_entry.grid(row=4, column=1)

    tk.Label(root, text='Оценка:').grid(row=5, column=0)
    grade_entry = tk.Entry(root)
    grade_entry.grid(row=5, column=1)

    print_button = tk.Button(root, text='Вывести записи из файла', command=print_file)
    print_button.grid(row=6, column=0, columnspan=2, pady=10)

    show_button = tk.Button(root, text='Показать в Excel', command=lambda: show_in_excel(student_id_entry.get()))
    show_button.grid(row=7, column=0, columnspan=2, pady=10)

    add_button = tk.Button(root, text='Добавить запись', command=lambda: add_record(
        date_entry.get(), student_id_entry.get(), full_name_entry.get(),
        group_entry.get(), discipline_entry.get(), grade_entry.get()))
    add_button.grid(row=8, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == '__main__':
    main()
