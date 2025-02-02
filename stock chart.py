import tkinter as tk
import tkinter.font as tkfont
class GUI():
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("depot charts")
        self.root.attributes("-fullscreen", True)
        self.root.bind("<Escape>", lambda event: self.root.attributes("-fullscreen", False))
        
        self.operation = tk.Frame(self.root, bg= "#4C747A", bd= 1, width=300)
        self.window= tk.Frame(self.root, bg= "#8F8F8F", width=400)
        
        self.operation.pack(side="left", fill= "y")

        self.create_buttons()
        self.window.pack(padx= 4, pady= 4, side="right", fill= "both", expand= True)
        self.root.mainloop()
    def create_buttons(self):
        self.buttons = ["piechart", "account balance"]
        font = tkfont.Font()
        self.max_width = max(font.measure(i) for i in self.buttons)
        av_width = font.measure("w")
        self.button_width = self.max_width//av_width + 2
        for i in range(len(self.buttons)):
            btn = tk.Button(self.operation, text=self.buttons[i], width= self.button_width)
            btn.grid(row=i, column=0, padx= 5, pady=5)

GUI()