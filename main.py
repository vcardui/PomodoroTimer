from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checks_mark = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_count_down():
    global timer
    global reps
    global checks_mark
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    mainText.config(text="Timer")
    checks.config(text="")
    checks_mark = ""
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        mainText.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
        reps = 0
    elif reps % 2 == 0:
        mainText.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        mainText.config(text="Working Time", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global checks_mark

    canvas.itemconfig(timer_text, text=f"{time.strftime('%M:%S', time.gmtime(count))}")
    if 0 < count:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if (reps % 2) == 0:
            checks_mark += '✔ '
            checks.config(text=f"{checks_mark}",)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)


#MainText
mainText = Label(text="Timer", font=(FONT_NAME, 48), fg=GREEN, bg=YELLOW)
mainText.grid(column=1, row=0)

#Tomatito
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatito_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatito_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Start
start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

#Reset
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_count_down)
reset_button.grid(column=2, row=2)

#Check
checks = Label(font=(FONT_NAME, 28), fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)

window.mainloop()