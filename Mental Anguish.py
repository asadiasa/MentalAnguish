# Aira Sadiasa CIS 345 T/Th 10:30 Project Beta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


class Question:
    """Model questions and transition the canvas of the application to take the Quiz game"""
    global pts

    def __init__(self, question, choice1, choice2, choice3, choice4, correct_feedback, incorrect_feedback,
                 correct_ans, points=0):
        self.new_question = question
        self.points = points
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.correct_feedback = correct_feedback
        self.incorrect_feedback = incorrect_feedback
        self.correct_answer = correct_ans

    @property  # format
    def new_question(self):
        return self.__new_question

    @new_question.setter  # validation
    def new_question(self, new_text):
        self.__new_question = new_text

    @property
    def choice1(self):
        return self.__choice1

    @choice1.setter
    def choice1(self, new_choice):
        self.__choice1 = new_choice

    @property
    def choice2(self):
        return self.__choice2

    @choice2.setter
    def choice2(self, new_choice):
        self.__choice2 = new_choice

    @property
    def choice3(self):
        return self.__choice3

    @choice3.setter
    def choice3(self, new_choice):
        self.__choice3 = new_choice

    @property
    def choice4(self):
        return self.__choice4

    @choice4.setter
    def choice4(self, new_choice):
        self.__choice4 = new_choice

    @property
    def correct_feedback(self):
        return self.__correct_feedback

    @correct_feedback.setter
    def correct_feedback(self, new_feedback):
        self.__correct_feedback = new_feedback

    @property
    def incorrect_feedback(self):
        return self.__incorrect_feedback

    @incorrect_feedback.setter
    def incorrect_feedback(self, new_feedback):
        self.__incorrect_feedback = new_feedback

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, new_answer):
        self.__correct_answer = new_answer

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, new_points):
        self.__points = new_points

    def __str__(self):
        return f'{self.new_question}, {self.choice1},{self.choice2},{self.choice3}, {self.choice4},' \
               f'{self.correct_feedback},{self.incorrect_feedback},{self.correct_answer},{self.points}'


def get_questions(file):
    """Open txt file to get questions"""
    with open(file, 'r') as fp:
        for line in fp:
            line = line.strip()
            yield line


def EmptyFieldError(Error):
    """Raise when data field is empty"""
    pass


def save_question():
    """Save question and add to the question pool"""
    global question_list, question_text, choice_1, choice_2, choice_3, choice_4, \
        c_feedback, i_feedback, c_choice, pts, lstbx, question_list, question_details, points_entry, edit_mode, edit_index
    valid_points = ['1', '2', '3']
    points = str(pts.get().strip())
    if points not in valid_points:
        messagebox.showerror(title='Error', message='Point value must be between 1-3')
    elif edit_mode:
        question_list.pop(edit_index)
        question_details.pop(edit_index)
        lstbx.delete(edit_index)
        edit_mode = False
    try:
        temp_question = Question(question_text.get(), choice_1.get(), choice_2.get(), choice_3.get(), choice_4.get(),
                                 c_feedback.get(), i_feedback.get(), c_choice.get(), pts.get())
    except ValueError:
        messagebox.showerror(title='Incorrect Input', message='Please enter data in correct fields')
    else:
        question_list.append(temp_question.new_question)
        question_details.append(temp_question)
        lstbx.insert(END, question_text.get())
        with open('question_pool.txt', 'w') as fp:
            for question in question_details:
                fp.write(str(question)+('\n'))


def edit_question(event):
    """Edit an existing question"""
    global question_list, question_text, choice_1, choice_2, choice_3, choice_4, \
        c_feedback, i_feedback, c_choice, pts, lstbx, question_list, question_details, edit_mode, edit_index
    edit_mode = True
    edit_index = lstbx.curselection()[0]
    print(edit_index)
    temp = question_details[edit_index]
    question_text.set(temp.new_question)
    choice_1.set(temp.choice1)
    choice_2.set(temp.choice2)
    choice_3.set(temp.choice3)
    choice_4.set(temp.choice4)
    c_feedback.set(temp.correct_feedback)
    i_feedback.set(temp.incorrect_feedback)
    c_choice.set(temp.correct_answer)
    pts.set(temp.points)


