# import tkinter as tk
# from tkinter import ttk


# # root window
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Spinbox Demo')

# # Spinbox
# current_value = tk.StringVar(value=0)
# spin_box = ttk.Spinbox(
#     root,
#     from_=0,
#     to=30,
#     textvariable=current_value,
#     wrap=True)

# spin_box.pack()

# root.mainloop()


# import string # it is built-in lib
# # print(string.ascii_lowercase)
# print (string.ascii_letters)



# def dont_give_me_five(start,end):
#     n = 0
#     for i in range(start,end + 1):
#         AlWeggehaald = 0
#         for x in str(i):
#             Test = str(x)
#             if Test == "5":
#                 n -= 1
#                 AlWeggehaald += 1
#         if AlWeggehaald > 0:
#             n += AlWeggehaald - 1
            
#         n += 1

#     return n   # amount of numbers


# TEst = 5434
# if "5" not in str(TEst):
#     print ("test")
import tkinter as tk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')


Test = tk.StringVar(value=False)
NieuwWoord = Test.get()
print (NieuwWoord)


root.mainloop()