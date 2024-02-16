import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(pady=10)

listbox_tasks = tk.Listbox(frame, height=10, width=50, selectbackground="lightblue")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add = tk.Button(root, text="Add Task", width=20, command=add_task)
button_add.pack(side=tk.LEFT, padx=5)

button_delete = tk.Button(root, text="Delete Task", width=20, command=delete_task)
button_delete.pack(side=tk.RIGHT, padx=5)

# Run the application
root.mainloop()
