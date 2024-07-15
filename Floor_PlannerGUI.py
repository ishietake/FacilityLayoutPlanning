import tkinter as tk
from tkinter.constants import E, EW, N, S, W, NSEW
from PIL import ImageTk, Image

import Floor_Planner as fp
from Log import Logger

class FloorPlannerGUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        
        self.mainFrame = tk.Frame(self)
        self.mainFrame.config(bg="#2a3950")
        self.mainFrame.pack()
        
        self.mainFrameContents()
        self.logfile = Logger()
    
    def mainFrameContents(self):
        row = 0
        self.floor_size_label = tk.Label(self.mainFrame, text="Floor Size", fg="#ffffff", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.floor_size_label.grid(row=row, columnspan=4, sticky=N)
        
        row = 1
        self.rows_label = tk.Label(self.mainFrame, fg="#355C7D", bg="#2a3950", font=("Lalezar-Regular", int(25.0)), text="Rows:")
        self.rows_label.grid(row=row, column=0)
        
        self.rows_entry = tk.Entry(self.mainFrame)
        self.rows_entry.grid(row=row, column=1)
        self.rows_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        self.col_label = tk.Label(self.mainFrame, fg="#C56C86", bg="#2a3950", font=("Lalezar-Regular", int(25.0)), text="Columns:")
        self.col_label.grid(row=row, column=2)
        
        self.col_entry = tk.Entry(self.mainFrame)
        self.col_entry.grid(row=row, column=3)
        self.col_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        row = 2
        tk.Label(self.mainFrame, text=" ", bg="#2a3950",).grid(row=row)
        
        row = 3
        self.entrance_label = tk.Label(self.mainFrame, text="Entrance Coordinates", fg="white", bg="#2a3950", font = ("Lalezar-Regular", int(25.0)))
        self.entrance_label.grid(row=row, columnspan=4, sticky=N)
        
        row = 4
        self.entrance_x_label = tk.Label(self.mainFrame, fg="#355C7D", bg="#2a3950", font=("Lalezar-Regular", int(25.0)), text="X:")
        self.entrance_x_label.grid(row=row, column=0)
        
        self.entrance_x = tk.Entry(self.mainFrame)
        self.entrance_x.grid(row=row, column=1)
        self.entrance_x.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        self.entrance_y_label = tk.Label(self.mainFrame, text="Y:",  fg="#C56C86", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.entrance_y_label.grid(row=row, column=2)
        
        self.entrance_y = tk.Entry(self.mainFrame)
        self.entrance_y.grid(row=row, column=3)
        self.entrance_y.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        row = 5
        tk.Label(self.mainFrame, text=" ", bg="#2a3950",).grid(row=row)

        row = 6
        self.create_room_label = tk.Label(self.mainFrame, text="Create Room", fg="white", bg="#2a3950", font = ("Lalezar-Regular", int(25.0)))
        self.create_room_label.grid(row=row, columnspan=4, sticky=N)
        
        row = 7
        self.width_label = tk.Label(self.mainFrame, fg="#355C7D", bg="#2a3950", font=("Lalezar-Regular", int(25.0)), text="Width:")
        self.width_label.grid(row=row, column=0)
        
        self.width_entry = tk.Entry(self.mainFrame)
        self.width_entry.grid(row=row, column=1)
        self.width_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        self.height_label = tk.Label(self.mainFrame, text="Height:",  fg="#C56C86", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.height_label.grid(row=row, column=2)
        
        self.height_entry = tk.Entry(self.mainFrame)
        self.height_entry.grid(row=row, column=3)
        self.height_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        row = 8
        self.room_label = tk.Label(self.mainFrame, fg="#355C7D", bg="#2a3950", font=("Lalezar-Regular", int(25.0)), text="Name:")
        self.room_label.grid(row=row, column=0)
        
        self.room_name_entry = tk.Entry(self.mainFrame)
        self.room_name_entry.grid(row=row, column=1)
        self.room_name_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        self.color_label = tk.Label(self.mainFrame, text="Color:",  fg="#C56C86", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.color_label.grid(row=row, column=2)
        
        self.color_entry = tk.Entry(self.mainFrame)
        self.color_entry.grid(row=row, column=3)
        self.color_entry.config(width=15, background="light gray", fg="black", font=("Lalezar-Regular"))
        
        row = 9    
        img = Image.open("img7.png")
        resized_img = img.resize((20, 20), Image.Resampling.LANCZOS)
        img7 = ImageTk.PhotoImage(resized_img)
        self.remove_room_button = tk.Button(self.mainFrame, image=img7, command=self.remove_room)
        self.remove_room_button.photo = img7
        self.remove_room_button.grid(row=row, column=0, sticky=E)
        
        img = Image.open("img8.png")
        resized_img = img.resize((20, 20), Image.Resampling.LANCZOS)
        img8 = ImageTk.PhotoImage(resized_img)
        self.add_room_button = tk.Button(self.mainFrame, image=img8, command=self.add_room)
        self.add_room_button.photo = img8
        self.add_room_button.grid(row=row, column=3, sticky=W)
        
        self.created_rooms = ['No Rooms Yet']
        self.room_name = tk.StringVar()
        self.room_name.set(self.created_rooms[0])
        
        self.drop_down = tk.OptionMenu(self.mainFrame, self.room_name, *self.created_rooms)
        self.drop_down.grid(row=row, column=1, columnspan=2)
        self.drop_down.config(width=25, activebackground="gray", background="#353d7d", fg="white", font=("Lalezar-Regular", int(10.0)))
        
        row = 10
        tk.Label(self.mainFrame, text=" ", bg="#2a3950",).grid(row=row)
        
        row = 11
        self.sort_rooms_label = tk.Label(self.mainFrame, text="Sort",  fg="#355C7D", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.sort_rooms_label.grid(row=row, column=0)
        
        self.options = ["None", "Ascending", "Descending"]
        self.options_variable = tk.StringVar()
        self.options_variable.set(self.options[0])
        
        self.sort_rooms_drop_down = tk.OptionMenu(self.mainFrame, self.options_variable, *self.options)
        self.sort_rooms_drop_down.config(activebackground="gray", background="#353d7d", fg="white", font=("Lalezar-Regular", int(10.0)))
        self.sort_rooms_drop_down.grid(row=row, column=1, sticky=W)
        
        self.randomize_rooms_label = tk.Label(self.mainFrame, text="Randomize",  fg="#C56C86", bg="#2a3950", font=("Lalezar-Regular", int(25.0)))
        self.randomize_rooms_label.grid(row=row, column=2)
        
        self.randomize_bool = tk.BooleanVar()
        self.randomize_bool.set(False)
        
        self.randomize_rooms = tk.Button(self.mainFrame, text="False", command=lambda:[(self.randomize_rooms.config(text="True") if self.randomize_bool.get() is False else self.randomize_rooms.config(text="False")), (self.randomize_bool.set(True) if self.randomize_bool.get() == False else self.randomize_bool.set(False))])
        self.randomize_rooms.config(background="#353d7d", fg="white", font=("Lalezar-Regular"), width=10, height=2)
        self.randomize_rooms.grid(row=row, column=3)
        
        row = 12
        img = Image.open("img12.png")
        resized_img = img.resize((200, 50), Image.Resampling.LANCZOS)
        img12 = ImageTk.PhotoImage(resized_img)
        self.create_button = tk.Button(self.mainFrame, image=img12, command=self.create_grid)
        self.create_button.photo = img12
        self.create_button.grid(row=row, columnspan=4, pady=10, sticky=S)
        
        
        row = 13
        self.log_toggle = tk.BooleanVar()
        self.log_toggle.set(False)
        
        self.log_button = tk.Button(self.mainFrame, text="❌", bg="red", command=lambda:[(self.log_button.config(text="✔", bg="green") if self.log_toggle.get() == False else self.log_button.config(text="❌", bg="red")), (self.log_toggle.set(True) if self.log_toggle.get() == False else self.log_toggle.set(False)), self.enable_logging()])
        self.log_button.grid(row=row, column=0, sticky=W)
        
    def enable_logging(self):
        if self.logfile.enabled == True:
            self.logfile.enabled = False
            print(self.logfile.enabled)
        else:
            self.logfile.enabled = True
            print(self.logfile.enabled)
    
    def add_room(self):
        new_room = fp.Room(int(self.width_entry.get()), int(self.height_entry.get()), self.color_entry.get(), self.room_name_entry.get())

        if "No Rooms Yet" in self.created_rooms:
            self.created_rooms.remove("No Rooms Yet")

        self.created_rooms.append(new_room)

        # Update the OptionMenu with the new list of room names
        self.drop_down["menu"].delete(0, "end")  # Remove all items from the menu

        for room in self.created_rooms:
            self.drop_down["menu"].add_command(label=f"{room.name, room.symbol}", command=tk._setit(self.room_name, room.name))

        # Set the selection to the newly created room
        self.room_name.set(new_room.name)
        self.logfile.log(f"Room Created: with Name: '{self.room_name_entry.get()}', Color: '{self.color_entry.get()}' W: '{self.width_entry.get()}' and H: '{self.height_entry.get()}'")
    
    def remove_room(self):
        selected_room_name = self.room_name.get()

        if selected_room_name != "No Rooms Yet":
            for room in self.created_rooms:
                if room.name == selected_room_name:
                    self.logfile.log(f"Room Deleted: with Name: '{room.name}', Color: '{room.symbol}' W: '{room.width}' and H: '{room.height}'")
                    self.created_rooms.remove(room)
                    break

            # Update the OptionMenu with the new list of room names
            self.drop_down["menu"].delete(0, "end")  # Remove all items from the menu

            if not self.created_rooms:  # If the list is empty after removing the room, add "No Rooms Yet" back
                self.created_rooms.append("No Rooms Yet")
                self.room_name.set("No Rooms Yet")
            else:
                for room in self.created_rooms:
                    self.drop_down["menu"].add_command(label=f"{room.name, room.symbol}", command=tk._setit(self.room_name, room.name))

                # Set the selection to the first room in the list
                self.room_name.set(self.created_rooms[0].name)
            
    def create_grid(self):
        Floor = fp.FloorPlan(int(self.rows_entry.get()), int(self.col_entry.get()), int(self.entrance_x.get()), int(self.entrance_y.get()), self.created_rooms, self.options_variable.get(), self.randomize_bool.get(), self.logfile)
        self.logfile.log(f"Floor size created with: {self.rows_entry.get()} row/s, {self.col_entry.get()} column/s")
        
        
        self.frame = tk.Tk()
        self.frame.title("Grid")
        
        if len(Floor.rooms) != 0:
            try:
                rows = int(self.rows_entry.get())
                cols = int(self.col_entry.get())
                if rows > 0 and cols > 0:
                    # Create the new grid
                    for r in range(rows):
                        for c in range(cols):
                            # Make all cells perfect squares
                            cell_frame = tk.Frame(self.frame, width=50, height=50, borderwidth=1, relief="solid")
                            cell_frame.grid(row=r, column=c, padx=1, pady=1, sticky=NSEW)
                            cell_frame.config(background=f"{Floor.grid[r][c] if Floor.grid[r][c] == 'black' else (Floor.grid[r][c].symbol if isinstance(Floor.grid[r][c], fp.Room) else 'white')}")
                            self.logfile.log(f"Creating cells. Currently at cell R:{r} C:{c}")
                            
                            # Configure row and column weights to make the cells expand evenly
                            self.frame.grid_rowconfigure(r, weight=1)
                            self.frame.grid_columnconfigure(c, weight=1)
                else:
                    print("Invalid input! Rows and columns must be positive integers.")
            except ValueError:
                print("Invalid input! Please enter positive integers for rows and columns.")
        else:
            cell_frame = tk.Label(self.frame, text="No valid arrangement found")
            cell_frame.pack()
        
        if self.log_toggle.get():
            self.logfile.create_logfile()
        
root = tk.Tk()
root.minsize(490, 512)
root.config(bg="#2a3950")
root.winfo_toplevel().title("LayoutTopia")

main = FloorPlannerGUI(root)
main.mainloop()