import tkinter as tk
from tkinter import messagebox, filedialog
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        # Title
        self.title = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"))
        self.title.pack(pady=10)

        # Entry box
        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
        self.task_entry.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Task", width=12, command=self.add_task)
        self.add_button.grid(row=0, column=0, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Task", width=12, command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        self.save_button = tk.Button(self.button_frame, text="Save", width=12, command=self.save_tasks)
        self.save_button.grid(row=1, column=0, pady=5)

        self.load_button = tk.Button(self.button_frame, text="Load", width=12, command=self.load_tasks)
        self.load_button.grid(row=1, column=1, pady=5)

        # Listbox
        self.task_listbox = tk.Listbox(root, height=15, width=40, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()
            if not selected:
                raise IndexError
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Success", "Tasks saved successfully.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt")])
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                self.tasks = [line.strip() for line in f]
                self.task_listbox.delete(0, tk.END)
                for task in self.tasks:
                    self.task_listbox.insert(tk.END, task)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
