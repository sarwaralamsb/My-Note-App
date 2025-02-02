import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get("1.0", tk.END).strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_listbox.itemconfig(tk.END, {'bg': '#FFF9C4'})  # Light yellow background for new tasks
        add_popup.withdraw()  # Close the popup
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def open_add_popup():
    global add_popup, task_entry
    add_popup = tk.Toplevel(root)
    add_popup.title("Add New Task")
    add_popup.geometry("400x300")
    
    task_entry = tk.Text(add_popup, font=("Arial", 12), height=6, wrap=tk.WORD)
    task_entry.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    add_button = tk.Button(add_popup, text="Add Task", command=add_task, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10)
    add_button.pack(pady=10)

def open_edit_popup(task, index):
    edit_popup = tk.Toplevel(root)
    edit_popup.title("Edit Task")
    edit_popup.geometry("400x300")
    
    task_entry = tk.Text(edit_popup, font=("Arial", 12), height=6, wrap=tk.WORD)
    task_entry.insert(tk.END, task)
    task_entry.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

    def save_edited_task():
        new_task = task_entry.get("1.0", tk.END).strip()
        if new_task:
            task_listbox.delete(index)
            task_listbox.insert(index, new_task)  # Insert the updated task without "..."
            task_listbox.itemconfig(index, {'bg': '#FFF9C4'})  # Apply slight yellow background to updated task
            edit_popup.withdraw()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    save_button = tk.Button(edit_popup, text="Save", command=save_edited_task, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10)
    save_button.pack(pady=10)

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def on_task_double_click(event):
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        task = task_listbox.get(index)
        open_edit_popup(task, index)

# Creating the main window
root = tk.Tk()
root.title("My Note App")
root.geometry("350x500")
root.minsize(350, 500)  # Prevents resizing below this size
root.configure(bg="#f0f0f0")
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=open_add_popup, font=("Arial", 12), bg="#4CAF50", fg="white", padx=10)
add_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Task Listbox
list_frame = tk.Frame(root, bg="#f0f0f0")
list_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, font=("Arial", 12), selectbackground="#d3d3d3", yscrollcommand=scrollbar.set)
task_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

task_listbox.config(selectmode=tk.SINGLE)

scrollbar.config(command=task_listbox.yview)

# Bind task double-click to open edit popup
task_listbox.bind("<Double-1>", on_task_double_click)

# Buttons Frame (remove and clear)
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

remove_button = tk.Button(buttons_frame, text="Remove", command=remove_task, font=("Arial", 10), bg="#f44336", fg="white", padx=10)
remove_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)

clear_button = tk.Button(buttons_frame, text="Clear All", command=clear_tasks, font=("Arial", 10), bg="#FFC107", fg="black", padx=10)
clear_button.pack(side=tk.RIGHT, padx=5, expand=True, fill=tk.X)

# Run the application
root.mainloop()
