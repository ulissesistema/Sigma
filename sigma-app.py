import tkinter as tk
from tkinter import ttk
import random
from tkinter import messagebox, scrolledtext
import sys
w = tk.Tk()
w.config(bg="#202020")
w.title("Sigma")
def memo2():
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import messagebox
    class Menubar:
        def __init__(self, parent):
            font_specs = ('Calibri', 14)
            menubar = tk.Menu(parent.master, font=font_specs)
            parent.master.config(menu=menubar)
            file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
            file_dropdown.add_command(label="Nuovo File",
                                      accelerator="Ctrl+N",
                                      command=parent.new_file)
            file_dropdown.add_command(label="Apri File",
                                      accelerator="Ctrl+O",
                                      command=parent.open_file)
            file_dropdown.add_command(label="Salva",
                                      accelerator="Ctrl+S",
                                      command=parent.save)
            file_dropdown.add_command(label="Salva con Nome",
                                      accelerator="Ctrl+Shift+S",
                                      command=parent.save_as)
            file_dropdown.add_separator()
            file_dropdown.add_command(label="Esci",
                                      command=parent.master.destroy)
            about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
            about_dropdown.add_command(label="Note di Rilascio",
                                       command=self.show_release_notes)
            about_dropdown.add_separator()
            about_dropdown.add_command(label="About",
                                       command=self.show_about_message)
            menubar.add_cascade(label="File", menu=file_dropdown)
            menubar.add_cascade(label="About", menu=about_dropdown)
        def show_about_message(self):
            box_title = "Riguardo Sigma Memo"
            box_message = "Un semplice Editor Testuale per usare appunti con Sigma! E' incorporato con l'app Sigma."
            messagebox.showinfo(box_title, box_message)
        def show_release_notes(self):
            box_title = "Note di Rilascio"
            box_message = "Versione 0.1 - Gutenberg"
            messagebox.showinfo(box_title, box_message)
    class Statusbar:
        def __init__(self, parent):
            font_specs = ('Calibri', 12)
            self.status = tk.StringVar()
            self.status.set("Sigma Memo - 0.1 Gutenberg")
            label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                             bg="lightgrey", anchor='sw', font=font_specs)
            label.pack(side=tk.BOTTOM, fill=tk.BOTH)
        def update_status(self, *args):
            if isinstance(args[0], bool):
                self.status.set("Il tuo File è stato salvato!")
            else:
                self.status.set("Sigma Memo - 0.1 Gutenberg")
    class PyText:
        """ Sigma Memo è un semplice Editor Testuale creato con TkInter Python 3.10.7."""
        def __init__(self, master):
            master.title("Untitled - Sigma Memo")
            master.geometry("1200x700")
            font_specs = ('Calibri', 18)
            self.master = master
            self.filename = None
            self.textarea = tk.Text(master, font=font_specs)
            self.scroll = tk.Scrollbar(master, command=self.textarea.yview)
            self.textarea.configure(yscrollcommand=self.scroll.set)
            self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
            self.menubar = Menubar(self)
            self.statusbar = Statusbar(self)
            self.bind_shortcuts()
        def set_window_title(self, name=None):
            if name:
                self.master.title(name + " - Sigma Memo")
            else:
                self.master.title("Untitled - Sigma Memo")
        def new_file(self, *args):
            self.textarea.delete(1.0, tk.END)
            self.filename = None
            self.set_window_title()
        def open_file(self, *args):
            self.filename = filedialog.askopenfilename(
                defaultextension=".txt",
                filetypes=[("Tutti i file", "*.*"),
                           ("File di Testo", "*.txt")])
            if self.filename:
                self.textarea.delete(1.0, tk.END)
                with open(self.filename, "r") as f:
                    self.textarea.insert(1.0, f.read())
                self.set_window_title(self.filename)
        def save(self, *args):
            if self.filename:
                try:
                    textarea_content = self.textarea.get(1.0, tk.END)
                    with open(self.filename, "w") as f:
                        f.write(textarea_content)
                except Exception as e:
                    print(e)
            else:
                self.save_as()

        def save_as(self, *args):
            try:
                new_file = filedialog.asksaveasfilename(
                    initialfile='Untitled.txt',
                    defaultextension=".txt",
                        filetypes=[("Tutti i file", "*.*"),
                                   ("File di Testo", "*.txt")])
                with open(new_file, 'w') as f:
                    textarea_content = self.textarea.get(1.0, tk.END)
                    f.write(textarea_content)
                self.filename = new_file
                self.set_window_title(self.filename)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        def bind_shortcuts(self):
            self.textarea.bind('<Control-n>', self.new_file)
            self.textarea.bind('<Control-o>', self.open_file)
            self.textarea.bind('<Control-s>', self.save)
            self.textarea.bind('<Control-S>', self.save_as)
            self.textarea.bind('<Key>', self.statusbar.update_status)
    if __name__ == "__main__":
        master = tk.Tk()
        pt = PyText(master)
        master.mainloop()