def delete_question():
    global edit_index, question_details, question_list, lstbx
    edit_index = lstbx.curselection()[0]
    question_details.pop(edit_index)
    question_list.pop(edit_index)
    lstbx.delete(edit_index)
    with open('question_pool.txt', 'w') as fp:
        for question in question_details:
            fp.write(str(question)+'\n')


def search_question():
    """User has ability to search for a question"""
    pass


def take_quiz():
    """Enter quiz mode and allow the user to play the game"""
    global quiz_mode, window_heading, quiz_questions, quiz_question_count
    quiz_mode = True
    quiz_question_count = 0
    window_heading.set('Quiz')
    win.geometry('700x400')
    correct_label.grid_forget()
    correct_entry.grid_forget()
    incorrect_label.grid_forget()
    incorrect_entry.grid_forget()
    cancel_button.grid_forget()
    lstbx.grid_forget()
    lstbx_label.grid_forget()
    user_choice_entry.grid(row=8, column=1, ipadx=entry_padding, pady=10)
    pb.grid(row=12, column=1, ipadx=30, pady=30)
    save_button.config(command=check_answer, text='Submit')
    take_quiz_button.config(command=next_question, text='Next')

    quiz_questions = random.sample(question_details, k=3)
    question_text.set(quiz_questions[0].new_question)
    pts.set(quiz_questions[0].points)
    choice_1.set(quiz_questions[0].choice1)
    choice_2.set(quiz_questions[0].choice2)
    choice_3.set(quiz_questions[0].choice3)
    choice_4.set(quiz_questions[0].choice4)
    c_feedback.set(quiz_questions[0].correct_feedback)
    i_feedback.set(quiz_questions[0].incorrect_feedback)
    c_choice.set(quiz_questions[0].correct_answer)
    quiz_question_count += 1

    question_entry.config(state=DISABLED)
    points_entry.config(state=DISABLED)
    choice1_entry.config(state=DISABLED)
    choice2_entry.config(state=DISABLED)
    choice3_entry.config(state=DISABLED)
    choice4_entry.config(state=DISABLED)
    correct_entry.config(state=DISABLED)
    incorrect_entry.config(state=DISABLED)


def check_answer():
    """Checks user's answer and assign points"""
    global c_feedback, i_feedback, c_choice, pts, player_score, entry_padding, quiz_question_count
    user = user_answer.get()
    machine = c_choice.get()
    points = int(pts.get())
    print(user)
    print(machine)
    if user.casefold() == machine.casefold():
        player_score += points
        correct_label.grid(row=9, column=0, ipadx=10)
        correct_entry.grid(row=9, column=1, ipadx=entry_padding)
    else:
        incorrect_label.grid(row=9, column=0, ipadx=10)
        incorrect_entry.grid(row=9, column=1, ipadx=entry_padding)
    if quiz_question_count == 3:
        save_button.config(state=DISABLED)
        take_quiz_button.config(state=DISABLED)
        messagebox.showinfo(title='You made it!', message=f'You scored {player_score} points')

    pb['value'] += 100
    print(player_score)


def next_question():
    """Move to the next question"""
    global quiz_question_count, quiz_questions
    correct_label.grid_forget()
    correct_entry.grid_forget()
    incorrect_label.grid_forget()
    incorrect_entry.grid_forget()
    user_answer.set('')

    if quiz_question_count == 1:
        question_text.set(quiz_questions[1].new_question)
        pts.set(quiz_questions[1].points)
        choice_1.set(quiz_questions[1].choice1)
        choice_2.set(quiz_questions[1].choice2)
        choice_3.set(quiz_questions[1].choice3)
        choice_4.set(quiz_questions[1].choice4)
        c_feedback.set(quiz_questions[1].correct_feedback)
        i_feedback.set(quiz_questions[1].incorrect_feedback)
        c_choice.set(quiz_questions[1].correct_answer)
        quiz_question_count += 1
    elif quiz_question_count == 2:
        question_text.set(quiz_questions[2].new_question)
        pts.set(quiz_questions[2].points)
        choice_1.set(quiz_questions[2].choice1)
        choice_2.set(quiz_questions[2].choice2)
        choice_3.set(quiz_questions[2].choice3)
        choice_4.set(quiz_questions[2].choice4)
        c_feedback.set(quiz_questions[2].correct_feedback)
        i_feedback.set(quiz_questions[2].incorrect_feedback)
        c_choice.set(quiz_questions[2].correct_answer)
        quiz_question_count += 1


