from tkinter import *
def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(END,task)
        task_entry.delete(0,END)
    else:
        status_label.config(text="Task cannot be empty")
def delete_task():
    try:
        selected_task_index = tasks_list.curselection()[0]  
        tasks_list.delete(selected_task_index)
        status_label.config(text="Task deleted")
    except IndexError:
        status_label.config(text="Please select a task to delete!")
root = Tk()
root.title("To-Do List")
root.geometry("500x500")
frame = Frame(root)
frame.pack(pady=20)
task_entry = Entry(frame,width=30)
task_entry.pack(side=RIGHT,padx=5)
add_button = Button(frame,text="Add",command=add_task)
add_button.pack(side=RIGHT)
tasks_list = Listbox(root,width=50,height=20)
tasks_list.pack(pady=20)
delete_button = Button(root,text="Delete",command=delete_task)
delete_button.pack(pady=10)
status_label = Label(root,text="",fg="red")
status_label.pack()
root.mainloop()
