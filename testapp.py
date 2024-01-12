import tkinter as tk
from PIL import ImageTk
from PIL import Image

# Parameters
bgcolor = "#d5ab82"

# Initialize app
root = tk.Tk()
root.title("Free Image Compression")

# Functions
def load_frame1():
    frame1.pack_propagate(False) #Prevents child, logo element from modifying parent, frame element.

    # Logo widget
    logo_img = ImageTk.PhotoImage(file="assets/logo_bingus.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bgcolor)
    logo_widget.image = logo_img
    logo_widget.pack()

    # Text widget
    tk.Label(frame1,
            text="A free, ligthweight, image compression &\n resizing program",
            bg=bgcolor,
            fg="white",
            font=("TkMenuFont", 14)
            ).pack()

    #Button Widget
    tk.Button(
        frame1,
        text="BINGUS",
        font=("TkHeadingFont", 20),
        bg = "#28393a",
        fg = "white",
        cursor = "hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame2()).pack(pady=20)

def load_frame2():
    print("All hail Bingus")

#root.eval("tk::PlaceWindow . center")
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry("600x800+" + str(x) + "+" + str(y))

# Settings
frame1 = tk.Frame(root, width=600, height=800, bg=bgcolor)
frame2 = tk.Frame(root, bg=bgcolor)
for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

load_frame1()

#run app
root.mainloop()