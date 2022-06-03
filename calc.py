from tkinter import *




class start_app:  #here we create class gui tkinter for calc
    
    
    def __init__(self):   #constructor class start_app
        
        self.root = Tk()
        self.root.title('app_calc')
        self.root.geometry("354x460")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.config(background='black')

        self.string = "" #create string
        
        app_calc(self.root , self.string)  #send to class app_calc(to constructor:tkinter and string = "")
        




                

class app_calc: #in this class we create function for calculator


    def __init__(self ,gui ,inputC):  #constructor class app_calc

        self.gui = gui

        self.inputC = inputC

        #GUI function
        self.gui_button_numbers()
        self.gui_button_char()
        self.gui_button_clear()
        self.gui_button_result()
        self.gui_show_dispaly()


   

    def gui_button_numbers(self):  #create gui button and send to command char

        btn1=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="1",command=lambda: self.add_string_to_screen('1'),font=("Courier New",16,'bold'))
        btn1.place(x=10,y=100)

        btn2=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="2",command=lambda: self.add_string_to_screen('2'),font=("Courier New",16,'bold'))
        btn2.place(x=10,y=170)

        btn3=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="3",command=lambda: self.add_string_to_screen('3'),font=("Courier New",16,'bold'))
        btn3.place(x=10,y=240)

        btn4=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="4",command=lambda: self.add_string_to_screen('4'),font=("Courier New",16,'bold'))
        btn4.place(x=75,y=100)

        btn5=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="5",command=lambda: self.add_string_to_screen('5'),font=("Courier New",16,'bold'))
        btn5.place(x=75,y=170)

        btn6=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="6",command=lambda: self.add_string_to_screen('6'),font=("Courier New",16,'bold'))
        btn6.place(x=75,y=240)

        btn7=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="7",command=lambda: self.add_string_to_screen('7'),font=("Courier New",16,'bold'))
        btn7.place(x=140,y=100)

        btn8=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="8",command=lambda: self.add_string_to_screen('8'),font=("Courier New",16,'bold'))
        btn8.place(x=140,y=170)

        btn9=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="9",command=lambda: self.add_string_to_screen('9'),font=("Courier New",16,'bold'))
        btn9.place(x=140,y=240)

        btn0=Button(self.gui,padx=79,pady=14,bd=4,bg='white',text="0",command=lambda: self.add_string_to_screen('0'),font=("Courier New",16,'bold'))
        btn0.place(x=10,y=310)



    def gui_button_char(self): #gui char and send command

        ch1=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="+",command=lambda: self.add_string_to_screen('+'),font=("Courier New",16,'bold'))
        ch1.place(x=205,y=100)

        ch2=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="-",command=lambda: self.add_string_to_screen('-'),font=("Courier New",16,'bold'))
        ch2.place(x=205,y=170)

        ch3=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="*",command=lambda: self.add_string_to_screen('*'),font=("Courier New",16,'bold'))
        ch3.place(x=205,y=240)

        ch4=Button(self.gui,padx=14,pady=14,bd=4,bg='white',text="/",command=lambda: self.add_string_to_screen('/'),font=("Courier New",16,'bold'))
        ch4.place(x=205,y=310)



    def gui_button_clear(self): #gui button clear all and send command

        btn_clear=Button(self.gui,padx=14,pady=119,bd=4,bg='grey',text="CE",command=self.clear,font=("Courier New",16,'bold'))
        btn_clear.place(x=270,y=100)
        


    def gui_button_result(self): #gui button result and send command to calc

        btn_res=Button(self.gui,padx=151,pady=14,bd=4,bg='green',text="=",command=self.calculator,font=("Courier New",16,'bold'))
        btn_res.place(x=10,y=380)

            

    def gui_show_dispaly(self): #gui screen and send all result to ( self.show )

        self.show = Text(self.gui,font=('Verdana', 15),height=3 ,width=30,bg='powder blue')
        self.show.grid()
        
        self.show.insert(END,"Enter expression")



    def add_string_to_screen(self, text): #add to self.inputC chars , and send to fun to show

        self.inputC = self.inputC + text
        self.screen_show(self.inputC)



    def screen_show(self, text): #show items in the screen

        self.show.delete('1.0', END)
        self.show.insert('1.0', text)
       


    def calculator(self): # here we clac all self.inputC string when we input
        
        try:
           self.answer = eval(self.inputC) # eval this fun Built-in which calculates an arithmetic operation our(self.inputC)
           self.screen_show(self.answer)
           
        except:
           self.show.delete(0.0,END)
           self.show.insert(END,"Enter correct input")
           self.inputC = ""

           

    def clear(self): #clear all from screen and from self.inputC
        
           self.inputC = ""
           self.screen_show(self.inputC)
     

        


        

    

if __name__ == '__main__': #start the app
    start_app()
