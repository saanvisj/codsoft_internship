import tkinter as t                                    #abbrevated to t
from tkinter import ttk as s                           #abbrevated to s
from tkinter import messagebox as mb                   #abbrevated to mb

def add_task():                                        #adding tasks
    task_string = task_field.get()
    if len(task_string) == 0:
        mb.showinfo('Error', 'Field is Empty.')        #error for no task entered
    else:
        tasks.append(task_string)
        list_update()
        task_field.delete(0, 'end')

def list_update():                                      #updating lists
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():                                       #delete tasks
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
    except:
        mb.showinfo('Error', 'No Task Selected. Cannot Delete.')  #error if no task selected

def delete_all_tasks():                                    #delete all tasks
    message_box = mb.askyesno('Delete All', 'Are you sure?')
    if message_box == True:
        tasks.clear()
        clear_list()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

#*******proving aesthetics for the list*********

if __name__ == "__main__":
    guiWindow = t.Tk()
    guiWindow.title("To-Do List using python")
    guiWindow.geometry("600x400+600+300")  
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#1E1E1E")  

    # Create a style object
    style = s.Style()
    style.configure("TButton", font=("Roboto", 10), background="#4285F4") #button styling

    tasks = []
    
    #header
    header_frame = t.Frame(guiWindow, bg="#1E1E1E")
    functions_frame = t.Frame(guiWindow, bg="#1E1E1E")
    listbox_frame = t.Frame(guiWindow, bg="#1E1E1E")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = s.Label(   
        header_frame,
        text="To-Do List",
        font=("Roboto", "40"), 
        background="#1E1E1E",
        foreground="#4285F4" 
    )
    header_label.pack(padx=20, pady=20)
      
    #task labels
    task_label = s.Label(
        functions_frame,
        text="Enter the Task:",
        font=("Roboto", "12", "bold"),  
        background="#1E1E1E",
        foreground="#FFFFFF"  
    )
    task_label.place(x=30, y=40)

    task_field = s.Entry(
        functions_frame,
        font=("Roboto", "12"),
        width=25, 
        background="#FFFFFF",
        foreground="#000000"  
    )
    task_field.place(x=30, y=80)
    
    #creating buttons

    add_button = s.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task
    )
    del_button = s.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task
    )
    del_all_button = s.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks
    )
    exit_button = s.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close
    )
    add_button.place(x=30, y=120)
    del_button.place(x=30, y=160)
    del_all_button.place(x=30, y=200)
    exit_button.place(x=30, y=240)

    task_listbox = t.Listbox(
        listbox_frame,
        width=32,  
        height=13,
        selectmode='SINGLE',
        background="#FFFFFF",
        foreground="#000000",
        selectbackground="#4285F4",  
        selectforeground="#FFFFFF"  
    )
    task_listbox.place(x=10, y=20)

    guiWindow.mainloop()
