import tkinter as tk
from tkinter import filedialog, messagebox

class WordCollectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unique Word Collector Pro")
        self.root.geometry("500x400")
        
        # Data Storage
        self.unique_words = set()

        # UI Setup
        self.setup_ui()

    def setup_ui(self):
        """Initializes all GUI components."""
        # Input Section
        self.prompt_label = tk.Label(self.root, text="Paste text below or upload a file", font=("Arial", 10, "bold"))
        self.prompt_label.pack(pady=10)

        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        self.add_btn = tk.Button(btn_frame, text="Process Text", command=self.process_manual_input, bg="#e1e1e1")
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.upload_btn = tk.Button(btn_frame, text="Upload .txt File", command=self.upload_file, bg="#d1e7dd")
        self.upload_btn.pack(side=tk.LEFT, padx=5)

        self.clear_btn = tk.Button(btn_frame, text="Clear All", command=self.clear_data, bg="#f8d7da")
        self.clear_btn.pack(side=tk.LEFT, padx=5)

        # Statistics Display
        self.result_label = tk.Label(self.root, text="Total unique words: 0", font=("Arial", 12))
        self.result_label.pack(pady=20)

    def _update_unique_words(self, raw_text):
        """Internal helper to clean and add words to the set."""
        words = raw_text.lower().split()
        # Clean punctuation from words
        cleaned_words = [word.strip('.,!?:;"()') for word in words]
        for word in cleaned_words:
            if word: # Ensure it's not an empty string
                self.unique_words.add(word)
        
        self.result_label.config(text=f"Total unique words: {len(self.unique_words)}")

    def process_manual_input(self):
        """Handles text entered in the text box."""
        text = self.text_area.get("1.0", tk.END).strip()
        if text:
            self._update_unique_words(text)
            self.text_area.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter some text first!")

    def upload_file(self):
        """ Opens a file dialog and processes a .txt file. """
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self._update_unique_words(content)
                messagebox.showinfo("Success", f"File processed: {file_path.split('/')[-1]}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file: {e}")

    def clear_data(self):
        """ Resets the unique word set and the display. """
        self.unique_words.clear()
        self.result_label.config(text="Total unique words: 0")
        messagebox.showinfo("Reset", "All data has been cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WordCollectorApp(root)
    root.mainloop()