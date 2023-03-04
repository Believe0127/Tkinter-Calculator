import tkinter as tk
from tkinter import filedialog
import os

app = tk.Tk()
app.title("計算ソフト")
app.geometry("300x230")

def menu_destroy():
    app.destroy()

menubar = tk.Menu(app)
# File Menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='終了', command=menu_destroy)

menubar.add_cascade(label='ファイル', menu=filemenu)
app.config(menu=menubar)

def Calculation_plus():
    value1 = int(keisann1.get())
    value2 = int(keisann2.get())
    answer = value1 + value2
    answer_ent.delete(0, tk.END)
    answer_ent.insert(0, answer)

def Calculation_minus():
    value3 = int(keisann1.get())
    value4 = int(keisann2.get())
    answer = value3 - value4
    answer_ent.delete(0, tk.END)
    answer_ent.insert(0, answer)

def Caluclation_multiplication():
    value5 = int(keisann1.get())
    value6 = int(keisann2.get())
    answer = value5 * value6
    answer_ent.delete(0, tk.END)
    answer_ent.insert(0, answer)

def Calculation_divide():
    value7 = int(keisann1.get())
    value8 = int(keisann2.get())
    answer = value7 / value8
    answer_ent.delete(0, tk.END)
    answer_ent.insert(0, answer)

def clear_cmd():
    keisann1.delete(0, tk.END)
    keisann2.delete(0, tk.END)

answer_write = tk.Label(text="答え:", font=("bold", 20))
answer_write.pack()
answer_write.place(x=110, y=82)

keisann1 = tk.Entry(width=10, font=10)
keisann1.pack()
keisann1.place(x=32, y=45)

keisann2 = tk.Entry(width=10, font=10)
keisann2.pack()
keisann2.place(x=170, y=45)

One_label = tk.Label(text="数値1")
One_label.pack()
One_label.place(x=55, y=20)

Two_label = tk.Label(text="数値2")
Two_label.pack()
Two_label.place(x=195, y=20)

answer_btn_plus = tk.Button(text="足し算", width=8, command=Calculation_plus)
answer_btn_plus.pack()
answer_btn_plus.place(x=45, y=86)

answer_btn_minus = tk.Button(text="引き算", width=8, command=Calculation_minus)
answer_btn_minus.pack()
answer_btn_minus.place(x=45, y=116)

answer_btn_multiplication = tk.Button(text="かけ算", width=8, command=Caluclation_multiplication)
answer_btn_multiplication.pack()
answer_btn_multiplication.place(x=45, y=146)

answer_btn_divide = tk.Button(text="割り算", width=8, command=Calculation_divide)
answer_btn_divide.pack()
answer_btn_divide.place(x=45, y=176)

clear_btn = tk.Button(text="入力した文字を削除", width=15, command=clear_cmd)
clear_btn.pack()
clear_btn.place(x=155, y=116)

answer_ent = tk.Entry(width=8, font=20)
answer_ent.pack()
answer_ent.place(x=175, y=87)

# Windowを表示させる
app.mainloop()