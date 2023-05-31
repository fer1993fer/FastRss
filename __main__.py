
import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.font import Font
from PIL import Image

class App(tk.Tk) :
    def __init__(self) :
        super().__init__()

        self.f = Font(family='Cantarell-Bold', name='q', size=16, weight='bold', slant="italic")
        self.f2 = Font(family="Cantarell-Bold", name="q2", size=10, weight="bold")
        self.f3 =Font(family="Canterall-Bold", name="q3", size=13, weight="normal", slant="italic" )

        self.geometry("474x302")
        

        self.fr = ttk.Frame(master=self)
        self.fr.configure(height=292, width=464, relief="groove", borderwidth=5)
        self.fr.place(x=5, y=5)

        self.lbl = ttk.Label(master=self.fr)
        self.lbl.configure(text="Selecciona una imagen", font=self.f)
        self.lbl.place(x=85, y=20)

        self.ent = ttk.Entry(master=self.fr, width=25, font=self.f3, foreground="red")
        self.ent.place(x=80, y=70)

        self.btn = ttk.Button(master=self.fr)
        self.btn.configure(command=self.busqueda, text="...", style="Toolbutton", padding=[-1,-4,0,-3])
        self.btn.place(x=370, y=90, bordermode="outside")

        self.lbl2 =ttk.Label(master=self.fr)
        self.lbl2.configure(text="Ingresa las medidas deceadas", font=self.f)
        self.lbl2.place(x=40, y=120)

        self.lbl3 = ttk.Label(master=self.fr)
        self.lbl3.config(text="Alto",font=self.f)
        self.lbl3.place(x=50, y=190)

        self.lbl4 = ttk.Label(master=self.fr)
        self.lbl4.configure(text="Ancho", font=self.f)
        self.lbl4.place(x=250, y=190)


        self.ent2 = ttk.Entry(master=self.fr)
        self.ent2.configure(width=5, font=self.f3, foreground="red")
        self.ent2.place(x=120, y=190)


        self.ent3 = ttk.Entry(master=self.fr)
        self.ent3.configure(width=5, font=self.f3, foreground="red")
        self.ent3.place(x=350, y=190)

        self.btn2 = ttk.Button(master=self.fr)
        self.btn2.configure(text="Iniciar", command=self.iniciar)
        self.btn2.place(x=145, y=240)

        self.s = ttk.Style()
        self.s.configure("Toolbutton", font=self.f2)
        self.s.configure("TButton", font=self.f)
        
    
         
        

    def busqueda(self) :
        arch = askopenfilename()
        self.ent.insert(tk.END, arch)

    def iniciar(self) :
        arch1 = self.ent.get()
        m1 = self.ent2.get()
        m2 = self.ent3.get()
        archpr, archpr1 = os.path.split(arch1)
        mm1 = int(m1)
        mm2 = int(m2)
        
        with Image.open(arch1) as img :
            imgns = img.resize((mm1, mm2))
            imgns.save(archpr1)

if __name__ == "__main__" :
    app = App()
    app.mainloop()


