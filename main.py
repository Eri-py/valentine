from customtkinter import *
from PIL import ImageTk, Image
from random import randint
import customtkinter


customtkinter.set_appearance_mode("system")
root = CTk()
screenWidth = root.winfo_screenwidth()
screenHeight =root.winfo_screenheight()
appWidth = 600
appHeight =400
x = (screenWidth/2) - (appWidth/2)
y = (screenHeight/2) - (appHeight/2 +200)
root.geometry(f"{appWidth}x{appHeight}+{int(x)}+{int(y)}")

class mainWindowClass:
    def __init__(self, master=None, **kwargs):
        # Create a canvas
        mainWindow = CTkCanvas(root, bg="white")
        mainWindow.grid(row=0, column=0, sticky="nsew")

        # functions
        def moveNo():
            x = randint(0, 5)
            y = randint(0, 5)
            if x == 3 and y == 1:
                x = 0
                y = 4
            elif x == 1 and y == 3:
                x = 0
                y = 4
            else:
                noButton.grid(row=x, column=y)

        def yesClick():
            mainWindow.grid_remove()
            yesScreen()

        # image
        centerImage = Image.open(
            "C:/Users/eriol/OneDrive/Desktop/P.project/valentine/image.jpg"
        ).resize((300, 250))
        centerImage = ImageTk.PhotoImage(centerImage)
        centerImageLabel = CTkLabel(master=mainWindow, image=centerImage, text="")
        centerImageLabel.grid(row=2, column=2, sticky="nsew", columnspan=2)

        # yes button
        yesImage = Image.open(
            "C:/Users/eriol/OneDrive/Desktop/P.project/valentine/yesButton.png"
        ).resize((25, 25))
        yesImage = ImageTk.PhotoImage(yesImage)
        yesButton = CTkButton(
            master=mainWindow,
            text="Yes",
            corner_radius=100,
            fg_color="red",
            hover_color="red",
            command=yesClick,
            image=yesImage,
            compound="left",
            anchor="center",
        )
        yesButton.grid(row=3, column=1)

        # no button
        noImage = Image.open(
            "C:/Users/eriol/OneDrive/Desktop/P.project/valentine/noButton.png"
        ).resize((25, 25))
        noImage = ImageTk.PhotoImage(noImage)
        noButton = CTkButton(
            master=mainWindow,
            text="No",
            text_color="Black",
            fg_color="white",
            hover_color="white",
            corner_radius=100,
            command=moveNo,
            border_width=2,
            border_color="red",
            image=noImage,
            compound="left",
            anchor="center",
        )
        noButton.grid(row=3, column=4)

        # main message
        message = CTkLabel(
            master=mainWindow,
            text="Do You Love Me??",
            font=(None, 25),
            text_color="black",
        )
        message.grid(row=1, column=3)

        # custom grid
        mainWindow.columnconfigure((0, 1, 3, 4, 5), weight=1)
        mainWindow.rowconfigure((0, 1, 3, 4, 5), weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)


class yesScreen:
    def __init__(self, master=None, **kwargs) -> None:
        mainWindow = CTkCanvas(master=root, bg="white")
        mainWindow.grid(row=0, column=0, sticky="nsew")

        # text widget
        yayLabel = CTkLabel(
            master=mainWindow, text="I love you too!! :)", text_color="black", font=(None, 25)
        )
        yayLabel.grid(row=1, column=3)

        # image
        centerImage = Image.open(
            "C:/Users/eriol/OneDrive/Desktop/P.project/valentine/yesGif.gif"
        ).resize((300, 250))
        centerImage = ImageTk.PhotoImage(centerImage)
        centerImageLabel = CTkLabel(master=mainWindow, image=centerImage, text="")
        centerImageLabel.grid(row=2, column=2, sticky="nsew", columnspan=2)

        # custom grid
        mainWindow.columnconfigure((0, 1, 3, 4, 5), weight=1)
        mainWindow.rowconfigure((0, 1, 3, 4, 5), weight=1)


mainWindowClass()

# window loop
root.mainloop()
