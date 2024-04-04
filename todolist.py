import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To do list")

        # Centering the window
        window_width = 400
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.task_entry = tk.Entry(self.main_frame, font=("Arial", 12), bd=2, relief="flat")
        self.task_entry.pack(side="top", fill="x", padx=5, pady=5)

        self.add_button = tk.Button(self.main_frame, text="Add Task", command=self.add_task, font=("Arial", 12), bg="#007BFF", fg="white", relief="raised")
        self.add_button.pack(side="top", fill="x", padx=5, pady=5)

        self.task_listbox = tk.Listbox(self.main_frame, font=("Arial", 12), bd=2, relief="flat")
        self.task_listbox.pack(side="top", fill="both", expand=True, padx=5, pady=5)

        self.delete_button = tk.Button(self.main_frame, text="Delete Task", command=self.delete_task, font=("Arial", 12), bg="#DC3545", fg="white", relief="raised")
        self.delete_button.pack(side="left", fill="x", padx=5, pady=5)

        self.update_button = tk.Button(self.main_frame, text="Update Task", command=self.update_task, font=("Arial", 12), bg="#28A745", fg="white", relief="raised")
        self.update_button.pack(side="left", fill="x", padx=5, pady=5)

        self.complete_button = tk.Button(self.main_frame, text="Complete Task", command=self.complete_task, font=("Arial", 12), bg="#FFC107", fg="black", relief="raised")
        self.complete_button.pack(side="left", fill="x", padx=5, pady=5)

        self.task_listbox.bind('<<ListboxSelect>>', self.select_task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"text": task, "completed": False})
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def select_task(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, task["text"])

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[index]["text"] = new_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, new_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            task["completed"] = not task["completed"]
            self.update_task_appearance(index)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as complete.")

    def update_task_appearance(self, index):
        task = self.tasks[index]
        if task["completed"]:
            self.task_listbox.itemconfig(index, bg="lightgrey", fg="red")
        else:
            self.task_listbox.itemconfig(index, bg="white", fg="black")

def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
