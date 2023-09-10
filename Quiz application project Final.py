import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x550')  

questions = [
    "What is the capital of Japan?",
    "Who wrote the novel 'To Kill a Mockingbird'?",
    "Which gas makes up the majority of Earth's atmosphere?",
    "Who is known as the father of modern physics?",
    "Which planet is known as the 'Blue Planet'?"
]

options = [
    ['Tokyo', 'Beijing', 'New York', 'Paris', 'Tokyo'],
    ['Mark Twain', 'Harper Lee', 'George Orwell', 'Jane Austen', 'Harper Lee'],
    ['Oxygen', 'Carbon Dioxide', 'Nitrogen', 'Helium', 'Oxygen'],
    ['Isaac Newton', 'Albert Einstein', 'Marie Curie', 'Charles Darwin', 'Albert Einstein'],
    ['Mars', 'Earth', 'Venus', 'Jupiter', 'Earth']
]

frame = tk.Frame(root, padx=10, pady=10, bg='#fff')
question_label = tk.Label(frame, height=5, width=28, bg='grey', fg="#fff",
                          font=('Verdana', 20), wraplength=500)

v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, text="A", font=('Verdana', 20),
                         command=lambda: checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20),
                         command=lambda: checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, text="B", font=('Verdana', 20),
                         command=lambda: checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20),
                         command=lambda: checkAnswer(option4))

score_label = tk.Label(root, text="Score: 0", font=('Verdana', 16))
pass_note_label = tk.Label(root, text="Minimum score to pass: 3", font=('Verdana', 12), fg="blue")

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky='W', row=1, column=0)
option2.grid(sticky='W', row=2, column=0)
option3.grid(sticky='W', row=3, column=0)
option4.grid(sticky='W', row=4, column=0)

score_label.pack(pady=10)
pass_note_label.pack(pady=10)

index = 0
correct = 0

def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state

def checkAnswer(radio):
    global correct, index
    if radio['text'] == options[index][4]:
        correct += 1

    index += 1
    disableButtons('disable')
    score_label.config(text=f"Score: {correct}/{len(questions)}")

def restartQuiz():
    global index, correct
    index = 0
    correct = 0
    question_label['text'] = ""
    question_label['bg'] = 'grey'  # to Reset background color
    score_label.config(text="Score: 0")
    button_next.config(text="Next", command=displayNextQuestion)
    displayNextQuestion()

def displayNextQuestion():
    global index, correct
    if index == len(options):
        question_label['text'] = str(correct) + " / " + str(len(options))
        if correct >= 3:
            question_label['bg'] = 'green'
            messagebox.showinfo("Congratulations", "You have passed the quiz!")
        else:
            question_label['bg'] = 'red'
            messagebox.showinfo("Try Again", "You can do better next time!")

        button_next.config(text="Restart The Quiz", command=restartQuiz)

    else:
        question_label['text'] = questions[index]

        disableButtons('normal')
        opts = options[index]
        option1.config(text=opts[0])
        option2.config(text=opts[1])
        option3.config(text=opts[2])
        option4.config(text=opts[3])
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next.config(text="Check the Results", command=displayNextQuestion)

button_next = tk.Button(root, text='Next', bg='Orange', font=('Verdana', 20), command=displayNextQuestion)
button_next.pack(pady=10)

displayNextQuestion()

root.mainloop()
