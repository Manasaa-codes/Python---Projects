tasks = []

try:
    with open("tasks.txt","r") as file:
        tasks =[line.strip() for line in file]
except FileNotFoundError:
    tasks = []

import tkinter as tk
root = tk.Tk()
root.configure(bg="#f4f6f8")
root.resizable(False,False)
root.title("Todo App")
root.geometry("450x650")
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

title=tk.Label(root,text ="Todo App",font=("Arial",20,"bold"),bg="#f4f6f8",fg="#333")
title.grid(row=0,column=0,columnspan=2,pady=15)

def add_task():
    task = entry.get()
    if task == "":
        return
    tasks.append(task)
    listbox.insert(tk.END,task)
    entry.delete(0,tk.END)
    save_tasks()
    refresh_list()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        return
    index = selected[0]
    tasks.pop(index)
    listbox.delete(index)
    save_tasks()
    refresh_list()

def save_tasks():
    with open("tasks.txt","w") as file:
        for task in tasks:
            file.write(task+"\n")

def load_task(event):
    selected=listbox.curselection()
    if not selected:
        return
    index= selected[0]
    entry.delete(0,tk.END)
    entry.insert(0,tasks[index])

def update_task():
    selected=listbox.curselection()
    if not selected:
        return
    index=selected[0]
    new_task=entry.get()
    if new_task=="":
        return
    tasks[index]=new_task
    save_tasks()
    refresh_list()
    entry.delete(0,tk.END)

def complete_task():
    selected=listbox.curselection()
    if not selected:
        return
    index=selected[0]

    tasks[index]="✔" + tasks[index].replace("✔ ","")
    save_tasks()
    refresh_list()

def search_task():
    keyword=search_entry.get().lower()

    listbox.delete(0,tk.END)
    for task in tasks:
        if keyword in task.lower():
            listbox.insert(tk.END,task)

def show_all_tasks():
    refresh_list()

def refresh_list():
    listbox.delete(0,tk.END)
    for task in tasks:
        listbox.insert(tk.END,task)
    
def live_search(event):
    keyword=search_entry.get().lower()
    listbox.delete(0,tk.END)

    for task in tasks:
        if keyword in task.lower():
            listbox.insert(tk.END,task)

def toggle_theme():
    global dark_mode

    if not dark_mode:
        root.configure(bg="#1e1e1e")
        title.config(bg="#1e1e1e",fg="white")
        dark_mode=True
    else:
        root.configure(bg="#f4f6f8")
        title.configure(bg="#f4f6f8",fg="#333")
        dark_mode=False

entry=tk.Entry(root,width=25,font=("Segoe UI",12),relief="solid",bd=1)
entry.grid(row=1, column=0, padx=10, pady=10)

button=tk.Button(root,text="Add Task",command=add_task,bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"))
button.grid(row=1,column=1,padx=10,pady=5)

frame_list=tk.Frame(root)
frame_list.grid(row=2,column=0,columnspan=2,pady=10)

scrollbar=tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

listbox=tk.Listbox(frame_list,width=45,height=15,font=("Segoe UI",11),yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)
scrollbar.config(command=listbox.yview)

delete_button=tk.Button(root,text="Delete",bg="#e53935",fg="white",command=delete_task,font=("Segoe UI", 10))
delete_button.grid(row=3,column=0,columnspan=2,pady=6)

update_button = tk.Button(root,text="Update", bg="#1e88e5", fg="white", font=("Segoe UI", 10))
update_button.grid(row=4,column=0,columnspan=2,pady=6)

complete_button = tk.Button(root,text="Complete",command=complete_task,bg="#fb8c00", fg="white", font=("Segoe UI", 10))
complete_button.grid(row=5,column=0,columnspan=2,pady=6)

search_entry = tk.Entry(root,width=25,font=("Segoe UI",11))
search_entry.grid(row=6,column=0,padx=10,pady=5)
search_entry.bind("<KeyRelease>",live_search)

search_button = tk.Button(root,text="Search",command=search_task)
search_button.grid(row=6,column=1,pady=6)

show_all_button=tk.Button(root,text="Show All",command=show_all_tasks)
show_all_button.grid(row=7,column=0,columnspan=2,pady=6)

theme_button = tk.Button(root,text="Dark Mode",command=toggle_theme)
theme_button.grid(row=8,column=0,columnspan=2,pady=10)

for task in tasks:
    listbox.insert(tk.END,task)

dark_mode=False

root.mainloop()