def convertitore2():
    class ValueConverter:
        def __init__(self, master):
            master.title("Sigma Convertitore di Valori")
            master.geometry("400x400")
            master.config(bg="#202020")
            container = tk.Frame(master)
            container.pack(fill="both", expand=True)
            canvas = tk.Canvas(container, bg="#202020")
            scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas, bg="#202020")
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            # Unità di misura lunghezza
            self.lenunits = {
                "Chilometri": 0.001,
                "Ettometri": 0.01,
                "Decametri": 0.1,
                "Metri": 1,
                "Decimetri": 10,
                "Centimetri": 100,
                "Millimetri": 1000,
                "Miglia": 0.000621371,
                "Piedi": 3.28084
            }
            # Titolo
            self.wow = tk.Label(scrollable_frame, text="Da qui a là", font=("Calibri", 36), bg="#202020", fg="white")
            self.wow.pack(pady=10)
            # Sezione lunghezza
            self.label_input = tk.Label(scrollable_frame, text="Lunghezza: inserisci il valore:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_input.pack(pady=10)
            self.entry_value = tk.Entry(scrollable_frame, font=("Courier", 14), justify="center")
            self.entry_value.pack(pady=5)
            self.label_from = tk.Label(scrollable_frame, text="Da:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_from.pack(pady=10)
            self.combo_from = ttk.Combobox(scrollable_frame, values=list(self.lenunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_from.set("Metri")
            self.combo_from.pack()
            self.label_to = tk.Label(scrollable_frame, text="A:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_to.pack(pady=10)
            self.combo_to = ttk.Combobox(scrollable_frame, values=list(self.lenunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_to.set("Chilometri")
            self.combo_to.pack()
            self.button_convert = tk.Button(scrollable_frame, text="Converti", font=("Courier", 14), command=self.convertlen, bg="#1848ca", fg="white")
            self.button_convert.pack(pady=20)
            self.result_label = tk.Label(scrollable_frame, text="", font=("Courier", 16), bg="#202020", fg="blue")
            self.result_label.pack(pady=10)
            # Unità di misura massa
            self.massunits = {
                "Megagrammi (1000 kg)": 0.001,
                "Quintali (100 kg)": 0.01,
                "Miriagrammi (10 kg)": 0.1,
                "Chilogrammi": 1,
                "Ettogrammi": 10,
                "Decagrammi": 100,
                "Grammi": 1000,
                "Decigrammi": 10000,
                "Centigrammi": 100000,
                "Milligrammi": 1000000
            }
            # Sezione massa
            self.label_input2 = tk.Label(scrollable_frame, text="Massa: inserisci il valore:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_input2.pack(pady=10)
            self.entry_value2 = tk.Entry(scrollable_frame, font=("Courier", 14), justify="center")
            self.entry_value2.pack(pady=5)
            self.label_from2 = tk.Label(scrollable_frame, text="Da:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_from2.pack(pady=10)
            self.combo_from2 = ttk.Combobox(scrollable_frame, values=list(self.massunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_from2.set("Chilogrammi")
            self.combo_from2.pack()
            self.label_to2 = tk.Label(scrollable_frame, text="A:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_to2.pack(pady=10)
            self.combo_to2 = ttk.Combobox(scrollable_frame, values=list(self.massunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_to2.set("Grammi")
            self.combo_to2.pack()
            self.button_convert2 = tk.Button(scrollable_frame, text="Converti", font=("Courier", 14), command=self.convertmass, bg="#1848ca", fg="white")
            self.button_convert2.pack(pady=20)
            self.result_label2 = tk.Label(scrollable_frame, text="", font=("Courier", 16), bg="#202020", fg="blue")
            self.result_label2.pack(pady=10)
            # Unità di misura valuta
            self.monyunits = {
                "USD $ (Dollaro degli USA)": 1,
                "BTC (Bitcoin)": 0.00001,
                "EUR € (Euro)": 0.95843,
                "GBP £ (Sterlina britannica)": 0.79544,
                "JPY (Yen giapponese)": 156.375,
                "CNY (Renminbi Yuan cinese)": 7.2953,
                "AED (Dirham degli Emirati Arabi)": 3.7269
            }
            # Sezione valuta
            self.label_input3 = tk.Label(scrollable_frame, text="Valuta: inserisci il valore:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_input3.pack(pady=10)
            self.entry_value3 = tk.Entry(scrollable_frame, font=("Courier", 14), justify="center")
            self.entry_value3.pack(pady=5)
            self.label_from3 = tk.Label(scrollable_frame, text="Da:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_from3.pack(pady=10)
            self.combo_from3 = ttk.Combobox(scrollable_frame, values=list(self.monyunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_from3.set("USD $ (Dollaro degli USA)")
            self.combo_from3.pack()
            self.label_to3 = tk.Label(scrollable_frame, text="A:", font=("Courier", 12), bg="#202020", fg="white")
            self.label_to3.pack(pady=10)
            self.combo_to3 = ttk.Combobox(scrollable_frame, values=list(self.monyunits.keys()), font=("Courier", 12), state="readonly")
            self.combo_to3.set("EUR € (Euro)")
            self.combo_to3.pack()
            self.button_convert3 = tk.Button(scrollable_frame, text="Converti", font=("Courier", 14), command=self.convertmony, bg="#1848ca", fg="white")
            self.button_convert3.pack(pady=20)
            self.result_label3 = tk.Label(scrollable_frame, text="", font=("Courier", 16), bg="#202020", fg="blue")
            self.result_label3.pack(pady=10)
        def convertlen(self):
            try:
                value = float(self.entry_value.get())
                from_unit = self.combo_from.get()
                to_unit = self.combo_to.get()
                factor_from = self.lenunits[from_unit]
                factor_to = self.lenunits[to_unit]
                base_value = value / factor_from
                converted_value = base_value * factor_to
                self.result_label.config(text=f"{value} {from_unit} = {converted_value} {to_unit}", fg="blue")
            except ValueError:
                self.result_label.config(text="Errore: inserisci un numero valido!",bg="#202020", fg="red")
        def convertmass(self):
                    try:
                        value = float(self.entry_value2.get())
                        from_unit = self.combo_from2.get()
                        to_unit = self.combo_to2.get()
                        factor_from = self.massunits[from_unit]
                        factor_to = self.massunits[to_unit]
                        base_value = value / factor_from
                        converted_value = base_value * factor_to
                        self.result_label2.config(text=f"{value} {from_unit} = {converted_value} {to_unit}", fg="blue")
                    except ValueError:
                        self.result_label2.config(text="Errore: inserisci un numero valido!",bg="#202020", fg="red")
        def convertmony(self):
                    try:
                        value = float(self.entry_value3.get())
                        from_unit = self.combo_from3.get()
                        to_unit = self.combo_to3.get()
                        factor_from = self.monyunits[from_unit]
                        factor_to = self.monyunits[to_unit]
                        base_value = value / factor_from
                        converted_value = base_value * factor_to
                        self.result_label3.config(text=f"{value} {from_unit} = {converted_value} {to_unit}", fg="blue")
                    except ValueError:
                        self.result_label3.config(text="Errore: inserisci un numero valido!",bg="#202020", fg="red")                        
    if __name__ == "__main__":
        root = tk.Tk()
        app = ValueConverter(root)
        root.mainloop()
def calcolatrice2():
    sys.set_int_max_str_digits(2147483647)
    root = tk.Tk()
    root.config(bg="#202020")
    root.title("Sigma Calcolatrice")
    root.geometry("600x400")
    cronology = []
    def calculate(event=None):
        exp = input_entry.get()
        history_text.config(state="normal")
        try:
            if exp == "delcronology":
                cronology.clear()
                history_text.delete('1.0', tk.END)
                return
            if "0^0" in exp or "0**0" in exp:
                result = "indeterminato"
            else:
                safe_exp = exp.replace("^", "**").replace("x", "*").replace(",", ".").replace(":", "/").replace("[","(").replace("]",")").replace("{","(").replace("}",")")
                result = eval(safe_exp)
            result_text = f"{exp} = {result}"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        except ZeroDivisionError:
            result_text = f"{exp} = Errore: divisione per zero"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        except RecursionError:
            result_text = f"{exp} = Errore: scadenza calcolo"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        except (SyntaxError, NameError, TypeError, ValueError):
            result_text = f"{exp} = Errore: espressione non valida"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        except OverflowError:
            result_text = f"{exp} = Errore: numero troppo grande"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        except Exception as e:
            result_text = f"{exp} = Errore generico: {str(e)}"
            cronology.append(result_text)
            history_text.insert(tk.END, result_text + "\n")
        finally:
            history_text.config(state="disabled")
    root.bind("<Return>", calculate)
    titolo = tk.Label(root, text="Calcola di tutto con Sigma...", fg="white", bg="#202020", font=("Calibri", 36))
    titolo.pack(pady=10)
    input_frame = tk.Frame(root, bg="#202020")
    input_frame.pack(pady=10)
    input_entry = tk.Entry(input_frame, width=40, fg="white", bg="#1848ca")
    input_entry.grid(row=0, column=0, padx=5)
    calc_button = tk.Button(input_frame, text="Calcola (o premi Invio)", command=calculate, border=1, fg="white", bg="#1848ca")
    calc_button.grid(row=0, column=2, padx=5)
    history_label = tk.Label(root, text="Cronologia:", fg="white", bg="#202020")
    history_label.pack()
    history_text = scrolledtext.ScrolledText(root, width=230, height=50, fg="white", bg="#202020", state="disabled")
    history_text.pack()
    root.mainloop()
def TavolaNumeriPrimi2():
    root = tk.Tk()
    root.config(bg="#202020")
    root.title("Sigma Tavola Numeri Primi")
    root.geometry("600x400")
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    def find_primes(limit):
        primes = []
        for num in range(2, limit + 1):
            if is_prime(num):
                primes.append(num)
        return primes
    limit = 500
    primes = find_primes(limit)
    titolo = tk.Label(root, text="Una bella tavolozza di numeri primi!", fg="white", bg="#202020", font=("Calibri", 36))
    titolo.pack(pady=10)
    history_text = scrolledtext.ScrolledText(root, width=230, height=50, fg="white", bg="#202020")
    history_text.pack(pady=10)
    history_text.insert(tk.END,str(primes).replace("[","").replace("]","").replace(",",";"))
    history_text.config(state="disabled")
    def genera_altri_primi():
        nonlocal limit, primes
        limit += 500
        primes = find_primes(limit)
        history_text.config(state="normal")
        history_text.delete('1.0', tk.END)
        history_text.insert(tk.END,str(primes).replace("[","").replace("]","").replace(",",";"))
        history_text.config(state="disabled")
    calc_button2 = tk.Button(root, text="Genera altri numeri!", command=genera_altri_primi, border=1, fg="white", bg="#1848ca")
    calc_button2.pack(pady=10)
logoi = tk.PhotoImage(file="logo2.png")
saluto = random.choice(["Ciao, genio matematico!",
                        "Pronto a copiare per matematica?",
                        "Mi piace un po' più l'italiano che la matematica.",
                        """Quest'app è italiana, ma ha il nome di una lettera greca (non potevo chiamarla "Esse").""",
                        "L'ha inventata qualcuno tanto per fare qualcosa.",
                        "Ti piace l'algebra?",
                        "Confronto di bonta': pasta_carbonara = pizza_norma_con_wurstel",
                        "La calcolatrice piu' potente al... beh... in citta'?!",
                        "Senza IA GPT, sono intelligente lo stesso.",
                        ":)",
                        "Conosci le tabelline?",
                        "Teorema della follia: ananas + pizza",
                        "Viva l'ultranormale!",
                        "Mi ha inventato un ragazzino di 12 anni. Non fate domande.",
                        "CPU: Pronta al 100%, GPU: Pronta al 100%, Disco: Pronto al 100%, voglia di lavorare: Pari allo 0%",
                        "Made in Italy (Sono pregiato, per intenderci)",
                        "Ehi, capitano!",
                        "2 + 2 = 5"])
esteticoFrame = tk.Frame(bg="#020002",height=30)
esteticoFrame.grid(column=0,row=0,sticky="ew")
logo = tk.Label(image=logoi, text=saluto, font=("Courier New",18), bg="#202020",fg="white", compound="left")
logo.grid(column=0,row=1,sticky="w")
w.columnconfigure(0, weight=1)
container = tk.Frame(w)
container.grid(column=0, sticky="ew")
container.grid_columnconfigure(0, weight=1)
canvas = tk.Canvas(container, bg="#323232")
scrollbar = tk.Scrollbar(container, orient="horizontal", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#202020")
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=scrollable_frame, anchor="center")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.grid(sticky="ew")
canvas.grid_columnconfigure(0, weight=1)
scrollbar.grid(sticky="ew")
calcolatricei = tk.PhotoImage(file="calculator.png")
calcolatrice = tk.Button(scrollable_frame, text="Calcolatrice", image=calcolatricei, compound="top", font=("Courier New",18),fg="white",bg="#1c2b53",command=calcolatrice2)
calcolatrice.grid(sticky="ew")
convertitorei = tk.PhotoImage(file="convertitore.png")
convertitore = tk.Button(scrollable_frame, text="Convertitore Valori", image=convertitorei, compound="top", font=("Courier New",18),fg="white",bg="#005643",command=convertitore2)
convertitore.grid(sticky="ew")
TavolaNumeriPrimii = tk.PhotoImage(file="tavolenumeriprimi.png")
TavolaNumeriPrimi = tk.Button(scrollable_frame, text="Tavola di Numeri Primi", image=TavolaNumeriPrimii, compound="top", font=("Courier New",18),fg="white",bg="#A7A072",command=TavolaNumeriPrimi2)
TavolaNumeriPrimi.grid(sticky="ew")
memoi = tk.PhotoImage(file="memo.png")
memo = tk.Button(scrollable_frame, text="Memo", image=memoi, compound="top", font=("Courier New",18),fg="white",bg="#8F8F8F",command=memo2)
memo.grid(sticky="ew")
updatefestival = open("updatefestival.sgms","r")
exec(updatefestival.read())
updatefestival.close()
ulissesistema_image = tk.PhotoImage(file="ulissesistema.png")
license_ = tk.Label(image=ulissesistema_image, text="Sigma, ulissesistema, applicazione Open Source sotto licenza MIT\nNon fare caso all'ironia del programmatore, cioè il celebre ulissesistema,\ninoltre il programmatore non si chiama davvero ulissesistema\nma Casto Nicolò Corrado.", font=("Courier New",12), bg="#202020",fg="white", compound="top")
license_.grid(column=0,sticky="ew",pady=10)
w.mainloop()
