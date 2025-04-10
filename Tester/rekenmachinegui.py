import tkinter as tk
from tkinter import messagebox


def optellen(x, y):
    return x + y

def aftrekken(x, y):
    return x - y

def vermenigvuldigen(x, y):
    return x * y

def delen(x, y):
    if y == 0:
        return "Kan niet delen door nul!"
    return x / y

def bereken():
    try:
        getal1 = float(entry1.get())
        getal2 = float(entry2.get())
        bewerking = keuze.get()

        if bewerking == "Optellen":
            resultaat = optellen(getal1, getal2)
        elif bewerking == "Aftrekken":
            resultaat = aftrekken(getal1, getal2)
        elif bewerking == "Vermenigvuldigen":
            resultaat = vermenigvuldigen(getal1, getal2)
        elif bewerking == "Delen":
            resultaat = delen(getal1, getal2)
        else:
            resultaat = "Ongeldige bewerking!"

        label_resultaat.config(text="Resultaat: " + str(resultaat))
    except ValueError:
        messagebox.showerror("Fout", "Voer alleen geldige nummers in.")

root = tk.Tk()
root.title("Rekenmachine")

tk.Label(root, text="Eerste getal:").grid(row=0, column=0, padx=10, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Tweede getal:").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Bewerking:").grid(row=2, column=0, padx=10, pady=5)
keuze = tk.StringVar(root)
keuze.set("Optellen")  
optie_menu = tk.OptionMenu(root, keuze, "Optellen", "Aftrekken", "Vermenigvuldigen", "Delen")
optie_menu.grid(row=2, column=1)

knop = tk.Button(root, text="Bereken", command=bereken)
knop.grid(row=3, column=0, columnspan=2, pady=10)

label_resultaat = tk.Label(root, text="Resultaat: ")
label_resultaat.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()