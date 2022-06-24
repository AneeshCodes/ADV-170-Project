from tkinter import *

root = Tk()
root.title("600x600")
root.title("ADV-170")

grade3 = Label(root)
grade5 = Label(root)
grade10 = Label(root)

class grade_3():
    
    def __init__(self,math,lang):
        self.math = math
        self.lang = lang
        
    def percent3(self):
        percentage = (self.math + self.lang)/2
        grade3["text"] = percentage
        
class grade_5():
    
    def __init__(self,math,lang,social):
        self.math = math
        self.lang = lang
        self.social = social
        
    def percent3(self):
        percentage = (self.math + self.lang + self.social)/3
        grade5["text"] = percentage
        
class grade_10():
    
    def __init__(self,math,lang,social,science):
        self.math = math
        self.lang = lang
        self.social = social
        self.science = science
        
    def percent3(self):
        percentage = (self.math + self.lang + self.social + self.science)/4
        grade10["text"] = percentage

obj3 = grade_3(40,50)
obj5 = grade_5(40,50,60)        
obj10 = grade_10(40,50,60,70)

button3 = Button(root,text="Grade 3",command = obj3.percent3)
button5 = Button(root,text="Grade 5",command = obj5.percent3)
button10 = Button(root,text="Grade 10",command = obj10.percent3)

button3.pack(padx=20,pady=20)
grade3.pack(padx=20,pady=20)
button5.pack(padx=20,pady=20)
grade5.pack(padx=20,pady=20)
button10.pack(padx=20,pady=20)
grade10.pack(padx=20,pady=20)

root.mainloop()