from tkinter import *

# Initialize the main window
window = Tk()
window.geometry("400x500")
window.title("Calculator")
window.configure(background="gray")

# Create the entry screen at the top of the window
entry=Entry(window, width=16, font=("Arial", 24), bd=10, relief="sunken", justify="right", background="lightgray")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.insert(0, "")

# Function to update the screen with button presses
def button_click(number):
    current = entry.get()

    # Check if it is the percentage button
    if number == "%":
        current = str(float(current) / 100) # Calculate percentage by dividing by 100
    else:
        current += number # Append the number to the current entry

    entry.delete(0, END)
    entry.insert(0, current)

# Function to clear the screen
def clear():
    entry.delete(0, END)

# Function to evaluate the expression
def evaluate():
    try:
        # Replace "x" with "*" for multiplication
        expression = entry.get().replace("x","*")
        result = str(eval(expression)) # Using eval to calculate the expression
        entry.delete(0, END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, END)
        entry.insert(0, "Error")



# Button definitions in a list to loop through (without calculation functions)
buttons = [
    ("7", 1, 0,), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("6", 2, 0), ("5", 2, 1), ("4", 2, 2), ("x", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("Clr", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("=", 5, 0), ("%", 5, 1), ("(", 5, 2), (")", 5, 3)
]

# Creating the buttons and placing them using grid (no functionality for now)
for (text, row, col) in buttons:
    if text == "=":
        button=Button(window, text=text, width=10, height=3, relief="solid", command=evaluate)
    elif text == "Clr":
        button=Button(window, text=text, width=10, height=3, relief="solid", command=clear)
    else:
        button=Button(window, text=text, width=10, height=3, relief="solid", command=lambda number=text: button_click(number))

    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make the window resizeable, so that buttons stretch properly
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)




# Start the main loop
window.mainloop()
