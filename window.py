import tkinter as tk
from tkinter import Toplevel, PhotoImage
from PIL import ImageTk, Image
import Floor_PlannerGUI as sc  # Import the second code as a module


def btn_clicked():
    # Open the second page (SecondPage class) as a pop-up window
    second_window = Toplevel(window)
    second_page = sc.FloorPlannerGUI(second_window)


window = tk.Tk()
window.geometry("1000x600")
window.configure(bg="#2a3950")

canvas = tk.Canvas(
    window,
    bg="#2a3950",
    height=600,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.pack()

img1 = PhotoImage(file="img1.png")
canvas.create_image(500, 250, image=img1)

img0 = PhotoImage(file="img0.png")
b0 = tk.Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,  # Call the function to open the second page
    relief="flat")
b0.pack()

b0.place(
    x=189, y=473,
    width=308,
    height=77)

window.resizable(False, False)
window.mainloop()