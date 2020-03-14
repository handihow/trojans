import tkinter as tk
from tkinter import messagebox
from database import Database
from simulation import Simulation

# Instantiate database object
db = Database('Astronomical_Objects.db')


# Main Application/GUI class


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Astronomical Objects Manager')
        # Width height
        master.geometry("700x350")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial list
        self.populate_list()

    def create_widgets(self):
        # Name
        self.name_text = tk.StringVar()
        self.name_label = tk.Label(
            self.master, text='Object Name', font=('bold', 14), pady=10)
        self.name_label.grid(row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, textvariable=self.name_text)
        self.name_entry.grid(row=0, column=1)
        # Mass
        self.mass_text = tk.StringVar()
        self.mass_label = tk.Label(
            self.master, text='Mass [kg]', font=('bold', 14))
        self.mass_label.grid(row=0, column=2, sticky=tk.W)
        self.mass_entry = tk.Entry(self.master, textvariable=self.mass_text)
        self.mass_entry.grid(row=0, column=3)
        # Radius
        self.radius_text = tk.StringVar()
        self.radius_label = tk.Label(
            self.master, text='Radius [m]', font=('bold', 14), pady=10)
        self.radius_label.grid(row=1, column=0, sticky=tk.W)
        self.radius_entry = tk.Entry(
            self.master, textvariable=self.radius_text)
        self.radius_entry.grid(row=1, column=1)
        # Color
        self.color_text = tk.StringVar()
        self.color_label = tk.Label(
            self.master, text='Color', font=('bold', 14))
        self.color_label.grid(row=1, column=2, sticky=tk.W)
        self.color_entry = tk.Entry(self.master, textvariable=self.color_text)
        self.color_entry.grid(row=1, column=3)
        # Position
        self.pos_text_x = tk.StringVar()
        self.pos_text_y = tk.StringVar()
        self.pos_text_z = tk.StringVar()
        self.pos_label = tk.Label(
            self.master, text='Position [m] (x,y,z)', font=('bold', 14), pady=10)
        self.pos_label.grid(row=2, column=0, sticky=tk.W)
        self.pos_entry_x = tk.Entry(
            self.master, textvariable=self.pos_text_x)
        self.pos_entry_y = tk.Entry(
            self.master, textvariable=self.pos_text_y)
        self.pos_entry_z = tk.Entry(
            self.master, textvariable=self.pos_text_z)
        self.pos_entry_x.grid(row=2, column=1)
        self.pos_entry_y.grid(row=2, column=2)
        self.pos_entry_z.grid(row=2, column=3)
        # Velocity
        self.velocity_text_x = tk.StringVar()
        self.velocity_text_y = tk.StringVar()
        self.velocity_text_z = tk.StringVar()
        self.velocity_label = tk.Label(
            self.master, text='Velocity [ms-1] (x,y,z)', font=('bold', 14), pady=10)
        self.velocity_label.grid(row=3, column=0, sticky=tk.W)
        self.velocity_entry_x = tk.Entry(
            self.master, textvariable=self.velocity_text_x)
        self.velocity_entry_y = tk.Entry(
            self.master, textvariable=self.velocity_text_y)
        self.velocity_entry_z = tk.Entry(
            self.master, textvariable=self.velocity_text_z)
        self.velocity_entry_x.grid(row=3, column=1)
        self.velocity_entry_y.grid(row=3, column=2)
        self.velocity_entry_z.grid(row=3, column=3)
        # Trail
        self.trail_bool = tk.BooleanVar()
        self.trail_btn = tk.Checkbutton(text='Trail?', variable=self.trail_bool)
        self.trail_btn.grid(row=4, column=0, pady=10)
        # Simulate
        self.simulate_bool = tk.BooleanVar()
        self.simulate_btn = tk.Checkbutton(text='Simulate?', variable=self.simulate_bool)
        self.simulate_btn.grid(row=4, column=1)
        # Simulation button
        self.simulation_btn = tk.Button(self.master, text="Simulate", width=12, command=self.simulate)
        self.simulation_btn.grid(row=4, column=2)
        # Astronomical Objects list (listbox)
        self.astronomical_objects_list = tk.Listbox(self.master, height=8, width=50, border=0)
        self.astronomical_objects_list.grid(row=6, column=0, columnspan=3,
                                            rowspan=6, pady=10, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=6, column=3)
        # Set scrollbar to parts
        self.astronomical_objects_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.astronomical_objects_list.yview)

        # Bind select
        self.astronomical_objects_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons
        self.add_btn = tk.Button(
            self.master, text="Add Object", width=12, command=self.add_item)
        self.add_btn.grid(row=5, column=0, pady=10)

        self.remove_btn = tk.Button(
            self.master, text="Remove Object", width=12, command=self.remove_item)
        self.remove_btn.grid(row=5, column=1)

        self.update_btn = tk.Button(
            self.master, text="Update Object", width=12, command=self.update_item)
        self.update_btn.grid(row=5, column=2)

        self.exit_btn = tk.Button(
            self.master, text="Clear Input", width=12, command=self.clear_text)
        self.exit_btn.grid(row=5, column=3)

    def populate_list(self):
        # Delete items before update.
        # So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.astronomical_objects_list.delete(0, tk.END)
        # Loop through records
        for row in db.fetch():
            # Insert into list
            self.astronomical_objects_list.insert(tk.END, row)

    # Add new item
    def add_item(self):
        print('adding')
        if self.name_text.get() == '' or self.mass_text.get() == '' or self.radius_text.get() == '' \
                or self.color_text.get() == '' or self.pos_text_x.get() == '' or self.pos_text_y.get() == '' \
                or self.pos_text_z.get() == '' or self.velocity_text_x.get() == '' or self.velocity_text_y.get() == '' \
                or self.velocity_text_z.get() == '':
            messagebox.showerror(
                "Required Fields", "Please include all fields")
            return
        print(self.name_text.get())
        # Insert into DB
        db.insert(self.name_text.get(), self.pos_text_x.get(), self.pos_text_y.get(), self.pos_text_z.get(),
                  self.radius_text.get(), self.color_text.get(), self.mass_text.get(), self.velocity_text_x.get(),
                  self.velocity_text_y.get(), self.velocity_text_z.get(), self.trail_bool.get(),
                  self.simulate_bool.get())
        # Clear list
        self.astronomical_objects_list.delete(0, tk.END)
        # Insert into list
        self.astronomical_objects_list.insert(tk.END, (self.name_text.get(), self.pos_text_x.get(),
                                                       self.pos_text_y.get(), self.pos_text_z.get(),
                                                       self.radius_text.get(), self.color_text.get(),
                                                       self.mass_text.get(), self.velocity_text_x.get(),
                                                       self.velocity_text_y.get(), self.velocity_text_z.get(),
                                                       self.trail_bool.get(), self.simulate_bool.get()))
        self.clear_text()
        self.populate_list()

    # Runs when item is selected
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.astronomical_objects_list.curselection()[0]
            # Get selected item
            self.selected_item = self.astronomical_objects_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item[1])
            self.mass_entry.delete(0, tk.END)
            self.mass_entry.insert(tk.END, self.selected_item[7])
            self.radius_entry.delete(0, tk.END)
            self.radius_entry.insert(tk.END, self.selected_item[5])
            self.color_entry.delete(0, tk.END)
            self.color_entry.insert(tk.END, self.selected_item[6])
            self.pos_entry_x.delete(0, tk.END)
            self.pos_entry_x.insert(tk.END, self.selected_item[2])
            self.pos_entry_y.delete(0, tk.END)
            self.pos_entry_y.insert(tk.END, self.selected_item[3])
            self.pos_entry_z.delete(0, tk.END)
            self.pos_entry_z.insert(tk.END, self.selected_item[4])
            self.velocity_entry_x.delete(0, tk.END)
            self.velocity_entry_x.insert(tk.END, self.selected_item[8])
            self.velocity_entry_y.delete(0, tk.END)
            self.velocity_entry_y.insert(tk.END, self.selected_item[9])
            self.velocity_entry_z.delete(0, tk.END)
            self.velocity_entry_z.insert(tk.END, self.selected_item[10])
            self.trail_bool.set(self.selected_item[11])
            self.simulate_bool.set(self.selected_item[12])

        except IndexError:
            pass

    # Remove item
    def remove_item(self):
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item
    def update_item(self):
        print('updating')
        db.update(self.selected_item[0], self.name_text.get(), self.pos_text_x.get(),
                  self.pos_text_y.get(), self.pos_text_z.get(),
                  self.radius_text.get(), self.color_text.get(),
                  self.mass_text.get(), self.velocity_text_x.get(),
                  self.velocity_text_y.get(), self.velocity_text_z.get(),
                  self.trail_bool.get(), self.simulate_bool.get())
        self.populate_list()

    # Clear all text fields
    def clear_text(self):
        print('clearing')
        self.name_entry.delete(0, tk.END)
        self.mass_entry.delete(0, tk.END)
        self.radius_entry.delete(0, tk.END)
        self.color_entry.delete(0, tk.END)
        self.pos_entry_x.delete(0, tk.END)
        self.pos_entry_y.delete(0, tk.END)
        self.pos_entry_z.delete(0, tk.END)
        self.velocity_entry_x.delete(0, tk.END)
        self.velocity_entry_y.delete(0, tk.END)
        self.velocity_entry_z.delete(0, tk.END)
        self.trail_bool.set(False)
        self.simulate_bool.set(False)

    # Simulate
    def simulate(self):
        astronomical_object_data = db.fetch()
        Simulation(astronomical_object_data, 2)

#
root = tk.Tk()
app = Application(master=root)
app.mainloop()
