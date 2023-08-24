import tkinter as tk


#TODO: add functionality to the buttons
#TODO: string analyzer function
#TODO: transform this program into an executable file

input_expression =""

def setup():
    #create the Window
    window = tk.Tk()
    window.geometry('648x360')
    window.title('Calculator')
    window.resizable(0,0)   


    #-----Create the buttons and text box--------

    #create the frame for the input field
    frame_txt = tk.Frame(window,highlightbackground='black',highlightthickness=2,bd=0,width=648)
    frame_txt.grid(row=0,column=0,ipadx=13)
    text_box_1 = tk.Entry(frame_txt,width=36,justify='right',textvariable=input_expression,font=('Arial',18,'bold'))
    text_box_1.pack(expand=True,fill='both',side='left',ipadx=0,ipady=10)

    #create the frame for the buttons
    frame_btn = tk.Frame(window, width=648, bg="black",highlightbackground='black',highlightthickness=2,bd=0)
    frame_btn.grid(row=1,column=0)

    #create the buttons
    button_0 = tk.Button(frame_btn,text='0',width=33,height=2,command=lambda: text_box_1.insert(tk.END,'0'),padx=10,pady=10)
    button_1 = tk.Button(frame_btn,text='1',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'1'),padx=10,pady=10)
    button_2 = tk.Button(frame_btn,text='2',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'2'),padx=10,pady=10)
    button_3 = tk.Button(frame_btn,text='3',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'3'),padx=10,pady=10)
    button_4 = tk.Button(frame_btn,text='4',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'4'),padx=10,pady=10)
    button_5 = tk.Button(frame_btn,text='5',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'5'),padx=10,pady=10)
    button_6 = tk.Button(frame_btn,text='6',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'6'),padx=10,pady=10)
    button_7 = tk.Button(frame_btn,text='7',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'7'),padx=10,pady=10)
    button_8 = tk.Button(frame_btn,text='8',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'8'),padx=10,pady=10)
    button_9 = tk.Button(frame_btn,text='9',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'9'),padx=10,pady=10)
    button_add = tk.Button(frame_btn,text='+',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'+'),padx=10,pady=10)
    button_sub = tk.Button(frame_btn,text='-',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'-'),padx=10,pady=10)
    button_eq = tk.Button(frame_btn,text='=',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'='),padx=10,pady=10)
    button_mul = tk.Button(frame_btn,text='*',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'*'),padx=10,pady=10)
    button_div = tk.Button(frame_btn,text='/',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'/'),padx=10,pady=10)
    button_per = tk.Button(frame_btn,text='%',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'%'),padx=10,pady=10)
    button_del = tk.Button(frame_btn,text='del',width=15,height=2,command=lambda: text_box_1.delete(len(text_box_1.get())-1),padx=10,pady=10)
    clear_button = tk.Button(frame_btn,text='Clear',width=15,height=2,command=lambda: text_box_1.delete(0,tk.END),padx=10,pady=10)
    dot_button = tk.Button(frame_btn,text='.',width=15,height=2,command=lambda: text_box_1.insert(tk.END,'.'),padx=10,pady=10)

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
    clear_button.grid(row=5,column=3)
    dot_button.grid(row=5,column=2)
    #------------------ Layout ------------------


    window.mainloop()   


def str_analyzer(str):
    return None

def main():
    setup()



if __name__ == '__main__':
    main()