def toggle():
    """Clear all entry fields. Allows to switch between quiz mode and edit mode"""
    global entry_padding, question_text, choice_1, choice_2, choice_3, choice_4, c_feedback, i_feedback, c_choice, pts, edit_mode
    win.geometry('800x600')
    window_heading.set('Create Questions')
    question_text.set('')
    choice_1.set('')
    choice_2.set('')
    choice_3.set('')
    choice_4.set('')
    c_feedback.set('')
    i_feedback.set('')
    c_choice.set('')
    pts.set('')
    pb.grid_forget()
    edit_mode = False

    points_entry.config(state=NORMAL)
    question_entry.config(state=NORMAL)
    choice1_entry.config(state=NORMAL)
    choice2_entry.config(state=NORMAL)
    choice3_entry.config(state=NORMAL)
    choice4_entry.config(state=NORMAL)
    correct_entry.config(state=NORMAL)
    incorrect_entry.config(state=NORMAL)
    correct_choice_entry.config(state=NORMAL)

    correct_choice_label.grid(row=8, column=0, ipadx=10)
    correct_choice_entry.grid(row=8, column=1, ipadx=entry_padding)
    correct_label.grid(row=9, column=0, ipadx=10)
    correct_entry.grid(row=9, column=1, ipadx=entry_padding)
    incorrect_label.grid(row=10, column=0, ipadx=10)
    incorrect_entry.grid(row=10, column=1, ipadx=entry_padding)

    cancel_button.grid(row=11, column=1, ipadx=20, pady=10, sticky=W)
    save_button.grid(row=11, column=1, pady=8, ipadx=30)
    take_quiz_button.config(text='Take Quiz')
    take_quiz_button.config(command=take_quiz)
    take_quiz_button.grid(row=11, column=1, ipadx=15, sticky=E)

    lstbx_label.grid(row=12, column=1, sticky=W)
    lstbx.grid(row=13, column=1, columnspan=3, pady=5, sticky=W, ipadx=30)


def insert_lstbx():
    global question_details, question_list
    for question in question_list:
        question = str(question)
        lstbx.insert(END, question)


# Build window called win
win = Tk()
win.config(bg='linen')
win.title('Mental Anguish')
win.geometry('800x600')

# Variables
color = 'linen'
entry_padding = 130
question_text = StringVar()
choice_1 = StringVar()
choice_2 = StringVar()
choice_3 = StringVar()
choice_4 = StringVar()
c_feedback = StringVar()
i_feedback = StringVar()
c_choice = StringVar()
user_answer = StringVar()
pts = StringVar()
window_heading = StringVar()
question_list = []
question_details = []
quiz_questions = []
quiz_question_count = 0
edit_mode = FALSE
edit_index = 0
quiz_mode = FALSE
player_score = 0

# Menu System
menu_bar = Menu(win)
win.config(menu=menu_bar)
edit_menu = Menu(menu_bar, tearoff=False)
edit_menu.add_command(label='View', command=toggle)
edit_menu.add_command(label='Edit', command=toggle)
edit_menu.add_command(label='Add', command=toggle)
edit_menu.add_command(label='Delete', command=delete_question)
edit_menu.add_command(label='Search', command=search_question)

file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label='New')
file_menu.add_command(label='Exit')

menu_bar.add_cascade(label='File', menu=file_menu)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

# Labels & Entry
title_label = Label(win, textvariable=window_heading, bg=color, font='bold')
window_heading.set('Create Questions')
title_label.grid(row=0, column=1, pady=15)

question_label = Label(win, text='Question: ', bg=color, font='bold')
question_label.grid(row=2, column=0, ipadx=10)
question_entry = Entry(win, textvariable=question_text)
question_entry.grid(row=2, column=1, ipadx=entry_padding)

