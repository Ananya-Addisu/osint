import tkinter as tk
from tkinter import filedialog
import os
import random
import string

def obfuscate_file(file_path, output_path=None):
    """
    Обфусцирует Python файл.

    Args:
        file_path: Путь к исходному файлу.
        output_path: Путь к выходному файлу (необязательно).
    """

    if output_path is None:
        output_path = file_path.replace(".py", "_obfuscated.py")

    with open(file_path, "r") as f:
        code = f.read()

    variables = [var for var in code.split() if var.startswith("_") or var.isalpha()]
    for var in variables:
        if not var.startswith("_"):
            new_var = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
            code = code.replace(var, new_var)

    functions = [func for func in code.split() if func.endswith("(")]
    for func in functions:
        new_func = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        code = code.replace(func, new_func)

    classes = [cls for cls in code.split() if cls.startswith("class")]
    for cls in classes:
        new_cls = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
        code = code.replace(cls, new_cls)

    with open(output_path, "w") as f:
        f.write(code)

class ObfuscatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Reaper Obfuscator")

        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        self.input_file_label = tk.Label(input_frame, text="Исходный файл:")
        self.input_file_label.pack(side=tk.LEFT)

        self.input_file_path = tk.StringVar(input_frame)
        self.input_file_path.set("Файл не выбран")
        self.input_file_entry = tk.Entry(input_frame, textvariable=self.input_file_path, state="readonly")
        self.input_file_entry.pack(side=tk.LEFT)

        browse_button = tk.Button(input_frame, text="Обзор...", command=self.select_input_file)
        browse_button.pack(side=tk.LEFT)

        output_frame = tk.Frame(master)
        output_frame.pack(pady=10)

        self.output_file_label = tk.Label(output_frame, text="Выходной файл:")
        self.output_file_label.pack(side=tk.LEFT)

        self.output_file_path = tk.StringVar(output_frame)
        self.output_file_path.set("...")
        self.output_file_entry = tk.Entry(output_frame, textvariable=self.output_file_path, state="readonly")
        self.output_file_entry.pack(side=tk.LEFT)

        browse_output_button = tk.Button(output_frame, text="Обзор...", command=self.select_output_file)
        browse_output_button.pack(side=tk.LEFT)

        obfuscate_button = tk.Button(master, text="Обфусцировать", command=self.obfuscate)
        obfuscate_button.pack(pady=10)

        self.result_frame = tk.Frame(master)
        self.result_label = tk.Label(self.result_frame, text="")
        self.result_label.pack()
        self.result_frame.pack(pady=10)

    def select_input_file(self):
        """Открывает диалоговое окно для выбора исходного файла."""
        file_path = filedialog.askopenfilename(initialdir=".", title="Выберите исходный файл", filetypes=(("Python files", "*.py"), ("All files", "*.*")))
        self.input_file_path.set(file_path)

    def select_output_file(self):
        """Открывает диалоговое окно для выбора выходного файла."""
        file_path = filedialog.asksaveasfilename(initialdir=".", title="Выберите выходной файл", defaultextension=".py")
        self.output_file_path.set(file_path)

    def obfuscate(self):
        """Обфусцирует выбранный файл."""
        input_file = self.input_file_path.get()
        output_file = self.output_file_path.get()

        if not input_file:
            self.result_label.config(text="Не выбран исходный файл.")
            return

        if not output_file:
            output_file = None

        try:
            obfuscate_file(input_file, output_file)
            self.result_label.config(text=f"Файл {os.path.basename(input_file)} успешно обфусцирован!")
        except Exception as e:
            self.result_label.config(text=f"Ошибка: {e}")

root = tk.Tk()
app = ObfuscatorApp(root)
root.mainloop()