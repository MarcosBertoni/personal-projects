import customtkinter as ctk

class APP:
    def __init__(self, master: ctk.CTk()):
        self.master= master
        self.master.geometry('250x200')
        self.master.resizable(False, False)
        self.master.wm_title('Counter')
        
        #Creates the counter as a string
        self.counter: str = '0'
        
        #Creates a Label
        self.lable = ctk.CTkLabel(self.master, text= self.counter, font= ('Helvetica bold', 26))
        self.lable.place(relx=0.5, rely=0.4, anchor='center')
        
        #Creates a Button
        self.button= ctk.CTkButton(self.master, text= 'Increment',
                                   command= self.increment, corner_radius= 20)
        self.button.place(relx=0.5, rely=0.6, anchor='center')
        
        self.reset_button: ctk.CTkButton | None = None
    def increment(self):
        try:
            self.counter = str(int(self.counter)+1)
            self.lable.configure(text = self.counter)
            
            if int(self.counter) == 1:
                self.reset_button = ctk.CTkButton(self.master,text = 'Reset ',
                                                  command = self.reset, corner_radius= 20,
                                                  fg_color= 'red', hover_color= 'darkred')
                self.reset_button.place(relx=0.5, rely=0.8, anchor='center')
        
        except Exception as e:
            print('Error',e) 
    
    def reset(self):
        try:
            self.counter='0'
            self.lable.configure(text= self.counter)
            
            self.reset_button.destroy()
            
        except Exception as e:
            print('Error',e)
    
if __name__== '__main__':
    
    app= ctk.CTk()
    gui=APP(master=app)
    app.mainloop()
    
    
        
        