points_label = Label(win, text='Points(1-3): ', bg=color, font='bold')
points_label.grid(row=3, column=0)
points_entry = Entry(win, textvariable=pts)
points_entry.grid(row=3, column=1, ipadx=entry_padding)

choice1_label = Label(win, text='Choice A: ', bg=color, font='bold')
choice1_label.grid(row=4, column=0, ipadx=10)
choice1_entry = Entry(win, textvariable=choice_1)
choice1_entry.grid(row=4, column=1, ipadx=entry_padding)

choice2_label = Label(win, text='Choice B: ', bg=color, font='bold')
choice2_label.grid(row=5, column=0, ipadx=10)
choice2_entry = Entry(win, textvariable=choice_2)
choice2_entry.grid(row=5, column=1, ipadx=entry_padding)

choice3_label = Label(win, text='Choice C: ', bg=color, font='bold')
choice3_label.grid(row=6, column=0, ipadx=10)
choice3_entry = Entry(win, textvariable=choice_3)
choice3_entry.grid(row=6, column=1, ipadx=entry_padding)

choice4_label = Label(win, text='Choice D: ', bg=color, font='bold')
choice4_label.grid(row=7, column=0, ipadx=10)
choice4_entry = Entry(win, textvariable=choice_4)
choice4_entry.grid(row=7, column=1, ipadx=entry_padding)

correct_choice_label = Label(win, text='Answer: ', bg=color, font='bold')
correct_choice_label.grid(row=8, column=0, ipadx=10)
correct_choice_entry = Entry(win, textvariable=c_choice)
correct_choice_entry.grid(row=8, column=1, ipadx=entry_padding)
user_choice_entry = Entry(win, textvariable=user_answer)
user_choice_entry.grid(row=8, column=1, ipadx=entry_padding)
user_choice_entry.grid_forget()

correct_label = Label(win, text='Correct Feedback: ', bg=color, font='bold')
correct_label.grid(row=9, column=0, ipadx=10)
correct_entry = Entry(win, textvariable=c_feedback)
correct_entry.grid(row=9, column=1, ipadx=entry_padding)

incorrect_label = Label(win, text='Incorrect Feedback: ', bg=color, font='bold')
incorrect_label.grid(row=10, column=0, ipadx=10)
incorrect_entry = Entry(win, textvariable=i_feedback)
incorrect_entry.grid(row=10, column=1, ipadx=entry_padding)


# Listbox
lstbx = Listbox(win, width=60)
lstbx_label = Label(win, text="Double click on a question to edit", bg=color, font='bold')
lstbx_label.grid(row=12, column=1, sticky=W)
lstbx.bind("<Double-Button-1>", edit_question)
lstbx.grid(row=13, column=1, columnspan=3, pady=5, sticky=W, ipadx=30)


# Clear Button
cancel_button = Button(win, command=toggle, text='Clear', cursor='heart')
cancel_button.grid(row=11, column=1, ipadx=20, pady=10, sticky=W)

# Save Button
save_button = Button(win, command=save_question, text='Save', cursor='heart')
save_button.grid(row=11, column=1, pady=8, ipadx=30)

# Progressbar
pb = ttk.Progressbar(win, orient='horizontal', maximum=301, mode='determinate')
pb.grid(row=12, column=1, ipadx=30)
pb.grid_forget()

# Take Quiz
take_quiz_button = Button(win, command=take_quiz, text='Take Quiz', cursor='heart')
take_quiz_button.grid(row=11, column=1, ipadx=15, sticky=E)


question_pool = get_questions('question_pool.txt')
for q in question_pool:
    # Comma split separates each part of a question and assigns it to temporary variable
    try:
        (temp_q, temp_1, temp_2, temp_3, temp_4, temp_cfeedback, temp_ifeedback, temp_answer, temp_pts) = q.split(',')
    except TypeError:
        messagebox.showerror(title='Invalid Input', message='Please enter all required data')
    else:
        # Add each question to the list of questions to be displayed to the user
        question_list.append(temp_q)
        question_item = Question(temp_q, temp_1, temp_2, temp_3, temp_4, temp_cfeedback, temp_ifeedback, temp_answer,
                                 temp_pts)
        question_details.append(question_item)

insert_lstbx()

win.mainloop()
