import tkinter
from tkinter import ttk

# App Window

root = tkinter.Tk()
root.title('Simple Calculator')
#root.geometry('800x600')

expression = ''

# Result Box

label_result = tkinter.Label(root, text = '')
label_result.grid(row = 0, column = 0, columnspan = 4)


# Button Functions

def add(value):
    global expression
    
    if value == '/':
        value = ' / '
    elif value == '*':
        value = ' * '
    elif value == '-':
        value = ' - '
    elif value == '+':
        value = ' + '
    
    expression += value
    label_result.config(text = expression)
    print(expression)

def clear():
    global expression
    expression = ''
    label_result.config(text = expression)

def calculate():
    global expression
    if expression == '':
        pass
    else:
        try:
            result = eval(expression)
            expression = str(result)
            label_result.config(text = result)
            print(result)
        except:
            result = 'error'
            expression = ''
    label_result.config(text = result)
# Calculator Number Buttons

button_decimal = ttk.Button(root, text = '.', command = lambda: add('.'))
button_decimal.grid(row = 4, column = 2)

button_0 = ttk.Button(root, text = '0', command = lambda: add('0'))
button_0.grid(row = 4, column = 1)

button_1 = ttk.Button(root, text = '1', command = lambda: add('1'))
button_1.grid(row = 3, column = 0)

button_2 = ttk.Button(root, text = '2', command = lambda: add('2'))
button_2.grid(row = 3, column = 1)

button_3 = ttk.Button(root, text = '3', command = lambda: add('3'))
button_3.grid(row = 3, column = 2)

button_4 = ttk.Button(root, text = '4', command = lambda: add('4'))
button_4.grid(row = 2, column = 0)

button_5 = ttk.Button(root, text = '5', command = lambda: add('5'))
button_5.grid(row = 2, column = 1)

button_6 = ttk.Button(root, text = '6', command = lambda: add('6'))
button_6.grid(row = 2, column = 2)

button_7 = ttk.Button(root, text = '7', command = lambda: add('7'))
button_7.grid(row = 1, column = 0)

button_8 = ttk.Button(root, text = '8', command = lambda: add('8'))
button_8.grid(row = 1, column = 1)

button_9 = ttk.Button(root, text = '9', command = lambda: add('9'))
button_9.grid(row = 1, column = 2)

# Calculator Operator Buttons

button_divide = ttk.Button(root, text = '/', command = lambda: add('/'))
button_divide.grid(row = 1, column = 3)

button_multiply = ttk.Button(root, text = '*', command = lambda: add('*'))
button_multiply.grid(row = 2, column = 3)

button_subtract = ttk.Button(root, text = '-', command = lambda: add('-'))
button_subtract.grid(row = 3, column = 3)

button_add = ttk.Button(root, text = '+', command = lambda: add('+'))
button_add.grid(row = 4, column = 3)

button_equal = ttk.Button(root, text = '=', command = lambda: calculate())
button_equal.grid(row = 5, column = 3)

button_clear = ttk.Button(root, text = 'C', command = lambda: clear())
button_clear.grid(row = 4, column = 0)

root.mainloop()