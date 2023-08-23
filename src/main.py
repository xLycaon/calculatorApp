import tkinter as tk



#TODO: place the buttons in the correct positions
#TODO: add functionality to the buttons
#TODO: the size of the text in the text box should be the same height as the text box
#TODO: string analyzer function
#TODO: transform this program into an executable file


def setup():
    #create the Window
    window = tk.Tk()
    window.geometry('650x300')
    window.title('Calculator')


    #Create the buttons and text box
    text_box_1 = tk.Text(window,width=80,height=5)
    button_0 = tk.Button(window,text='0',width=30,command=lambda: text_box_1.insert(tk.END,'0'))
    button_1 = tk.Button(window,text='1',width=15,command=lambda: text_box_1.insert(tk.END,'1'))
    button_2 = tk.Button(window,text='2',width=15,command=lambda: text_box_1.insert(tk.END,'2'))
    button_3 = tk.Button(window,text='3',width=15,command=lambda: text_box_1.insert(tk.END,'3'))
    button_4 = tk.Button(window,text='4',width=15,command=lambda: text_box_1.insert(tk.END,'4'))
    button_5 = tk.Button(window,text='5',width=15,command=lambda: text_box_1.insert(tk.END,'5'))
    button_6 = tk.Button(window,text='6',width=15,command=lambda: text_box_1.insert(tk.END,'6'))
    button_7 = tk.Button(window,text='7',width=15,command=lambda: text_box_1.insert(tk.END,'7'))
    button_8 = tk.Button(window,text='8',width=15,command=lambda: text_box_1.insert(tk.END,'8'))
    button_9 = tk.Button(window,text='9',width=15,command=lambda: text_box_1.insert(tk.END,'9'))
    button_add = tk.Button(window,text='+',width=15,command=lambda: text_box_1.insert(tk.END,'+'))
    button_sub = tk.Button(window,text='-',width=15,command=lambda: text_box_1.insert(tk.END,'-'))
    button_eq = tk.Button(window,text='=',width=15,command=lambda: text_box_1.insert(tk.END,'='))
    button_mul = tk.Button(window,text='*',width=15,command=lambda: text_box_1.insert(tk.END,'*'))
    button_div = tk.Button(window,text='/',width=15,command=lambda: text_box_1.insert(tk.END,'/'))
    button_per = tk.Button(window,text='%',width=15,command=lambda: text_box_1.insert(tk.END,'%'))
    button_del = tk.Button(window,text='del',width=15,command=lambda: text_box_1.delete(len(text_box_1.get())-1))
    clear_button = tk.Button(window,text='Clear',width=15,command=lambda: text_box_1.delete(0,tk.END))

    
    #------------------ Layout ------------------
    button_0.grid(row=5,column=0,columnspan=2)
    button_1.grid(row=4,column=0)
    button_2.grid(row=4,column=1)
    button_3.grid(row=4,column=2)
    button_4.grid(row=3,column=0)
    button_5.grid(row=3,column=1)
    button_6.grid(row=3,column=2)
    button_7.grid(row=2,column=0)
    button_8.grid(row=2,column=1)
    button_9.grid(row=2,column=2)
    button_add.grid(row=2,column=3)
    button_sub.grid(row=3,column=3)
    button_eq.grid(row=4,column=3)
    button_mul.grid(row=1,column=2)
    button_div.grid(row=1,column=3)
    button_per.grid(row=1,column=1)
    button_del.grid(row=1,column=0)
    clear_button.grid(row=6,column=1)
    text_box_1.grid(row=0,column=0,columnspan=4)
    #------------------ Layout ------------------


    window.mainloop()   


def str_analyzer(str):
    return None

def main():
    setup()



if __name__ == '__main__':
    main()