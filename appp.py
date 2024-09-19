import tkinter as tk
from tkinter import messagebox
import requests
import json

# Funkce pro odeslání dat
def send_drink():
    name = name_entry.get()
    drink_type = drink_type_var.get()
    quantity = quantity_entry.get()

    if not name or not quantity:
        messagebox.showerror("Chyba", "Vyplňte všechna pole.")
        return

    try:
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Chyba", "Množství musí být číslo.")
        return

    data = {
        "name": name,
        "drinkType": drink_type,
        "quantity": quantity
    }

    try:
        response = requests.post("http://ajax1.lmsoft.cz/procedure.php?cmd=saveDrinks", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Úspěch", "Data byla úspěšně odeslána!")
            name_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Chyba", f"Chyba při odesílání: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Došlo k chybě: {e}")

# Funkce pro načtení měsíčního přehledu
def show_summary():
    month = month_var.get()
    url = f"http://ajax1.lmsoft.cz/procedure.php?cmd=getSummaryOfDrinks&month={month}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            summary = response.json()
            summary_text = ""
            for drink in summary:
                summary_text += f"{drink['name']} vypil {drink['quantity']} ml {drink['drinkType']}\n"
            result_label.config(text=summary_text)
        else:
            messagebox.showerror("Chyba", f"Chyba při načítání: {response.status_code}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Došlo k chybě: {e}")

# Hlavní okno aplikace
root = tk.Tk()
root.title("Evidování vypité kávy")

# Vstupy pro odesílání dat
tk.Label(root, text="Jméno:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Typ nápoje:").grid(row=1, column=0)
drink_type_var = tk.StringVar(value="coffee")
drink_type_menu = tk.OptionMenu(root, drink_type_var, "coffee", "tea", "juice")
drink_type_menu.grid(row=1, column=1)

tk.Label(root, text="Množství (ml):").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1)

send_button = tk.Button(root, text="Odeslat", command=send_drink)
send_button.grid(row=3, columnspan=2)

# Výběr měsíce pro měsíční přehled
tk.Label(root, text="Vyberte měsíc:").grid(row=4, column=0)
month_var = tk.IntVar(value=9)
month_menu = tk.OptionMenu(root, month_var, *range(1, 13))
month_menu.grid(row=4, column=1)

summary_button = tk.Button(root, text="Zobrazit měsíční přehled", command=show_summary)
summary_button.grid(row=5, columnspan=2)

# Výsledek
result_label = tk.Label(root, text="")
result_label.grid(row=6, columnspan=2)

root.mainloop()
