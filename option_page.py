import customtkinter as ctk
from PIL import ImageTk,Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# root window
root = ctk.CTk()
root.geometry("450x500")
root.title("TIC-TAC-TOE")
icon = ImageTk.PhotoImage(Image.open(r"C:\Users\rachi\2year_vac\pygame\ttt\tic-tac-toe.png"))
root.iconphoto(False,icon)
root.resizable(0,0)

    

# frame to select mode
mode_frame = ctk.CTkFrame(root,fg_color="transparent")
mode_frame.pack(pady = 150)

# call game window on choice
def pl1x():
    pass

def pl1o():
    pass

# Select first move
def selctmove():
    mode_frame.pack_forget()
    move_frame = ctk.CTkFrame(root,fg_color="transparent")
    move_frame.pack(pady = 150)

    pl1 = ctk.CTkLabel(move_frame,text="Player 1 Choose:-",font=('Times New Roman',24))
    pl1.pack(pady = 5)

    choicex = ctk.CTkButton(move_frame,text="X",font=('Times New Roman',24),command=pl1x)
    choicex.pack(pady = 20)
    choiceo = ctk.CTkButton(move_frame,text="O",font=('Times New Roman',24),command=pl1o)
    choiceo.pack(pady = 20)


# two player
tpl = ctk.CTkButton(mode_frame,text="2 Player Mode",corner_radius=5,command=selctmove)
tpl.pack(pady = 20)

# single player
spl = ctk.CTkButton(mode_frame,text="Single Player Mode",corner_radius=5,command=selctmove)
spl.pack(pady = 20)


root.mainloop()