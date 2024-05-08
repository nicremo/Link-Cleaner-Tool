import tkinter as tk
from tkinter import filedialog, messagebox, Label, Entry, Button, Checkbutton, IntVar
import pandas as pd
from urllib.parse import urlparse

class LinkCleanerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Link Cleaner Tool')

        # UI Components
        Label(root, text="Select CSV files", pady=10).pack()
        Button(root, text="Choose Files", command=self.load_files).pack(pady=5)

        self.filter_var = tk.StringVar()
        self.filter_entry = Entry(root, textvariable=self.filter_var, width=50)
        self.filter_entry.pack(pady=10)
        Label(root, text="Enter custom filter text (URLs containing):").pack()

        # Checkboxes for predefined filters
        self.reddit_var = IntVar()
        self.duplicates_var = IntVar()
        Checkbutton(root, text="Filter out Reddit links", variable=self.reddit_var).pack(anchor=tk.W)
        Checkbutton(root, text="Remove duplicates", variable=self.duplicates_var).pack(anchor=tk.W)

        self.save_btn = Button(root, text="Clean Links and Save", command=self.process_files)
        self.save_btn.pack(pady=20)

        self.file_paths = []

    def load_files(self):
        self.file_paths = filedialog.askopenfilenames(filetypes=[("CSV files", "*.csv")])
        if not self.file_paths:
            messagebox.showerror("Error", "No files selected. Please select CSV files.")

    def process_files(self):
        if not self.file_paths:
            messagebox.showerror("Error", "Please load files first!")
            return

        all_urls = pd.DataFrame()

        for file_path in self.file_paths:
            try:
                data = pd.read_csv(file_path, header=None)

                # Apply predefined filters
                if self.reddit_var.get():
                    data = data[~data[0].str.contains('reddit', case=False, na=False)]

                # Apply custom filter text
                filter_text = self.filter_var.get().strip()
                if filter_text:
                    data = data[data[0].str.contains(filter_text, case=False, na=False)]

                all_urls = pd.concat([all_urls, data], ignore_index=True)

            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while processing the file: {file_path}\n{e}")
                return

        # Remove duplicates if selected
        if self.duplicates_var.get():
            all_urls = all_urls.drop_duplicates()

        # Clean and save the URLs to a .txt file
        self.save_cleaned_urls(all_urls)

      
    def save_cleaned_urls(self, all_urls):
            try:
                base_urls = set()
                for url in all_urls[0]:
                    parsed_url = urlparse(url)
                    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    base_urls.add(base_url)

                cleaned_urls = list(base_urls)

                # Dateiname und Speicherort vom Benutzer wählen lassen
                file_name = filedialog.asksaveasfilename(
                    defaultextension=".txt",
                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                    title="Save cleaned URLs"
                )

                # Wenn der Benutzer den Dialog abbricht, wird file_name None sein
                if file_name:
                    with open(file_name, 'w') as f:
                        for url in cleaned_urls:
                            f.write(f"{url}\n")

                    messagebox.showinfo("Success", f"Cleaned URLs saved to '{file_name}'")
                else:
                    messagebox.showwarning("Cancelled", "Save operation cancelled.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while saving the URLs: {e}")
        

if __name__ == "__main__":
    root = tk.Tk()
    app = LinkCleanerApp(root)
    root.geometry("500x300")
    root.mainloop()