from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *

number2 = ''
number1 = ''
newnumber1 = ''
xuanze = 0
language = 0

label1_more = Label()
label2_more = Label()
label3_more = Label()
button_more = Button()
button1_more = Button()
button2_more = Button()
button3_more = Button()
button4_more = Button()
entry_more = Entry()
entry1_more = Entry()

label_more1 = Label()
label1_more1 = Label()
label2_more1 = Label()
button_more1 = Button()
button2_more1 = Button()
button3_more1 = Button()
button4_more1 = Button()
button5_more1 = Button()
button6_more1 = Button()
entry_more1 = Entry()
entry1_more1 = Entry()

label_more2 = Label()
button_more2_add0 = Button()
button_more2_add1 = Button()
button_more2_add2 = Button()
button_more2_add3 = Button()
button_more2_add4 = Button()
button_more2_add5 = Button()
button_more2_add6 = Button()
button_more2_add7 = Button()
button_more2_add8 = Button()
button_more2_add9 = Button()
button_more2_adddian = Button()
button_more2_add = Button()
button_more2_subtract = Button()
button_more2_multiply = Button()
button_more2_except = Button()
button_more2_means = Button()
button_more2_reset = Button()
button_more2_negative_number = Button()
button_more2_exit = Button()
button_more2_back = Button()
text_more2 = Text()

label_choose_language = Label()
radiobutton_choose_language_1 = Radiobutton()
radiobutton_choose_language_2 = Radiobutton()
button_choose_language = Button()

text1 = Text()
button_about_reset = Button()

win = Tk
t = Tk
Calculator_point_and_click_window = Tk
language_window = Tk
colour_chooser_tk = Tk
about_tkinter = Tk


