import tkinter as tk
from tkinter import messagebox

def copy_and_cut():
    try:
        # Open the txt and read a txt
        with open('main.txt', 'r') as file: # You can change your txt name
            data = file.readlines()

        # Specify the range of rows to import
        start = 0
        finish = 4  # Since we count from 0, 4 takes the 5th row

        # Get data in specified range
        received_data = ''.join(data[start:finish+1])

        # Copy data to clipboard
        root.clipboard_clear()
        root.clipboard_append(received_data)
        root.update()

        # Delete received data from file
        with open('main.txt', 'w') as file: # You can change your txt name
            file.writelines(data[finish+1:])

    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

root = tk.Tk()
root.title("Copying and Deleting Data")

etiket = tk.Label(root, text="Copy and Delete Data")
etiket.pack(pady=10)

kopyala_dugme = tk.Button(root, text="Copy and Delete", command=copy_and_cut)
kopyala_dugme.pack()

cikis_dugme = tk.Button(root, text="Exit", command=root.quit)
cikis_dugme.pack()

root.mainloop()
