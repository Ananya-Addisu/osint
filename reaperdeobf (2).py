import tkinter as tk
from tkinter import filedialog, messagebox
import PyObfuscator
class Obfuscator:
    def __init__(self, master):
        self.master = master
        master.title("ReaperObfuscator(beta)")

        # Create input file label and button
        self.input_label = tk.Label(master, text="Выберите скрипт для обфускации:")
        self.input_label.pack()
        self.input_button = tk.Button(master, text="Обзор", command=self.select_input_file)
        self.input_button.pack()

        # Create output file label and button
        self.output_label = tk.Label(master, text="Выберите конечный файл:")
        self.output_label.pack()
        self.output_button = tk.Button(master, text="Обзор", command=self.select_output_file)
        self.output_button.pack()

        # Create obfuscate button
        self.obfuscate_button = tk.Button(master, text="Обфусцировать", command=self.obfuscate_script)
        self.obfuscate_button.pack()

    def select_input_file(self):
        self.input_file = filedialog.askopenfilename(title="Выберите скрипт для обфускации:", filetypes=[("Python files", "*.py")])

    def select_output_file(self):
        self.output_file = filedialog.asksaveasfilename(title="Выберите конечный файл:", filetypes=[("Python files", "*.py")])

    def obfuscate_script(self):
        if not hasattr(self, 'input_file') or not hasattr(self, 'output_file'):
            messagebox.showerror("Error", "Пожалуйста, выберите оба файла ввода и вывода")
            return

        with open(self.input_file, 'r') as f:
            script = f.read()

        obfuscated_script = PyObfuscator.obfuscate(script)

        with open(self.output_file, 'w') as f:
            f.write(obfuscated_script)

        messagebox.showinfo("Отлично!", "Твой код успешно обфусцирован!")

root = tk.Tk()
obfuscator = Obfuscator(root)
root.mainloop()
