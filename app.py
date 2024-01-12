import tkinter as tk
from PIL import ImageTk
from PIL import Image

# Parameters
bgcolor = "#d5ab82"

# Initialize app
root = tk.Tk()
root.geometry("300x375")
root.title("Free Image Compression")

def LoadAppCanvas():
    canvas.pack_propagate(False) #Prevents child, logo element from modifying parent, frame element.
    
    tk.Label(canvas, text="Input").grid(row=1,padx=10)
    tk.Label(canvas, text="Output").grid(row=2, padx=10)
    tk.Label(canvas, text="Quality").grid(row=3, padx=10)
    tk.Label(canvas, text="Format").grid(row=4, padx=10)
    
    # Add Glorious Logo
    Bingus = ImageTk.PhotoImage(file="assets/bingus_resized.png")
    BingusHatched = tk.Label(canvas, image=Bingus, fg=bgcolor,bg=bgcolor)
    BingusHatched.image = Bingus
    BingusHatched.grid(row=0, column=1, sticky=tk.NW)
    
    # Entry widget - Path to image file
    ImgNameInput = tk.StringVar()
    ImgInput = tk.Entry(canvas, width=30, textvariable=ImgNameInput)
    ImgInput.insert(10, "Enter file-path to image")
    ImgInput.grid(row=1,
                  sticky=tk.NW,
                  column=1, 
                  pady=4,
                  padx=4)

    # Entry widget - Name of new file
    ImgNameOutput= tk.StringVar()
    ImgOutput = tk.Entry(canvas, width=30, textvariable=ImgNameOutput)
    ImgOutput.insert(10, "Enter save-path for new image")
    ImgOutput.grid(row=2,
                   sticky=tk.W,
                   column=1, 
                   pady=4,
                   padx=4)

    # Scale widget - CompressPct
    ScaleValue = tk.IntVar()
    CompressScale = tk.Scale(canvas, orient="horizontal", length=200, from_=0.0, to=100.0, variable=ScaleValue)
    CompressScale.grid(row=3,
                       sticky=tk.W,
                       column=1, 
                       pady=4,
                       padx=4)
    
    # OptionMenu widget - Format
    FormatEntry = tk.StringVar()
    FormatEntry.trace_add("write", lambda *args: print(FormatEntry.get()))
    FormatMenu = tk.OptionMenu(canvas,
                               FormatEntry,
                               "PNG",
                               "JPEG",
                               "EPS").grid(row=4,
                                    sticky=tk.W,
                                    column=1, 
                                    pady=4,
                                    padx=4) 
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
    tk.Button(canvas, 
          text='Submit', 
          command=lambda: lossy_compress()).grid(row=5, 
                                    column=1, 
                                    sticky=tk.W, 
                                    pady=10,
                                    padx=4)
          


canvas = tk.Frame(root, width=300,height=375,relief="sunken", bg=bgcolor)
canvas.pack(fill="both", expand=1, pady=4, padx=4)

LoadAppCanvas()

root.mainloop()