class Calculator(object):
    def Calculator_other_operations(self):
        global label1_more
        global label2_more
        global label3_more
        global button_more
        global button1_more
        global button2_more
        global button3_more
        global button4_more
        global entry_more
        global entry1_more
        global win
        global language
        win = Tk()

        def ci():
            try:
                num = float(entry_more.get()) ** float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def yu():
            try:
                num = float(entry_more.get()) % float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def zheng():
            try:
                num = float(entry_more.get()) // float(entry1_more.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def tuichu():
            global language
            if language == 0:
                b = '是否退出？'
                a = askquestion("question", '%s' % b)
                if a == 'yes':
                    win.destroy()
                else:
                    pass
            elif language == 1:
                b = 'Do you want to quit?'
                a = askquestion("error", '%s' % b)
                if a == 'yes':
                    win.destroy()
                else:
                    pass

        if language == 0:
            win.geometry('500x500')
            win.title("计算器")
            win.iconbitmap(default="./calculator-icon_34473.ico")

            label1_more = Label(win, text='计算器附属窗口')
            label1_more.pack()

            label2_more = Label(win, text="数字一")
            label2_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label3_more = Label(win, text="数字二")
            label3_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            button_more = Button(win, text="次方", command=ci)
            button_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button1_more = Button(win, text="取余", command=yu)
            button1_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button2_more = Button(win, text="取整", command=zheng)
            button2_more.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button3_more = Button(win, text="退出", command=tuichu)
            button3_more.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            button4_more = Button(win, text="更多", command=self.Calculator_four_operations)
            button4_more.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            entry_more = Entry(win)
            entry_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more = Entry(win)
            entry1_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        elif language == 1:
            win.geometry('500x500')
            win.title("calculator")
            win.iconbitmap(default="./calculator-icon_34473.ico")

            label1_more = Label(win, text='Calculator attachment Calculator_point_and_click_window')
            label1_more.pack()

            label2_more = Label(win, text="number1")
            label2_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label3_more = Label(win, text="number2")
            label3_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            button_more = Button(win, text="to the power", command=ci)
            button_more.place(relheight=0.1, rely=0.8, relx=0.1)

            button1_more = Button(win, text="Take the balance", command=yu)
            button1_more.place(relheight=0.1, rely=0.8, relx=0.4)

            button2_more = Button(win, text="Rounding", command=zheng)
            button2_more.place(relheight=0.1, rely=0.8, relx=0.7)

            button3_more = Button(win, text="exit", command=tuichu)
            button3_more.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            button4_more = Button(win, text="more", command=self.Calculator_four_operations)
            button4_more.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            entry_more = Entry(win)
            entry_more.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more = Entry(win)
            entry1_more.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        win.mainloop()

    def Calculator_four_operations(self):
        global label_more1
        global label1_more1
        global label2_more1
        global button_more1
        global button2_more1
        global button3_more1
        global button4_more1
        global button5_more1
        global button6_more1
        global entry_more1
        global entry1_more1
        global t
        global language
        t = Tk()

        def jia():
            try:
                num = float(entry_more1.get()) + float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def jian():
            global language
            try:
                num = float(entry_more1.get()) - float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)
            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def cheng():
            try:
                num = float(entry_more1.get()) * float(entry1_more1.get())
            except:
                if language == 0:
                    a = "请输入数字/输入的字符违法"
                    showerror("error", '%s' % a)
                elif language == 1:
                    a = "Please enter numbers/entered characters illegally"
                    showerror("error", '%s' % a)

            else:
                if language == 0:
                    showinfo("得数是", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)
                elif language == 1:
                    showinfo("The number is", '%f' % num)
                    entry_more1.delete(0, END)
                    entry1_more1.delete(0, END)

        def chu():
            global language
            while 1:
                try:
                    num = float(entry_more1.get()) / float(entry1_more1.get())
                    if float(entry1_more1.get()) == 0:
                        if language == 0:
                            a = "输入的数字不能为零"
                            showerror("error", '%s' % a)
                            entry1_more1.delete(0, END)
                            break
                        elif language == 1:
                            a = "The number entered cannot be zero"
                            showerror("error", '%s' % a)
                            entry1_more1.delete(0, END)
                            break
                except:
                    if language == 0:
                        a = "输入的数字格式不正确,请重新输入"
                        showerror("error", '%s' % a)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                    elif language == 1:
                        a = "The number entered is not in the correct format, please reenter it"
                        showerror("error", '%s' % a)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                else:
                    if language == 0:
                        showinfo("得数是", '%f' % num)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break
                    elif language == 1:
                        showinfo("The number is", '%f' % num)
                        entry_more1.delete(0, END)
                        entry1_more1.delete(0, END)
                        break

        def tuichu():
            global language
            if language == 0:
                b = '是否退出？'
                a = askquestion("question", '%s' % b)
                if a == 'yes':
                    t.destroy()
                else:
                    pass
            elif language == 1:
                b = 'Do you want to quit?'
                a = askquestion("error", '%s' % b)
                if a == 'yes':
                    t.destroy()
                else:
                    pass

        if language == 0:
            t.geometry('500x500')
            t.title("计算器")
            t.iconbitmap(default="./calculator-icon_34473.ico")

            label_more1 = Label(t, text="数字一")
            label_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label1_more1 = Label(t, text="数字二")
            label1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            label2_more1 = Label(t, text="计算器")
            label2_more1.pack()

            button_more1 = Button(t, text="+", command=jia)
            button_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button2_more1 = Button(t, text="-", command=jian)
            button2_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button3_more1 = Button(t, text="×", command=cheng)
            button3_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button4_more1 = Button(t, text='÷', command=chu)
            button4_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

            button5_more1 = Button(t, text="更多", command=self.Calculator_other_operations)
            button5_more1.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            button6_more1 = Button(t, text="退出", command=tuichu)
            button6_more1.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            entry_more1 = Entry(t)
            entry_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more1 = Entry(t)
            entry1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)
        elif language == 1:
            t.geometry('500x500')
            t.title("calculator")
            t.iconbitmap(default="./calculator-icon_34473.ico")

            label_more1 = Label(t, text="number1")
            label_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.1)

            label1_more1 = Label(t, text="number2")
            label1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.1)

            label2_more1 = Label(t, text="calculator")
            label2_more1.pack()

            button_more1 = Button(t, text="+", command=jia)
            button_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.1)

            button2_more1 = Button(t, text="-", command=jian)
            button2_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.3)

            button3_more1 = Button(t, text="×", command=cheng)
            button3_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.5)

            button4_more1 = Button(t, text='÷', command=chu)
            button4_more1.place(relheight=0.1, relwidth=0.1, rely=0.8, relx=0.7)

            button5_more1 = Button(t, text="more", command=self.Calculator_other_operations)
            button5_more1.place(relheight=0.1, relwidth=0.1, rely=0.3, relx=0.9)

            button6_more1 = Button(t, text="exit", command=tuichu)
            button6_more1.place(relheight=0.1, relwidth=0.1, rely=0.6, relx=0.9)

            entry_more1 = Entry(t)
            entry_more1.place(relheight=0.1, relwidth=0.3, rely=0.3, relx=0.5)

            entry1_more1 = Entry(t)
            entry1_more1.place(relheight=0.1, relwidth=0.3, rely=0.6, relx=0.5)

        t.mainloop()

    def Calculator_point_and_click(self):
        global label_more2
        global button_more2_add0
        global button_more2_add1
        global button_more2_add2
        global button_more2_add3
        global button_more2_add4
        global button_more2_add5
        global button_more2_add6
        global button_more2_add7
        global button_more2_add8
        global button_more2_add9
        global button_more2_adddian
        global button_more2_add
        global button_more2_subtract
        global button_more2_multiply
        global button_more2_except
        global button_more2_means
        global button_more2_reset
        global button_more2_negative_number
        global button_more2_exit
        global button_more2_back
        global text_more2
        global Calculator_point_and_click_window
        global language
        window = Tk()

        # ----------------------------------------------------------------------------------------------------------------------------

        class Add(object):

            def add0(self):
                global number1
                a1 = '0'
                text_more2.insert(END, a1)
                number1 += a1

            def add1(self):
                global number1
                a1 = '1'
                text_more2.insert(END, a1)
                number1 += a1

            def add2(self):
                global number1
                a1 = '2'
                text_more2.insert(END, a1)
                number1 += a1

            def add3(self):
                global number1
                a1 = '3'
                text_more2.insert(END, a1)
                number1 += a1

            def add4(self):
                global number1
                a1 = '4'
                text_more2.insert(END, a1)
                number1 += a1

            def add5(self):
                global number1
                a1 = '5'
                text_more2.insert(END, a1)
                number1 += a1

            def add6(self):
                global number1
                a1 = '6'
                text_more2.insert(END, a1)
                number1 += a1

            def add7(self):
                global number1
                a1 = '7'
                text_more2.insert(END, a1)
                number1 += a1

            def add8(self):
                global number1
                a1 = '8'
                text_more2.insert(END, a1)
                number1 += a1

            def add9(self):
                global number1
                a1 = '9'
                text_more2.insert(END, a1)
                number1 += a1

            def adddian(self):
                global number1
                a1 = '.'
                text_more2.insert(END, a1)
                number1 += a1

        # ----------------------------------------------------------------------------------------------------------------------------

        class Yunsuanfuhao(object):

            def add(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '+'
                text_more2.insert(END, string)
                number1 += string

            def jian(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '-'
                text_more2.insert(END, string)
                number1 += string

            def cheng(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '*'
                string1 = '×'
                text_more2.insert(END, string1)
                number1 += string

            def chu(self):
                global number1
                global newnumber1
                newnumber1 = number1
                string = '/'
                string1 = '÷'
                text_more2.insert(END, string1)
                number1 += string

        # ----------------------------------------------------------------------------------------------------------------------------

        def dengyu():
            global number2
            global number1
            global xuanze
            global language
            try:
                global number2
                global number1
                global newnumber1
                number2 = eval(number1)
                string = '='
                text_more2.insert(END, string)
                text_more2.insert(END, number2)
            except (ValueError, ZeroDivisionError, SyntaxError) as e:
                if language == 0:
                    a1 = '请输入（点击）正确的数'
                    showerror(e, '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)
                elif language == 1:
                    a1 = 'Please enter (click) the correct number'
                    showerror(e, '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)

        def ac():
            global number2
            global number1
            global xuanze
            number2 = ''
            number1 = ''
            xuanze = 0
            text_more2.delete(1.0, END)

        def zhengfushu():
            global number1
            global number2
            text_more2.insert(END, '-')
            number1 += '-'

        def back():
            global language
            try:
                global number1
                global number2
                global xuanze
                number1 = int(number1) // 10
                text_more2.delete(1.0, END)
                text_more2.insert(END, str(number1))
            except ValueError as e:
                if language == 0:
                    a1 = '请输入（点击）正确的数'
                    showerror(str(e), '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)
                elif language == 1:
                    a1 = 'Please enter (click) the correct number'
                    showerror(str(e), '%s' % a1)
                    number2 = ''
                    number1 = ''
                    xuanze = 0
                    text_more2.delete(1.0, END)

        def tuichu():
            global language
            if language == 0:
                b2 = '是否退出？'
                a1 = askquestion('questions', '%s' % b2)
                if a1 == 'yes':
                    window.destroy()
                else:
                    pass
            elif language == 1:
                b2 = 'Do you want to quit?'
                a1 = askquestion('questions', '%s' % b2)
                if a1 == 'yes':
                    window.destroy()
                else:
                    pass

        # ----------------------------------------------------------------------------------------------------------------------------

        addnumber = Add()
        addyunsuanfuhao = Yunsuanfuhao()

        if language == 0:
            window.geometry('500x500')
            window.title('计算器')
            window.iconbitmap(default="./calculator-icon_34473.ico")

            label_more2 = Label(window, text='计算器')
            label_more2.pack()

            button_more2_add0 = Button(window, text='0', command=addnumber.add0)
            button_more2_add0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.3)

            button_more2_add1 = Button(window, text='1', command=addnumber.add1)
            button_more2_add1.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.1)

            button_more2_add2 = Button(window, text='2', command=addnumber.add2)
            button_more2_add2.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.3)

            button_more2_add3 = Button(window, text='3', command=addnumber.add3)
            button_more2_add3.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.5)

            button_more2_add4 = Button(window, text='4', command=addnumber.add4)
            button_more2_add4.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.1)

            button_more2_add5 = Button(window, text='5', command=addnumber.add5)
            button_more2_add5.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.3)

            button_more2_add6 = Button(window, text='6', command=addnumber.add6)
            button_more2_add6.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.5)

            button_more2_add7 = Button(window, text='7', command=addnumber.add7)
            button_more2_add7.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.1)

            button_more2_add8 = Button(window, text='8', command=addnumber.add8)
            button_more2_add8.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.3)

            button_more2_add9 = Button(window, text='9', command=addnumber.add9)
            button_more2_add9.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.5)

            button_more2_adddian = Button(window, text='.', command=addnumber.adddian)
            button_more2_adddian.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.1)

            button_more2_add = Button(window, text='+', command=addyunsuanfuhao.add)
            button_more2_add.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.8)

            button_more2_subtract = Button(window, text='-', command=addyunsuanfuhao.jian)
            button_more2_subtract.place(relheight=0.1, relwidth=0.2, rely=0.5, relx=0.8)

            button_more2_multiply = Button(window, text='×', command=addyunsuanfuhao.cheng)
            button_more2_multiply.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.8)

            button_more2_except = Button(window, text='÷', command=addyunsuanfuhao.chu)
            button_more2_except.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.8)

            button_more2_means = Button(window, text='=', command=dengyu)
            button_more2_means.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.8)

            button_more2_reset = Button(window, text='AC', command=ac)
            button_more2_reset.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.8)

            button_more2_negative_number = Button(window, text='-/+（负）', command=zhengfushu)
            button_more2_negative_number.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.6)

            button_more2_exit = Button(window, text='退出', command=tuichu)
            button_more2_exit.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

            button_more2_back = Button(window, text='<--', command=back)
            button_more2_back.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.4)

            text_more2 = Text(window)
            text_more2.place(rely=0.05, relheight=0.3, relwidth=1)
        elif language == 1:
            window.geometry('500x500')
            window.title('calculator')
            window.iconbitmap(default="./calculator-icon_34473.ico")

            label_more2 = Label(window, text='calculator')
            label_more2.pack()

            button_more2_add0 = Button(window, text='0', command=addnumber.add0)
            button_more2_add0.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.3)

            button_more2_add1 = Button(window, text='1', command=addnumber.add1)
            button_more2_add1.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.1)

            button_more2_add2 = Button(window, text='2', command=addnumber.add2)
            button_more2_add2.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.3)

            button_more2_add3 = Button(window, text='3', command=addnumber.add3)
            button_more2_add3.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.5)

            button_more2_add4 = Button(window, text='4', command=addnumber.add4)
            button_more2_add4.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.1)

            button_more2_add5 = Button(window, text='5', command=addnumber.add5)
            button_more2_add5.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.3)

            button_more2_add6 = Button(window, text='6', command=addnumber.add6)
            button_more2_add6.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.5)

            button_more2_add7 = Button(window, text='7', command=addnumber.add7)
            button_more2_add7.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.1)

            button_more2_add8 = Button(window, text='8', command=addnumber.add8)
            button_more2_add8.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.3)

            button_more2_add9 = Button(window, text='9', command=addnumber.add9)
            button_more2_add9.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.5)

            button_more2_adddian = Button(window, text='.', command=addnumber.adddian)
            button_more2_adddian.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.1)

            button_more2_add = Button(window, text='+', command=addyunsuanfuhao.add)
            button_more2_add.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.8)

            button_more2_subtract = Button(window, text='-', command=addyunsuanfuhao.jian)
            button_more2_subtract.place(relheight=0.1, relwidth=0.2, rely=0.5, relx=0.8)

            button_more2_multiply = Button(window, text='×', command=addyunsuanfuhao.cheng)
            button_more2_multiply.place(relheight=0.1, relwidth=0.2, rely=0.6, relx=0.8)

            button_more2_except = Button(window, text='÷', command=addyunsuanfuhao.chu)
            button_more2_except.place(relheight=0.1, relwidth=0.2, rely=0.7, relx=0.8)

            button_more2_means = Button(window, text='=', command=dengyu)
            button_more2_means.place(relheight=0.1, relwidth=0.2, rely=0.8, relx=0.8)

            button_more2_reset = Button(window, text='AC', command=ac)
            button_more2_reset.place(relheight=0.1, relwidth=0.2, rely=0.9, relx=0.8)

            button_more2_back = Button(window, text='<--', command=back)
            button_more2_back.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.4)

            text_more2 = Text(window)
            text_more2.place(rely=0.05, relheight=0.3, relwidth=1)

            button_more2_negative_number = Button(window, text='-/+（negative）', command=zhengfushu)
            button_more2_negative_number.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.6)

            button_more2_exit = Button(window, text='exit', command=tuichu)
            button_more2_exit.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.2)

        window.mainloop()


