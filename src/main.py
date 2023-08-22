import tkinter as tk

def setup():
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    for i in range(0,10):
        button = tk.Button(window,text=str(i))
        button .pack()
    window.mainloop()

def main():
    setup()



if __name__ == '__main__':
    main()