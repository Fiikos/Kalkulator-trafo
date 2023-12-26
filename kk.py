import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Kalkulator transformatora")

        # Zmienne przechowujące dane wprowadzone przez użytkownika
        self.var_a = tk.StringVar()
        self.var_b = tk.StringVar()
        self.var_c = tk.StringVar()
        self.var_d = tk.StringVar()

        # Pole tekstowe i etykiety dla liczb
        tk.Label(root, text="Wymiar rdzenia a w cm:").grid(row=0, column=0)
        entry_a = tk.Entry(root, textvariable=self.var_a)
        entry_a.grid(row=0, column=1)

        tk.Label(root, text="Wymiar rdzenia b w cm:").grid(row=1, column=0)
        entry_b = tk.Entry(root, textvariable=self.var_b)
        entry_b.grid(row=1, column=1)

        tk.Label(root, text="Napięcie wejściowe:").grid(row=2, column=0)
        entry_c = tk.Entry(root, textvariable=self.var_c)
        entry_c.grid(row=2, column=1)

        tk.Label(root, text="napięcie wyjściowe:").grid(row=3, column=0)
        entry_d = tk.Entry(root, textvariable=self.var_d)
        entry_d.grid(row=3, column=1)

        # Przycisk do obliczeń
        calculate_button = tk.Button(root, text="Oblicz", command=self.calculate)
        calculate_button.grid(row=4, column=0, columnspan=2)

        # Wynik obliczeń
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def calculate(self):
        try:
            # Pobieranie danych od użytkownika i przekształcanie ich na liczby
            a = float(self.var_a.get())
            b = float(self.var_b.get())
            c = float(self.var_c.get())
            d = float(self.var_d.get())
            pi = 3.14
            # Wykonanie obliczeń
            S = a * b
            #Moc transformatora
            P = round(S * S * 0.69)
            #Ilość zwoi na jeden wolt
            N = 45 / S
            #Ilość zwoi uzwojenia pierwotnego
            N1 = round(c * N,1)
            #Ilość zwoi uzwojenia wtórnego
            N2 = round(d * N,1)
            #Prąd uzwojenia pierwotnego w A
            I1 = round(P / c,2)
            #Prąd uzwojenia wtórnego w A
            I2 = round(P / d,2)
            #Średnica drutu uzwojenia pierwotnego
            fi1 = round(((2 * I1) / pi),2)
            #Średnica drutu uzwojenia wtórnego
            fi2 = round(((2 * I2) / pi),2)
            # Wyświetlenie wyniku
            self.result_label.config(text=f"Wynik : |S = {S} cm || P = {P} W || N = {N}zwoi/Volt || N1 = {N1} zwoi || N2 = {N2} zwoi || I1 = {I1} A || I2 = {I2} A || fi1 = {fi1} mm || fi2 = {fi2} mm|")
           
        except ValueError:
            self.result_label.config(text="Błąd: Wprowadź poprawne liczby")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
