import math
import tkinter
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


#creating a window
top = tkinter.Tk()
top.geometry("400x1000")
top.title('quadratic equation solver')
top.config(bg="black")
#converting into integers
def converting():
	try:
		a_ = int(a.get())
		b_ = int(b.get())
		c_ = int(c.get())

		#calculating delta
		d = (b_**2)-(4*a_*c_)
		delta.config(text=f'Delta: {d}', font=('Arial', 20))

		#check if delta is equal to zero and calculate 
		if d==0:
			x_ = (-b_/2*a_)
			x1 = "%.2f" % x_
			Solution.config(text=f'Solution: {x1}', font=('Arial', 20))
		
		#check if delta is bigger than zero and calculate 
		if d>0:
			x_1_ = ((-b_-math.sqrt(d))/(2*a_))
			x_1 = "%.2f" % x_1_
			x_2_ = ((-b_+math.sqrt(d))/(2*a_))
			x_2 = "%.2f" % x_2_
			Solution.config(text=f'Solutions are : {x_1}, {x_2}', font=('Arial', 20))

		#check if delta is smaller than zero and calculate 
		if d<0:
			Solution.config(text='there is no solution!', font=('Arial', 20))
		
	#excepting the value error		
	except ValueError:
		Is_valid.config(text="please Enter a number !", font=('Arial', 20))
		
def Graph():
	try:
		a_ = int(a.get())
		b_ = int(b.get())
		c_ = int(c.get())
		x = np.linspace(-10, 100, 100)
		y = a_*(x**2)+b_*x+c_

		#creating the graph
		plt.plot(x, y)

		plt.title('Quadratic equation graph')
		plt.xlabel('X values')
		plt.ylabel('Y values')

		plt.show()
		
	#excepting the value error
	except ValueError:
		Is_valid.config(text="please Enter a number !", font=('Arial', 20))


#entering values
a1 = Label(top, text="enter a", font=('Arial', 20))
a1.pack(pady=10)
a1.config(bg="red")

# A entry
a = Entry(top, bd = 5)
a.pack(pady=5)


b1 = Label(top, text="enter b", font=('Arial', 20))
b1.pack(pady=10)
b1.config(bg="red")

#B entry
b = Entry(top, bd = 5)
b.pack(pady=5)


c1 = Label(top, text="enter c", font=('Arial', 20))
c1.pack(pady=10)
c1.config(bg="red")
# C entry
c = Entry(top, bd = 5)
c.pack(pady=5)

#calculate button
calculate_button = Button(top, padx=40, pady=20, text="calculate now !", command=converting, font=('Arial', 20))
calculate_button.pack(pady=20)
calculate_button.config(bg="yellow")

#Graph button
graph_button = Button(top, padx=40, pady=20, text="graph it!", command=Graph, font=('Arial', 20))
graph_button.pack()
graph_button.config(bg="yellow")


#Enter a number label
Is_valid = Label(top, text='', font=('Arial', 20))
Is_valid.pack(pady=20)
Is_valid.config(bg="red")

#delta value
delta = Label(top, text='', font=('Arial', 20))
delta.pack(pady=20)
delta.config(bg="blue")

#Solution
Solution = Label(top, text='', font=('Arial', 20))
Solution.pack(pady=20)
Solution.config(bg="blue")



top.mainloop()
