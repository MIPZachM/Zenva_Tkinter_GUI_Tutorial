import tkinter as tk

# TODOLIST-ITEM CLASS
class TodoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description
# END TODOLIST ITEM CLASS

# TODOLIST-APP CLASS
class TodoListApp:

    # Init Function
    def __init__(self, tkinter_root):
        # Initial tkinter root configuration
        self.root = tkinter_root
        self.root.title("To-Do List App - Zenva Tkinter Tutorial")
        # self.root.geometry("400x500")

        # Configure a frame
        frame = tk.Frame(self.root, borderwidth=2, relief="groove")
        frame.grid(column=1, row=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=5)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)

        # Configure a second frame
        frame_new_item = tk.Frame(self.root, borderwidth=2, relief="groove")
        frame_new_item.grid(column=2, row=1, sticky=(tk.N, tk.S, tk.E, tk.W), padx=5, pady=5)

        # Create Default To-Do
        self.todo_list_items = [
            TodoItem("Workout", "Treadmill for 1 hour"),
            TodoItem("Dishes", "Dishes in the sink"),
            TodoItem("Programming", "Finish Tkinter tutorial"),
            TodoItem("Pets", "Feed the cats")
        ]
        self.todo_list_names = tk.StringVar(value=list(map(lambda x: x.name, self.todo_list_items)))

        # Configure Item List Label
        list_label = tk.Label(frame, text="To Do Items", font="Helvetica 10 bold")
        list_label.grid(column=1, row=1, sticky=(tk.S, tk.W), padx=25, pady=10)

        # Configure ListBox
        items_list_box = tk.Listbox(frame, listvariable=self.todo_list_names)
        items_list_box.bind("<<ListboxSelect>>", lambda s: self.select_item(items_list_box.curselection()))
        items_list_box.grid(column=1, row=2, sticky=(tk.E, tk.W), padx=25, pady=1)

        # Configure Description Label
        self.selected_description = tk.StringVar()
        selected_description_label = tk.Label(frame, textvariable=self.selected_description, wraplength=200)
        selected_description_label.grid(column=1, row=3, sticky=(tk.E, tk.W))

        # Configure New Item Label
        new_item_label = tk.Label(frame_new_item, text="Create New Item", font="Helvetica 10 bold")
        new_item_label.grid(column=1, row=1, sticky=(tk.S, tk.W), padx=25, pady=10)

        # Configure Name Entry Label and Entry
        name_label = tk.Label(frame_new_item, text="Item name")
        name_label.grid(column=1, row=2, sticky=(tk.S, tk.W), padx=25, pady=1)

        self.name = tk.StringVar()
        name_entry = tk.Entry(frame_new_item, textvariable=self.name)
        name_entry.grid(column=1, row=3, sticky=(tk.N, tk.E, tk.W), padx=25, pady=1)

        # Configure Description Entry Label and Entry
        description_label = tk.Label(frame_new_item, text="Item description")
        description_label.grid(column=1, row=4, sticky=(tk.S, tk.W), padx=25, pady=1)

        self.description = tk.StringVar()
        description_entry = tk.Entry(frame_new_item, textvariable=self.description)
        description_entry.grid(column=1, row=5, sticky=(tk.N, tk.E, tk.W), padx=25, pady=2)

        # Configure Save Button
        save_button = tk.Button(frame_new_item, text="Save Item", command=self.save_item)
        save_button.grid(column=1, row=6, sticky=(tk.S, tk.E), pady=15, padx=25)

    # Run Function
    def run(self):
        self.root.mainloop()

    # Press Button Function
    def press_button(self):
        pass

    # Select Item Function
    def select_item(self, index):
        self.selected_description.set(self.todo_list_items[index[0]].description)

    # Save Item Function
    def save_item(self):
        name = self.name.get()
        description = self.description.get()
        new_item = TodoItem(name, description)
        self.todo_list_items.append(new_item)
        self.todo_list_names.set(list(map(lambda x: x.name, self.todo_list_items)))
# END TODOLIST-APP CLASS
