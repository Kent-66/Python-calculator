import tkinter

window = tkinter.Tk()
window.title("電卓")

#表示画面
display = tkinter.Entry(window)
display.grid(row = 0, column = 0, columnspan = 5)

#最初の数字を保存する変数
first_number = 0

#計算方法を保存する変数
operator = ""

#数字を表示する関数
def click(number):
    #「エラー」と表示されたらリセットする
    if display.get() == "エラー":
        display.delete(0, tkinter.END)
    #小数点が2個入らないようにする
    if number == "." and "." in display.get():
        return
    
    display.insert(tkinter.END, number)

#演算子を選ぶ関数
def select_operator(symbol):
    global first_number
    global operator

    first_number = float(display.get())
    operator = symbol

    display.delete(0, tkinter.END)

#＝ボタンで計算する関数
def equal():
    global first_number
    global operator

    second_number = float(display.get())

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            display.delete(0, tkinter.END)
            display.insert(tkinter.END, "エラー")

            first_number = 0
            operator = ""
            return
        else:
            result = first_number / second_number

    display.delete(0, tkinter.END)
    display.insert(tkinter.END, result)

#クリア機能
def clear():
    global first_number
    global operator

    first_number = 0
    operator = ""

    display.delete(0, tkinter.END)

#数字ボタン
numbers = [
    "7","8","9",
    "4","5","6",
    "1","2","3",
    "0"
]

for i, number in enumerate(numbers):

    button = tkinter.Button(
        window,
        text = number,
        command = lambda n = number: click(n)
    )

    row = i // 3 + 1
    column = i % 3

    button.grid(row = row, column = column)

#演算ボタン
operators = ["+","-","*","/"]

for i, symbol in enumerate(operators):

    button = tkinter.Button(
        window,
        text = symbol,
        command = lambda s = symbol: select_operator(s)
    )

    button.grid(row = 1 + i, column = 3)

#equalボタン
equal_button = tkinter.Button(
    window,
    text = "=",
    command = equal
)
equal_button.grid(row = 4, column = 2)

#小数点ボタン
dot_button = tkinter.Button(
    window,
    text = ".",
    command = lambda: click(".")
)
dot_button.grid(row = 4, column = 1)

#clearボタン
clear_button = tkinter.Button(
    window,
    text = "AC",
    command = clear
)
clear_button.grid(row = 1, column = 4)


#ウィンドウを表示し続ける
window.mainloop()
