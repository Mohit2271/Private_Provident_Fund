from tkinter import *
from PIL import Image, ImageTk

class ProvidentFundCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Provident Fund Calculator")
        self.root.geometry("900x600")
        self.root.config(bg="#04D8B2")
        Label(self.root, text="Provident Fund Calculator", font=("times new roman",20,"bold"),bg="#04D8B2", fg="black", anchor="w", padx=10).place(x=400,y=100,relwidth=1)

        self.Yearly_Investment = DoubleVar() 
        self.time_period = IntVar()
        self.interest_rate = DoubleVar(value=7.1)

        self.image_label = Label(root)
        self.image_label.place(x=50, y=170,width=400,height=330)
        self.image = Image.open("images\PPF-Calculator.png")
        self.image = self.image.resize((500, 500))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)

        Yearly_Investment_slider_label = Label(root, text="Yearly Investment",font=("times new roman",13,"bold"),bg="#04D8B2")
        Yearly_Investment_slider_label.place(x=500,y=200)
        Yearly_Investment_slider = Scale(root, from_=500, to=100000, orient="horizontal", length=200, variable=self.Yearly_Investment, command=lambda x: Yearly_Investment_slider_label.config(text=f'Yearly Investment : {Yearly_Investment_slider.get()}'),bg="#04D8B2",activebackground="#04D8B2")
        Yearly_Investment_slider.place(x=500,y=230)
        
        time_period_slider_label = Label(root, text="Time Period (In Years)",font=("times new roman",13,"bold"),bg="#04D8B2")
        time_period_slider_label.place(x=500,y=300)
        time_period_slider = Scale(root, from_=1, to=50, orient="horizontal", length=200, variable=self.time_period, command=lambda x: time_period_slider_label.config(text=f'Time Period (In Years): {time_period_slider.get()}'),bg="#04D8B2",activebackground="#04D8B2")
        time_period_slider.place(x=500,y=330)
        
        interest_rate_label = Label(root, text="Enter the annual interest rate (%):",font=("times new roman",13,"bold"),bg="#04D8B2")
        interest_rate_label.place(x=500,y=400)
        interest_rate_entry = Entry(root, textvariable=self.interest_rate,state="disabled")
        interest_rate_entry.place(x=500,y=430)

        calculate_button = Button(root, text="Calculate", command=self.calculate,font=("times new roman",10,"bold"), cursor="hand2")
        calculate_button.place(x=550,y=470)

        self.result_label = Label(root, text="",font=("times new roman",10,"bold"),bg="#04D8B2")
        self.result_label.place(x=500,y=530)

        back_button = Button(root, text="Back to Menu", command=self.back_to_menu,font=("times new roman",10,"bold"), cursor="hand2")
        back_button.place(x=650,y=470)

    def back_to_menu(self):
        self.root.destroy()
        import Main_menu 
        root = Tk()
        email = ""
        Main_menu.Main_Menu(root, email)
        root.mainloop()

    def calculate(self):
        principal = self.Yearly_Investment.get()
        years = self.time_period.get()
        interest_rate = self.interest_rate.get()

        if principal <= 0 or years <= 0 or interest_rate <= 0:
            self.result_label.config(text="Inputs should be greater than zero.")
            return

        interest_rate /= 100
        interest = principal * (1 + interest_rate) ** years - principal
        total_amount = principal + interest

        self.result_label.config(text=f"Total amount after {years} years: Rs. {total_amount:,.2f}")

if __name__ == "__main__":
    root = Tk()
    obj = ProvidentFundCalculator(root)
    root.mainloop()
