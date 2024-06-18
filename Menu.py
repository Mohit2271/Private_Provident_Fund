from tkinter import *
import webbrowser
from PIL import Image, ImageTk

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu")
        self.root.geometry("1550x800+0+0")
        self.root.configure(bg="white")
       
    def create_widgets(self,root):
        self.image3_label3 = Label(root,bg="white",cursor="hand2")
        self.image3_label3.place(x=1020, y=10,width=200,height=160)
        self.image3 = Image.open("images\satyamev-jayate-Logo.png")
        self.image3 = self.image3.resize((100, 100))
        self.photo3 = ImageTk.PhotoImage(self.image3)
        self.image3_label3.config(image=self.photo3)
        self.image3_label3.bind("<Button-1>", self.open_satyamev_jayate)

        self.image2_label2 = Label(root,bg="white",cursor="hand2")
        self.image2_label2.place(x=870, y=10,width=200,height=160)
        self.image2 = Image.open("images\Mahotsav_Azadi_logo.png")
        self.image2 = self.image2.resize((100, 100))
        self.photo2 = ImageTk.PhotoImage(self.image2)
        self.image2_label2.config(image=self.photo2)
        self.image2_label2.bind("<Button-1>", self.open_azadi)

        self.image1_label1 = Label(root,bg="white",cursor="hand2")
        self.image1_label1.place(x=720, y=10,width=200,height=160)
        self.image1 = Image.open("images\G2O-Logo.jpg")
        self.image1 = self.image1.resize((100, 100))
        self.photo1 = ImageTk.PhotoImage(self.image1)
        self.image1_label1.config(image=self.photo1)
        self.image1_label1.bind("<Button-1>", self.open_G2O)

        self.image_label = Label(root,bg="white")
        self.image_label.place(x=50, y=10,width=200,height=160)
        self.image = Image.open("images\PPF-Logo.jpg")
        self.image = self.image.resize((100, 100))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=self.photo)
        
        label = Label(root, text="Pirvate Provident Fund,India",font=("times new roman", 20, "bold"),bg="white")
        label.place(x=200, y=50)

        label1 = Label(root, text="Ministry of Labour & Employment Government of India",bg="white")
        label1.place(x=200, y=90)

        self.login_button = Button(root, text="Login", command=self.login,cursor="hand2")
        self.login_button.place(x=1070,y=170)

        self.signin_button = Button(root, text="Sign up", command=self.signup,cursor="hand2")
        self.signin_button.place(x=1125,y=170)

        about_us = Label(root,text=("About Us"),font=("times new roman", 20, "bold"),fg='darkblue',bg='white')
        about_us.place(x=730,y=215)

        label2 = Label(root, text='''#EPFO is one of the World's largest Social Security Organisations in terms of 
clientele and the volume of financial transactions undertaken. At present it
    maintains 24.77 crore accounts (Annual Report 2019-20) pertaining to its
members.''',font=("times new roman", 10),bg='white')
        label2.place(x=730,y=265)

        label3 = Label(root, text='''#The Employees' Provident Fund came into existence with the promulgation
of the Employees' Provident Funds Ordinance on the 15th November, 1951.
  It was replaced by the Employees' Provident Funds Act, 1952. The Employees'
   Provident Funds Bill was introduced in the Parliament as Bill Number 15 of the 
year 1952 as a Bill to provide for the institution of provident funds for 
employees in factories and other establishments. The Act is now referred as 
    the Employees' Provident Funds & Miscellaneous Provisions Act, 1952 which 
extends to the whole of India.The Act and Schemes framed there under 
are administered by a tri-partite Board known as the Central Board 
of Trustees, Employees' Provident Fund,consisting of representatives of 
Government (Both Central and State), Employers, and Employees.''',font=("times new roman", 10),bg='white')
        label3.place(x=730,y=345)

        label4 =Label(text='''#The Central Board of Trustees administers a contributory provident fund,
pension scheme and an insurance scheme for the workforce engaged in the 
    organized sector in India.The Board is assisted by the Employee's PF 
Organization (EPFO),consisting of offices at 138 locations across the country. 
  The Organization has a well equipped training set up where officers and 
  employees of the Organization as well as Representatives of the Employers and 
Employees attend sessions for trainings and seminars.The EPFO is under 
the administrative control of Ministry of 
    Labour and Employment, Government of India (click here)
EPFO Organisation Structure (Annual Report 2019-20)''',font=("times new roman", 10),bg='white')
        label4.place(x=730,y=530)

        vision = Label(root, text="Vison",font=("times new roman", 20, "bold"),fg='darkblue',bg='white')
        vision.place(x=50,y=215)

        label5 = Label(text=''' An innovation driven social security organisation aiming to extend universal 
        coverage and ensuring Nirbadh (Seamless and uninterrupted) service delivery to its 
        stakeholders through state-of-the-art technology.''',font=("times new roman", 10),bg='white')
        label5.place(x=50,y=265)

        mission = Label(text="Mission",font=("times new roman", 20, "bold"),fg='darkblue',bg='white')
        mission.place(x=50,y=330)

        label6 = Label(text='''To meet the evolving needs of comprehensive social security in a transparent, 
        contactless, faceless and paperless manner.''',font=("times new roman", 10),bg='white')
        label6.place(x=50,y=380)

        label7 = Label(text='''To ensure Nirbadh services with multi-locational and auto claim settlement process 
        for disaster proofing EPFO.''',font=("times new roman", 10),bg='white')
        label7.place(x=50,y=430)

        label8 = Label(text='''To ensure ease of living for members and pensioners, and ease of doing business 
        for employers by leveraging Government of India's technology platforms for 
        reaching out to millions.''',font=("times new roman", 10),bg='white')
        label8.place(x=50,y=480)

        schema = Label(text="EPFO Schema",font=("times new roman", 20, "bold"),fg='darkblue',bg='white')
        schema.place(x=50,y=545)

        label9 = Label(text='''EPF Scheme 1952''',font=("times new roman", 10, "bold"),fg='darkblue',bg='white')
        label9.place(x=50,y=590)

        label10 = Label(text='''Accumulation plus interest upon retirement and death.
Partial withdrawals allowed for education, marriage, illness and house construction.
Housing Scheme for EPFO Members to achieve Hon'ble Prime Minister's 
Vision of housing to all Indians by 2022.
''',font=("times new roman", 10),bg='white')
        label10.place(x=50,y=610)

        self.image4_label4 = Label(root,bg="white",cursor="hand2")
        self.image4_label4.place(x=1100, y=700,width=50,height=80)
        self.image4 = Image.open("images\whatsapp-logo.png")
        self.image4 = self.image4.resize((40, 40))
        self.photo4 = ImageTk.PhotoImage(self.image4)
        self.image4_label4.config(image=self.photo4)
        self.image4_label4.bind("<Button-1>", self.open_whatsapp)

        self.image5_label5 = Label(root,bg="white",cursor="hand2")
        self.image5_label5.place(x=1050, y=700,width=50,height=80)
        self.image5 = Image.open("images\logo-facebook.png")
        self.image5 = self.image5.resize((40, 40))
        self.photo5 = ImageTk.PhotoImage(self.image5)
        self.image5_label5.config(image=self.photo5)
        self.image5_label5.bind("<Button-1>", self.open_facebook)

        self.image6_label6 = Label(root,bg="white",cursor="hand2")
        self.image6_label6.place(x=1000, y=700,width=50,height=80)
        self.image6 = Image.open("images\logo-twitter.png")
        self.image6 = self.image6.resize((40, 40))
        self.photo6 = ImageTk.PhotoImage(self.image6)
        self.image6_label6.config(image=self.photo6)
        self.image6_label6.bind("<Button-1>", self.open_twitter)

        self.image7_label7 = Label(root,bg="white",cursor="hand2")
        self.image7_label7.place(x=950, y=700,width=50,height=80)
        self.image7 = Image.open("images\instagram.png")
        self.image7 = self.image7.resize((40, 40))
        self.photo7 = ImageTk.PhotoImage(self.image7)
        self.image7_label7.config(image=self.photo7)
        self.image7_label7.bind("<Button-1>", self.open_instagram)

        self.image8_label8 = Label(root,bg="white",cursor="hand2")
        self.image8_label8.place(x=900, y=700,width=50,height=80)
        self.image8 = Image.open("images\youtube.png")
        self.image8 = self.image8.resize((40, 40))
        self.photo8 = ImageTk.PhotoImage(self.image8)
        self.image8_label8.config(image=self.photo8)
        self.image8_label8.bind("<Button-1>", self.open_youtube)

        self.image9_label9 = Label(root,bg="white",cursor="hand2")
        self.image9_label9.place(x=850, y=700,width=50,height=80)
        self.image9 = Image.open("images\contact-logo.png")
        self.image9 = self.image9.resize((40, 40))
        self.photo9 = ImageTk.PhotoImage(self.image9)
        self.image9_label9.config(image=self.photo9)
        self.image9_label9.bind("<Button-1>", self.open_contact)

        self.image10_label10 = Label(root,bg="white")
        self.image10_label10.place(x=50, y=700,width=600,height=80)
        self.image10 = Image.open("images\G20_en.jpeg")
        self.image10 = self.image10.resize((600, 80))
        self.photo10 = ImageTk.PhotoImage(self.image10)
        self.image10_label10.config(image=self.photo10)

        self.image11_label11 = Label(root,bg="white",cursor="hand2")
        self.image11_label11.place(x=1200, y=50,width=350,height=150)
        self.image11 = Image.open("images\india_code.png")
        self.image11 = self.image11.resize((250, 150))
        self.photo11 = ImageTk.PhotoImage(self.image11)
        self.image11_label11.config(image=self.photo11)
        self.image11_label11.bind("<Button-1>", self.open_indiacode)

        self.image12_label12 = Label(root,bg="white",cursor="hand2")
        self.image12_label12.place(x=1200, y=250,width=350,height=150)
        self.image12 = Image.open("images\eShram.png")
        self.image12 = self.image12.resize((250, 150))
        self.photo12 = ImageTk.PhotoImage(self.image12)
        self.image12_label12.config(image=self.photo12)
        self.image12_label12.bind("<Button-1>", self.open_eShram)

        self.image13_label13 = Label(root,bg="white",cursor="hand2")
        self.image13_label13.place(x=1200, y=450,width=350,height=150)
        self.image13 = Image.open("images\online-voter.png")
        self.image13 = self.image13.resize((250, 120))
        self.photo13 = ImageTk.PhotoImage(self.image13)
        self.image13_label13.config(image=self.photo13)
        self.image13_label13.bind("<Button-1>", self.open_voter)

        self.image14_label14 = Label(root,bg="white",cursor="hand2")
        self.image14_label14.place(x=1200, y=650,width=350,height=80)
        self.image14 = Image.open("images\gov-national-portal.png")
        self.image14 = self.image14.resize((250, 50))
        self.photo14 = ImageTk.PhotoImage(self.image14)
        self.image14_label14.config(image=self.photo14)
        self.image14_label14.bind("<Button-1>", self.open_india_gov)

    def open_voter(self, event):
        webbrowser.open_new_tab("https://www.nvsp.in/")
    def open_india_gov(self, event):
        webbrowser.open_new_tab("https://www.india.gov.in/")
    def open_eShram(self, event):
        webbrowser.open_new_tab("https://register.eshram.gov.in/#/user/self")
    def open_indiacode(self, event):
        webbrowser.open_new_tab("https://www.indiacode.nic.in/")
    def open_satyamev_jayate(self, event):
        webbrowser.open_new_tab("http://www.satyamevjayate.in/")
    def open_azadi(self, event):
        webbrowser.open_new_tab("https://amritmahotsav.nic.in/index.htm")
    def open_G2O(self, event):
        webbrowser.open_new_tab("https://www.g20.org/en/")
    def open_whatsapp(self, event):
        webbrowser.open_new_tab("https://www.epfindia.gov.in/site_docs/PDFs/Downloads_PDFs/WhatsApp_Helpline.pdf")
    def open_facebook(self, event):
        webbrowser.open_new_tab("https://www.facebook.com/socialepfo/")
    def open_twitter(self, event):
        webbrowser.open_new_tab("https://twitter.com/socialepfo/")
    def open_instagram(self, event):
        webbrowser.open_new_tab("https://www.instagram.com/social_epfo/?igshid=YmMyMTA2M2Y%3D")
    def open_youtube(self, event):
        webbrowser.open_new_tab("https://www.youtube.com/channel/UClmVVcYuH0ZPm3qsPm1TQIg")
    def open_contact(self, event):
        webbrowser.open_new_tab("https://www.epfindia.gov.in/site_en/Contact.php")
    
    def login(self):
        self.root.destroy()
        import Login
        root=Tk()
        Login.Login(root)
        root.mainloop()

    def signup(self):
        self.root.destroy()
        import Signup
        root=Tk()
        Signup.SignUpPage(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Menu(root)
    obj.create_widgets(root)
    root.mainloop()
