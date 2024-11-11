import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_KEY = '75973fbca10d8c87c7ba'

def translate_text():
    source_lang = source_language.get()
    target_lang = target_language.get()
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        messagebox.showerror("Input Error", "Please enter text to translate.")
        return

    url = f"https://api.mymemory.translated.net/get?q={text}&langpair={source_lang}|{target_lang}&key={API_KEY}"

    try:
        response = requests.get(url)
        response_data = response.json()

        if 'responseStatus' in response_data and response_data['responseStatus'] != 200:
            messagebox.showerror("Translation Error", response_data['responseDetails'])
        else:
            translated_text = response_data['responseData']['translatedText']
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

app = tk.Tk()
app.title("Text Translator")
app.geometry("500x500")
app.configure(bg="#30475E")

title_label = tk.Label(app, text="Text Translator", font=("Arial", 16, "bold"), bg="#30475E", fg="#F5F5F5")
title_label.pack(pady=(10, 0))

input_text = tk.Text(app, height=8, width=50, font=("Arial", 12), bg="#F5F5F5", fg="#333333", bd=0)
input_text.pack(pady=(20, 10))

frame = tk.Frame(app, bg="#30475E")
frame.pack(pady=10)

source_language = ttk.Combobox(frame, values=["en", "es", "fr", "de"], width=10)
source_language.set("en")
source_language.pack(side="left", padx=5)

target_language = ttk.Combobox(frame, values=["en", "es", "fr", "de"], width=10)
target_language.set("es")
target_language.pack(side="left", padx=5)

translate_button = tk.Button(app, text="Translate", command=translate_text, font=("Arial", 12), bg="#F05454", fg="#F5F5F5", activebackground="#D94343", activeforeground="#F5F5F5", bd=0, padx=10, pady=5)
translate_button.pack(pady=10)

output_text = tk.Text(app, height=8, width=50, font=("Arial", 12), bg="#F5F5F5", fg="#333333", bd=0)
output_text.pack(pady=(10, 20))

app.mainloop()
