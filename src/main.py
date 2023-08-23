import tkinter as tk

def setup():
    window = tk.Tk()
    text_box = tk.Entry(window,width=50) 
    text_box.pack()
    button_0 = tk.Button(window,text='0',width=10,command=lambda: text_box.insert(tk.END,'0'))
    button_1 = tk.Button(window,text='1',width=10,command=lambda: text_box.insert(tk.END,'1'))
    button_2 = tk.Button(window,text='2',width=10,command=lambda: text_box.insert(tk.END,'2'))
    button_3 = tk.Button(window,text='3',width=10,command=lambda: text_box.insert(tk.END,'3'))
    button_4 = tk.Button(window,text='4',width=10,command=lambda: text_box.insert(tk.END,'4'))
    button_5 = tk.Button(window,text='5',width=10,command=lambda: text_box.insert(tk.END,'5'))
    button_6 = tk.Button(window,text='6',width=10,command=lambda: text_box.insert(tk.END,'6'))
    button_7 = tk.Button(window,text='7',width=10,command=lambda: text_box.insert(tk.END,'7'))
    button_8 = tk.Button(window,text='8',width=10,command=lambda: text_box.insert(tk.END,'8'))
    button_9 = tk.Button(window,text='9',width=10,command=lambda: text_box.insert(tk.END,'9'))
    button_0.pack()
    button_1.pack()
    button_2.pack()
    button_3.pack()
    button_4.pack()
    button_5.pack()
    button_6.pack()
    button_7.pack()
    button_8.pack()
    button_9.pack()
    button_add = tk.Button(window,text='+',width=10,command=lambda: text_box.insert(tk.END,'+'))
    button_sub = tk.Button(window,text='-',width=10,command=lambda: text_box.insert(tk.END,'-'))
    button_eq = tk.Button(window,text='=',width=10,command=lambda: text_box.insert(tk.END,'='))
    button_add.pack()
    button_sub.pack()
    button_eq.pack()
    clear_button = tk.Button(window,text='Clear',width=10,command=lambda: text_box.delete(0,tk.END))
    clear_button.pack()
    window.mainloop()   


def str_analyzer(str):
    return None

def main():
    setup()



if __name__ == '__main__':
    main()