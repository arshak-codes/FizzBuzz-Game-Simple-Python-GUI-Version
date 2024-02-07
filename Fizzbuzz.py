import tkinter as tk

def fizzbuzz(num):
    if num%3==0 and num%5==0:
        return("FizzBuzz!")
    elif num%3==0:
        return("Fizz")
    elif num%5==0:
        return("Buzz")
    else:
        return str(num)
    
def submitbut():
    try:
        usrinput = int(entry.get())
        result = fizzbuzz(usrinput)
        result_label.config(text = result)
    except ValueError:
        result_label.config(text="Invalid Input!")
    #main window
window = tk.Tk()
window.title("FizzBuzz Game")
    
#widgets
label = tk.Label(window,text="Enter a number")
label.pack(pady=10)
    
entry = tk.Entry(window)
entry.pack(pady=10)
    
submit_button = tk.Button(window,text="Submit",command=submitbut)
submit_button.pack(pady=10)
    
result_label = tk.Label(window,text="")
result_label.pack(pady=10)

window.mainloop()
    