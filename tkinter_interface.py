import tkinter as tk

root = tk.Tk()
root.title('Twitter follows research')
root.geometry('500x200')

user_entries = []

def expose_text():
    entry_list = []
    for entries in user_entries:
        input = str(entries.get())
        entry_list.append(input)
    user_ids = get_user_ids_u(entry_list)
    follows = get_follows(user_ids)
    output = pct_overlap(follows)
    label.config(text=str(output))

label1Text = tk.StringVar()
label1Text.set('Enter first username:')
user1_label = tk.Label(root, textvariable=label1Text, height=4)
user1_label.grid(row=1, column=1)

#for x in range(2):
directory1 = tk.StringVar(None)
user_input1 = tk.Entry(root, textvariable=directory1, width=50)
user_input1.grid(row=1, column=2)
user_entries.append(user_input1)

label2Text = tk.StringVar()
label2Text.set('Enter second username:')
user2_label = tk.Label(root, textvariable=label2Text, height=4)
user2_label.grid(row=2, column=1)

directory2 = tk.StringVar(None)
user_input2 = tk.Entry(root, textvariable=directory2, width=50)
user_input2.grid(row=2, column=2)
user_entries.append(user_input2)

label = tk.Label(root, text='')
label.grid(row=3, column=2)

submit_button = tk.Button(root, text='Enter', command=expose_text)
submit_button.grid(row=4, column=2)

root.mainloop()
