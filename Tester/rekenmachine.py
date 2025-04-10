import tkinter as tk

def knop_klik(value):
    huidig = invoer.get()
    invoer.delete(0, tk.END)
    invoer.insert(0, huidig + str(value))

def bereken():
    try:
        resultaat = eval(invoer.get())
        invoer.delete(0, tk.END)
        invoer.insert(0, str(resultaat))
    except Exception as e:
        invoer.delete(0, tk.END)
        invoer.insert(0, "Fout")

def wissen():
    invoer.delete(0, tk.END)

venster = tk.Tk()
venster.title("Rekenmachine")

invoer = tk.Entry(venster, width=20, font=('Arial', 24), borderwidth=2, relief="solid", justify="right")
invoer.grid(row=0, column=0, columnspan=4)

knoppen = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (tekst, rij, kolom) in knoppen:
    if tekst == "=":
        tk.Button(venster, text=tekst, width=5, height=2, font=('Arial', 20), command=bereken).grid(row=rij, column=kolom)
    else:
        tk.Button(venster, text=tekst, width=5, height=2, font=('Arial', 20), command=lambda waarde=tekst: knop_klik(waarde)).grid(row=rij, column=kolom)

tk.Button(venster, text="C", width=5, height=2, font=('Arial', 20), command=wissen).grid(row=4, column=0)

venster.mainloop()