import tkinter as tk

root = tk.Tk()
root.title("Canvas Test")
root.geometry("400x400")

label = tk.Label(root, text="Canvas Test", font=("Arial", 18))
label.pack(pady=10)

canvas = tk.Canvas(root, width=300, height=300, bg="green")
canvas.pack()

canvas.create_rectangle(
    50, 50, 150, 150,
    fill="yellow",
    outline="black"
)

canvas.create_oval(
    175, 75, 250, 150,
    fill="black"
)

root.mainloop()