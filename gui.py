import tkinter
window = tkinter.Tk()
window.title("GUI")
window.geometry('200x150')

tkinter.Button(window, text = "Button").pack()

# window.geometry()
window.mainloop()