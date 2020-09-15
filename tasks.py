from tkinter import *
from datetime import datetime


def create_task():
    tasks.append(message.get())
    message_entry.delete(0, 'end')  # проверить
    func_button(tasks[-1])


def func_button(text):
    var = Variable()
    cb = Checkbutton(text=text, variable=var, onvalue=1, offvalue=0)
    cb.pack(anchor=W)


def btn_start():
    timer()


def timer():
    global temp, after_id
    after_id = root.after(1000, timer)
    f_temp = datetime.utcfromtimestamp(temp).strftime("%H:%M:%S")
    l.configure(text=str(f_temp))
    temp += 1


def btn_stop():
    root.after_cancel(after_id)


def btn_cont():
    timer()


def btn_reset():
    global temp

    temp = 0
    l.configure(text="00:00:00")
    root.after_cancel(after_id)


if __name__ == "__main__":
    tasks = []
    temp = 0
    after_id = ''

    root = Tk()
    root.title("Задачи на день")
    root.geometry("500x500")

    message = StringVar()
    message_entry = Entry(textvariable=message)
    message_entry.place(relx=.8, rely=.04, anchor="c")

    message_button = Button(text="add", font=(
        "Ubuntu", 12), command=create_task)
    message_button.place(relx=.8, rely=.1, anchor="c")

    l = Label(root, width=7, font=("Ubuntu", 10), text="00:00:00")
    l.pack(side=BOTTOM, fill=Y)

    btn_start = Button(root, text="Start", font=(
        "Ubuntu", 9), command=btn_start, bg="green")
    btn_stop = Button(root, text="Stop", font=(
        "Ubuntu", 9), command=btn_stop, bg="red")
    btn_cont = Button(root, text="Continue",
                      command=btn_cont, font=("Ubuntu", 9))
    btn_reset = Button(root, text="Reset",
                       command=btn_reset, font=("Ubuntu", 9))

    btn_start.place(relx=.6, rely=.94)
    btn_stop.place(relx=.68, rely=.94)
    btn_cont.place(relx=.76, rely=.94)
    btn_reset.place(relx=.89, rely=.94)

    root.mainloop()