import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk
from PIL import Image

# Set custom tkinter defaults
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Initialize app
root = ctk.CTk()
root.geometry("300x375")
root.title("Free Image Compression")

def LoadAppCanvas():
    
    # Set text labels for entry fields
    ctk.CTkLabel(canvas, text="Input: ").place(relx=0.1,rely=0.1)
    ctk.CTkLabel(canvas, text="Output: ").place(relx=0.075,rely=0.18)
    ctk.CTkLabel(canvas, text="Quality: ").place(relx=0.075,rely=0.26)
    ctk.CTkLabel(canvas, text="Format: ").place(relx=0.075,rely=0.34)
    
    # Add Glorious Logo
    Bingus = ctk.CTkImage(light_image=Image.open("assets/bingus_bg.jpg"),size=(100,120))
    BingusHatched = ctk.CTkLabel(canvas, image=Bingus, text="", fg_color="transparent")
    BingusHatched.place(relx=0.3,rely=0.65)
    
    # Entry widget - Path to image file
    ImgNameInput = ctk.StringVar()
    ImgNameInput.set("Enter file-path to image...")
    ImgInput = ctk.CTkEntry(canvas,
                            width=170,
                            textvariable=ImgNameInput,
                            text_color="#808080")
    ImgInput.place(relx=0.25,rely=0.1)

    # Entry widget - Name of new file
    ImgNameOutput= ctk.StringVar()
    ImgNameOutput.set("Enter save-path for image...")
    ImgOutput = ctk.CTkEntry(canvas,
                             width=170,
                             textvariable=ImgNameOutput,
                             text_color="#808080")
    ImgOutput.place(relx=0.25,rely=0.18)
    
    # Scale widget - CompressPct
    ScaleValue = ctk.IntVar()
    CompressScale = ctk.CTkSlider(canvas, variable=ScaleValue, from_=0, to=100, number_of_steps=100)
    CompressScale.place(relx=0.25,rely=0.275)
    
    # OptionMenu widget - Format
    FormatEntry = ctk.StringVar()
    FormatEntry.trace_add("write", lambda *args: print(FormatEntry.get()))
    FormatMenu = ctk.CTkOptionMenu(canvas,
                               variable=FormatEntry,
                               values=["PNG", "JPEG", "EPS"]).place(relx=0.25,rely=0.35)
    FormatEntry.set("PNG") #Set default value

    def lossy_compress():
        # Collect arguments from user input
        ## Input file
        Img = ImgInput.get()
        Img = Img.replace("\\","/")
        
        ## Input format
        ImgFormat = FormatEntry.get()
        
        ## Input Quality
        CompressPct = ScaleValue.get()
        if CompressPct == 0:
            CompressPctScaled = 0
        else:
            CompressPctScaled = round((95 * CompressPct)/100)
        
        ## Input save-path
        FileName=ImgOutput.get()
        FileName=FileName.replace("\\","/")
        
        # Open image to be compressed
        image = Image.open(Img)
        
        # Save under different quality
        image.save(fp=FileName,
                   format = ImgFormat,
                   optimize = True,
                   quality = CompressPctScaled)
        
    #Submit button
    ctk.CTkButton(canvas, 
          text='Submit', 
          command=lambda: lossy_compress()).place(relx=0.25,rely=0.5)
          
canvas = ctk.CTkFrame(root, width=300,height=375)
canvas.pack(fill="both", expand=1, pady=4, padx=4)

LoadAppCanvas()

root.mainloop()