def Calculator_main_interface():
    global language

    def about():
        global about_tkinter
        global text1
        global button_about_reset
        about_tkinter = Tk()

        about_tkinter.geometry('500x500')
        about_tkinter.title('关于界面(about interface)')
        about_tkinter.iconbitmap(default="./calculator-icon_34473.ico")

        text1 = Text(about_tkinter)
        text1.place(relheight=0.9, relwidth=1, rely=0)

        def reset():
            if language == 0:
                a11 = '制作：@QQ小井井\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井，已注明，已获得许可\ngithub:\nhttps://github.com' \
                     '/jingcygz/jingcygz\n（此网站为readme.md） '
                text1.delete(1.0, END)
                text1.insert(END, a11)
            elif language == 1:
                a22 = 'Production: @QQ Xiaojingjing\nWell If you need to move, please add QQ:771732203 (indicate the intention)\nOr change this to (first line):\nProduction: @QQ Xiaojing, indicated, licensed \ngithub:https://github.com/jingcygz/jingcygz\n(this site is readme.md) '
                text1.delete(1.0, END)
                text1.insert(END, a22)

        if language == 0:
            a1 = '制作：@QQ小井井\n如需搬运请加QQ：771732203（注明来意）\n或更改此为（第一行）：\n制作：@QQ小井井，已注明，已获得许可\ngithub:\nhttps://github.com' \
                     '/jingcygz/jingcygz\n（此网站为readme.md） '
            text1.insert(END, a1)

            button_about_reset = Button(about_tkinter, text='重置', command=reset)
            button_about_reset.place(rely=0.9)
        elif language == 1:
            a2 = 'Production: @QQ Xiaojingjing\nWell If you need to move, please add QQ:771732203 (indicate the intention)\nOr change this to (first line):\nProduction: @QQ Xiaojing, indicated, licensed \ngithub:https://github.com/jingcygz/jingcygz\n(this site is readme.md) '
            text1.insert(END, a2)

            button_about_reset = Button(about_tkinter, text='reset', command=reset)
            button_about_reset.place(rely=0.9)

    def language_switching():
        global language_window
        global label_choose_language
        global radiobutton_choose_language_1
        global radiobutton_choose_language_2
        global button_choose_language

        def choose_language():
            global language
            v = int(var.get())
            if v == 0:
                language = 0
                a1 = '设置成功！'
                showinfo('成功', '%s' % a1)
            elif v == 1:
                language = 1
                a1 = '設置成功'
                showinfo('info', '%s' % a1)
            elif v == 2:
                language = 1
                a1 = 'Setup successful'
                showinfo('info', '%s' % a1)


        language_window = Tk()
        language_window.geometry('750x250')
        language_window.title('语言选择界面(Language selection interface)')
        language_window.iconbitmap(default="./calculator-icon_34473.ico")

        var = IntVar()

        label_choose_language = Label(language_window, text='语言选择界面(Language selection interface)')
        label_choose_language.pack()

        label_1_choose_language = Label(language_window, text='改变语言时，请先点击单选框默认的语言，否则会设置不成功！\n(When changing the language, please click the default language in the radio box first, otherwise the setting will be unsuccessful!)')
        label_1_choose_language.pack()

        radiobutton_choose_language_1 = Radiobutton(language_window, text='中文（简体）', value=0, variable=var, command=choose_language)
        radiobutton_choose_language_1.place(relx=0.1, rely=0.3)

        radiobutton_choose_language_2 = Radiobutton(language_window, text='中文（繁體）', value=1, variable=var, command=choose_language)
        radiobutton_choose_language_2.place(relx=0.1, rely=0.4)

        radiobutton_choose_language_3 = Radiobutton(language_window, text='English', value=2, variable=var,command=choose_language)
        radiobutton_choose_language_3.place(relx=0.1, rely=0.5)

        language_window.mainloop()

    def colour_chooser():
        global colour_chooser_tk
        global label_more2
        global button_more2_add0
        global button_more2_add1
        global button_more2_add2
        global button_more2_add3
        global button_more2_add4
        global button_more2_add5
        global button_more2_add6
        global button_more2_add7
        global button_more2_add8
        global button_more2_add9
        global button_more2_adddian
        global button_more2_add
        global button_more2_subtract
        global button_more2_multiply
        global button_more2_except
        global button_more2_means
        global button_more2_reset
        global button_more2_negative_number
        global button_more2_exit
        global button_more2_back
        global text_more2

        global label_more1
        global label1_more1
        global label2_more1
        global button_more1
        global button2_more1
        global button3_more1
        global button4_more1
        global button5_more1
        global button6_more1
        global entry_more1
        global entry1_more1

        global label1_more
        global label2_more
        global label3_more
        global button_more
        global button1_more
        global button2_more
        global button3_more
        global button4_more
        global entry_more
        global entry1_more

        global language_window
        global label_choose_language
        global radiobutton_choose_language_1
        global radiobutton_choose_language_2
        global button_choose_language

        global about_tkinter
        global text1
        global button_about_reset

        global win
        global Calculator_point_and_click_window
        global t
        global language

        def changeColor():
            while 1:
                try:
                    if language == 0:
                        color = askcolor()
                        color1 = askcolor()
                        fg, bg = str(color[1]), str(color1[1])
                        if fg == bg:
                            a4 = '你确定要选择一样的颜色吗？'
                            choose4 = askquestion('question', '%s' % a4)
                            if choose4 == 'yes':
                                a = '用于计算器（点击式）？'
                                choose = askquestion('question', '%s' % a)
                                if choose == 'yes':
                                    label_more2.configure(fg=fg, bg=bg)
                                    button_more2_add0.configure(fg=fg, bg=bg)
                                    button_more2_add1.configure(fg=fg, bg=bg)
                                    button_more2_add2.configure(fg=fg, bg=bg)
                                    button_more2_add3.configure(fg=fg, bg=bg)
                                    button_more2_add4.configure(fg=fg, bg=bg)
                                    button_more2_add5.configure(fg=fg, bg=bg)
                                    button_more2_add6.configure(fg=fg, bg=bg)
                                    button_more2_add7.configure(fg=fg, bg=bg)
                                    button_more2_add8.configure(fg=fg, bg=bg)
                                    button_more2_add9.configure(fg=fg, bg=bg)
                                    button_more2_adddian.configure(fg=fg, bg=bg)
                                    button_more2_add.configure(fg=fg, bg=bg)
                                    button_more2_subtract.configure(fg=fg, bg=bg)
                                    button_more2_multiply.configure(fg=fg, bg=bg)
                                    button_more2_except.configure(fg=fg, bg=bg)
                                    button_more2_means.configure(fg=fg, bg=bg)
                                    button_more2_reset.configure(fg=fg, bg=bg)
                                    button_more2_negative_number.configure(fg=fg, bg=bg)
                                    button_more2_exit.configure(fg=fg, bg=bg)
                                    button_more2_back.configure(fg=fg, bg=bg)
                                    text_more2.configure(fg=fg, bg=bg)
                                    Calculator_point_and_click_window.configure(bg=bg)
                                    break
                                else:
                                    a1 = '用于计算器（输入式）？'
                                    choose1 = askquestion('question', '%s' % a1)
                                    if choose1 == 'yes':
                                        label_more1.configure(fg=fg, bg=bg)
                                        label1_more1.configure(fg=fg, bg=bg)
                                        label2_more1.configure(fg=fg, bg=bg)
                                        button_more1.configure(fg=fg, bg=bg)
                                        button2_more1.configure(fg=fg, bg=bg)
                                        button3_more1.configure(fg=fg, bg=bg)
                                        button4_more1.configure(fg=fg, bg=bg)
                                        button5_more1.configure(fg=fg, bg=bg)
                                        button6_more1.configure(fg=fg, bg=bg)
                                        entry_more1.configure(fg=fg, bg=bg)
                                        entry1_more1.configure(fg=fg, bg=bg)
                                        t.configure(bg=bg)

                                        label1_more.configure(fg=fg, bg=bg)
                                        label2_more.configure(fg=fg, bg=bg)
                                        label3_more.configure(fg=fg, bg=bg)
                                        button_more.configure(fg=fg, bg=bg)
                                        button1_more.configure(fg=fg, bg=bg)
                                        button2_more.configure(fg=fg, bg=bg)
                                        button3_more.configure(fg=fg, bg=bg)
                                        button4_more.configure(fg=fg, bg=bg)
                                        entry_more.configure(fg=fg, bg=bg)
                                        entry1_more.configure(fg=fg, bg=bg)
                                        win.configure(bg=bg)
                                        break
                                    else:
                                        a2 = '用于语言选择界面？'
                                        choose2 = askquestion('question', '%s' % a2)
                                        if choose2 == 'yes':
                                            language_window.configure(bg=bg)
                                            label_choose_language.configure(fg=fg, bg=bg)
                                            radiobutton_choose_language_1.configure(fg=fg, bg=bg)
                                            radiobutton_choose_language_2.configure(fg=fg, bg=bg)
                                            button_choose_language.configure(fg=fg, bg=bg)
                                            break
                                        else:
                                            a3 = '用于关于界面？'
                                            choose3 = askquestion('question', '%s' % a3)
                                            if choose3 == 'yes':
                                                about_tkinter.configure(bg=bg)
                                                text1.configure(fg=fg, bg=bg)
                                                button_about_reset.configure(fg=fg, bg=bg)
                                                break
                                            else:
                                                label_choose_colour.configure(fg=fg, bg=bg)
                                                color_choose_button.configure(fg=fg, bg=bg)
                                                colour_chooser_tk.configure(bg=bg)
                                                break
                            else:
                                break
                        elif fg != bg:
                            a = '用于计算器（点击式）？'
                            choose = askquestion('question', '%s' % a)
                            if choose == 'yes':
                                label_more2.configure(fg=fg, bg=bg)
                                button_more2_add0.configure(fg=fg, bg=bg)
                                button_more2_add1.configure(fg=fg, bg=bg)
                                button_more2_add2.configure(fg=fg, bg=bg)
                                button_more2_add3.configure(fg=fg, bg=bg)
                                button_more2_add4.configure(fg=fg, bg=bg)
                                button_more2_add5.configure(fg=fg, bg=bg)
                                button_more2_add6.configure(fg=fg, bg=bg)
                                button_more2_add7.configure(fg=fg, bg=bg)
                                button_more2_add8.configure(fg=fg, bg=bg)
                                button_more2_add9.configure(fg=fg, bg=bg)
                                button_more2_adddian.configure(fg=fg, bg=bg)
                                button_more2_add.configure(fg=fg, bg=bg)
                                button_more2_subtract.configure(fg=fg, bg=bg)
                                button_more2_multiply.configure(fg=fg, bg=bg)
                                button_more2_except.configure(fg=fg, bg=bg)
                                button_more2_means.configure(fg=fg, bg=bg)
                                button_more2_reset.configure(fg=fg, bg=bg)
                                button_more2_negative_number.configure(fg=fg, bg=bg)
                                button_more2_exit.configure(fg=fg, bg=bg)
                                button_more2_back.configure(fg=fg, bg=bg)
                                text_more2.configure(fg=fg, bg=bg)
                                Calculator_point_and_click_window.configure(bg=bg)
                                break
                            else:
                                a1 = '用于计算器（输入式）？'
                                choose1 = askquestion('question', '%s' % a1)
                                if choose1 == 'yes':
                                    label_more1.configure(fg=fg, bg=bg)
                                    label1_more1.configure(fg=fg, bg=bg)
                                    label2_more1.configure(fg=fg, bg=bg)
                                    button_more1.configure(fg=fg, bg=bg)
                                    button2_more1.configure(fg=fg, bg=bg)
                                    button3_more1.configure(fg=fg, bg=bg)
                                    button4_more1.configure(fg=fg, bg=bg)
                                    button5_more1.configure(fg=fg, bg=bg)
                                    button6_more1.configure(fg=fg, bg=bg)
                                    entry_more1.configure(fg=fg, bg=bg)
                                    entry1_more1.configure(fg=fg, bg=bg)
                                    t.configure(bg=bg)

                                    label1_more.configure(fg=fg, bg=bg)
                                    label2_more.configure(fg=fg, bg=bg)
                                    label3_more.configure(fg=fg, bg=bg)
                                    button_more.configure(fg=fg, bg=bg)
                                    button1_more.configure(fg=fg, bg=bg)
                                    button2_more.configure(fg=fg, bg=bg)
                                    button3_more.configure(fg=fg, bg=bg)
                                    button4_more.configure(fg=fg, bg=bg)
                                    entry_more.configure(fg=fg, bg=bg)
                                    entry1_more.configure(fg=fg, bg=bg)
                                    win.configure(bg=bg)
                                    break
                                else:
                                    a2 = '用于语言选择界面？'
                                    choose2 = askquestion('question', '%s' % a2)
                                    if choose2 == 'yes':
                                        language_window.configure(bg=bg)
                                        label_choose_language.configure(fg=fg, bg=bg)
                                        radiobutton_choose_language_1.configure(fg=fg, bg=bg)
                                        radiobutton_choose_language_2.configure(fg=fg, bg=bg)
                                        button_choose_language.configure(fg=fg, bg=bg)
                                        break
                                    else:
                                        a3 = '用于关于界面？'
                                        choose3 = askquestion('question', '%s' % a3)
                                        if choose3 == 'yes':
                                            about_tkinter.configure(bg=bg)
                                            text1.configure(fg=fg, bg=bg)
                                            button_about_reset.configure(fg=fg, bg=bg)
                                            break
                                        else:
                                            label_choose_colour.configure(fg=fg, bg=bg)
                                            color_choose_button.configure(fg=fg, bg=bg)
                                            colour_chooser_tk.configure(bg=bg)
                                            break
                    elif language == 1:
                        color = askcolor()
                        color1 = askcolor()
                        fg, bg = str(color[1]), str(color1[1])
                        if fg == bg:
                            a4 = 'Are you sure you want to choose the same color?？'
                            choose4 = askquestion('question', '%s' % a4)
                            if choose4 == 'yes':
                                a = 'For calculator (point-and-click)？'
                                choose = askquestion('question', '%s' % a)
                                if choose == 'yes':
                                    label_more2.configure(fg=fg, bg=bg)
                                    button_more2_add0.configure(fg=fg, bg=bg)
                                    button_more2_add1.configure(fg=fg, bg=bg)
                                    button_more2_add2.configure(fg=fg, bg=bg)
                                    button_more2_add3.configure(fg=fg, bg=bg)
                                    button_more2_add4.configure(fg=fg, bg=bg)
                                    button_more2_add5.configure(fg=fg, bg=bg)
                                    button_more2_add6.configure(fg=fg, bg=bg)
                                    button_more2_add7.configure(fg=fg, bg=bg)
                                    button_more2_add8.configure(fg=fg, bg=bg)
                                    button_more2_add9.configure(fg=fg, bg=bg)
                                    button_more2_adddian.configure(fg=fg, bg=bg)
                                    button_more2_add.configure(fg=fg, bg=bg)
                                    button_more2_subtract.configure(fg=fg, bg=bg)
                                    button_more2_multiply.configure(fg=fg, bg=bg)
                                    button_more2_except.configure(fg=fg, bg=bg)
                                    button_more2_means.configure(fg=fg, bg=bg)
                                    button_more2_reset.configure(fg=fg, bg=bg)
                                    button_more2_negative_number.configure(fg=fg, bg=bg)
                                    button_more2_exit.configure(fg=fg, bg=bg)
                                    button_more2_back.configure(fg=fg, bg=bg)
                                    text_more2.configure(fg=fg, bg=bg)
                                    Calculator_point_and_click_window.configure(bg=bg)
                                    break
                                else:
                                    a1 = 'For calculator (input type)？'
                                    choose1 = askquestion('question', '%s' % a1)
                                    if choose1 == 'yes':
                                        label_more1.configure(fg=fg, bg=bg)
                                        label1_more1.configure(fg=fg, bg=bg)
                                        label2_more1.configure(fg=fg, bg=bg)
                                        button_more1.configure(fg=fg, bg=bg)
                                        button2_more1.configure(fg=fg, bg=bg)
                                        button3_more1.configure(fg=fg, bg=bg)
                                        button4_more1.configure(fg=fg, bg=bg)
                                        button5_more1.configure(fg=fg, bg=bg)
                                        button6_more1.configure(fg=fg, bg=bg)
                                        entry_more1.configure(fg=fg, bg=bg)
                                        entry1_more1.configure(fg=fg, bg=bg)
                                        t.configure(bg=bg)

                                        label1_more.configure(fg=fg, bg=bg)
                                        label2_more.configure(fg=fg, bg=bg)
                                        label3_more.configure(fg=fg, bg=bg)
                                        button_more.configure(fg=fg, bg=bg)
                                        button1_more.configure(fg=fg, bg=bg)
                                        button2_more.configure(fg=fg, bg=bg)
                                        button3_more.configure(fg=fg, bg=bg)
                                        button4_more.configure(fg=fg, bg=bg)
                                        entry_more.configure(fg=fg, bg=bg)
                                        entry1_more.configure(fg=fg, bg=bg)
                                        win.configure(bg=bg)
                                        break
                                    else:
                                        a2 = 'Used for the language selection interface？'
                                        choose2 = askquestion('question', '%s' % a2)
                                        if choose2 == 'yes':
                                            language_window.configure(bg=bg)
                                            label_choose_language.configure(fg=fg, bg=bg)
                                            radiobutton_choose_language_1.configure(fg=fg, bg=bg)
                                            radiobutton_choose_language_2.configure(fg=fg, bg=bg)
                                            button_choose_language.configure(fg=fg, bg=bg)
                                            break
                                        else:
                                            a3 = 'Used for the About interface？'
                                            choose3 = askquestion('question', '%s' % a3)
                                            if choose3 == 'yes':
                                                about_tkinter.configure(bg=bg)
                                                text1.configure(fg=fg, bg=bg)
                                                button_about_reset.configure(fg=fg, bg=bg)
                                                break
                                            else:
                                                label_choose_colour.configure(fg=fg, bg=bg)
                                                color_choose_button.configure(fg=fg, bg=bg)
                                                colour_chooser_tk.configure(bg=bg)
                                                break
                            else:
                                break
                        elif fg != bg:
                            a = 'For calculator (point-and-click)？'
                            choose = askquestion('question', '%s' % a)
                            if choose == 'yes':
                                label_more2.configure(fg=fg, bg=bg)
                                button_more2_add0.configure(fg=fg, bg=bg)
                                button_more2_add1.configure(fg=fg, bg=bg)
                                button_more2_add2.configure(fg=fg, bg=bg)
                                button_more2_add3.configure(fg=fg, bg=bg)
                                button_more2_add4.configure(fg=fg, bg=bg)
                                button_more2_add5.configure(fg=fg, bg=bg)
                                button_more2_add6.configure(fg=fg, bg=bg)
                                button_more2_add7.configure(fg=fg, bg=bg)
                                button_more2_add8.configure(fg=fg, bg=bg)
                                button_more2_add9.configure(fg=fg, bg=bg)
                                button_more2_adddian.configure(fg=fg, bg=bg)
                                button_more2_add.configure(fg=fg, bg=bg)
                                button_more2_subtract.configure(fg=fg, bg=bg)
                                button_more2_multiply.configure(fg=fg, bg=bg)
                                button_more2_except.configure(fg=fg, bg=bg)
                                button_more2_means.configure(fg=fg, bg=bg)
                                button_more2_reset.configure(fg=fg, bg=bg)
                                button_more2_negative_number.configure(fg=fg, bg=bg)
                                button_more2_exit.configure(fg=fg, bg=bg)
                                button_more2_back.configure(fg=fg, bg=bg)
                                text_more2.configure(fg=fg, bg=bg)
                                Calculator_point_and_click_window.configure(bg=bg)
                                break
                            else:
                                a1 = 'For calculator (input type)？'
                                choose1 = askquestion('question', '%s' % a1)
                                if choose1 == 'yes':
                                    label_more1.configure(fg=fg, bg=bg)
                                    label1_more1.configure(fg=fg, bg=bg)
                                    label2_more1.configure(fg=fg, bg=bg)
                                    button_more1.configure(fg=fg, bg=bg)
                                    button2_more1.configure(fg=fg, bg=bg)
                                    button3_more1.configure(fg=fg, bg=bg)
                                    button4_more1.configure(fg=fg, bg=bg)
                                    button5_more1.configure(fg=fg, bg=bg)
                                    button6_more1.configure(fg=fg, bg=bg)
                                    entry_more1.configure(fg=fg, bg=bg)
                                    entry1_more1.configure(fg=fg, bg=bg)
                                    t.configure(bg=bg)

                                    label1_more.configure(fg=fg, bg=bg)
                                    label2_more.configure(fg=fg, bg=bg)
                                    label3_more.configure(fg=fg, bg=bg)
                                    button_more.configure(fg=fg, bg=bg)
                                    button1_more.configure(fg=fg, bg=bg)
                                    button2_more.configure(fg=fg, bg=bg)
                                    button3_more.configure(fg=fg, bg=bg)
                                    button4_more.configure(fg=fg, bg=bg)
                                    entry_more.configure(fg=fg, bg=bg)
                                    entry1_more.configure(fg=fg, bg=bg)
                                    win.configure(bg=bg)
                                    break
                                else:
                                    a2 = 'Used for the language selection interface？'
                                    choose2 = askquestion('question', '%s' % a2)
                                    if choose2 == 'yes':
                                        language_window.configure(bg=bg)
                                        label_choose_language.configure(fg=fg, bg=bg)
                                        radiobutton_choose_language_1.configure(fg=fg, bg=bg)
                                        radiobutton_choose_language_2.configure(fg=fg, bg=bg)
                                        button_choose_language.configure(fg=fg, bg=bg)
                                    else:
                                        a3 = 'Used for the About interface？'
                                        choose3 = askquestion('question', '%s' % a3)
                                        if choose3 == 'yes':
                                            about_tkinter.configure(bg=bg)
                                            text1.configure(fg=fg, bg=bg)
                                            button_about_reset.configure(fg=fg, bg=bg)
                                            break
                                        else:
                                            label_choose_colour.configure(fg=fg, bg=bg)
                                            color_choose_button.configure(fg=fg, bg=bg)
                                            colour_chooser_tk.configure(bg=bg)
                                            break
                except TclError as e:
                    if language == 0:
                        b = '请选择/打开窗口！'
                        showerror(e, '%s' % b)
                        break
                    elif language == 1:
                        b = 'Please select/open Calculator_point_and_click_window!'
                        showerror(e, '%s' % b)
                        break

        colour_chooser_tk = Tk()
        colour_chooser_tk.geometry('240x240')
        colour_chooser_tk.title('计算器颜色选择界面(Calculator color selection interface)')
        colour_chooser_tk.iconbitmap(default="./calculator-icon_34473.ico")

        if language == 0:
            label_choose_colour = Label(colour_chooser_tk, text='颜色选择界面')
            label_choose_colour.pack()

            color_choose_button = Button(colour_chooser_tk, text='选择颜色（请保持打开）', command=changeColor)
            color_choose_button.pack()
        elif language == 1:
            label_choose_colour = Label(colour_chooser_tk, text='Color selection interface')
            label_choose_colour.pack()

            color_choose_button = Button(colour_chooser_tk, text='Choose a color (please keep the windows open)',
                                         command=changeColor)
            color_choose_button.pack()

    c = Calculator()
    calculator = Tk()
    calculator.geometry("500x500")
    calculator.title('计算器显示界面(The calculator displays the interface)')
    calculator.iconbitmap(default="./calculator-icon_34473.ico")

    label1 = Label(calculator, text='计算器选择界面(Calculator selection interface)')
    label1.pack()

    label2 = Label(calculator,
                   text='qq@小井井，QQ：77173203，邮箱：771732203@qq.com\n(qq@ Xiaojingjing, QQ: 77173203, Email: 771732203@qq.com)')
    label2.place(rely=0.8, relheight=0.2, relx=0.1)

    button1 = Button(calculator, text='计算器（输入式）(Calculator (input))', command=c.Calculator_four_operations)
    button1.place(rely=0.2, relx=0.25, relheight=0.1)

    button2 = Button(calculator, text='计算器（点击式）(Calculator (point-and-click))', command=c.Calculator_point_and_click)
    button2.place(rely=0.3, relx=0.25, relheight=0.1)

    button3 = Button(calculator, text='颜色切换(Color switching)', command=colour_chooser)
    button3.place(rely=0.4, relx=0.25, relheight=0.1)

    button4 = Button(calculator, text='语言(language)', command=language_switching)
    button4.place(rely=0.5, relx=0.25, relheight=0.1)

    button_about = Button(calculator, text='关于(about)', command=about)
    button_about.place(rely=0.6, relx=0.25, relheight=0.1)

    calculator.mainloop()


if __name__ == '__main__':
    try:
        Calculator_main_interface()
    except:
        pass
