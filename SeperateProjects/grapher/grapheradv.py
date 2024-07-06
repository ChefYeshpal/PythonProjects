'''
this is a more advanced program for grapher that can also map trignometric and quadratic inputs
created: 14:03:23 6 July 2024
Author: github.com/ChefYeshpal

to do:
	1. trig waves with values can also be generated
	2. multiple trig waves can be generated in one graph
	3. more than 2 degree quadratic eq's can be solved

'''

import matplotlib.pyplot as plt
import numpy as np


#for points
def plot_points():
    points = []
    print("Enter points as x,y pairs. Type 'done' to finish.")
    while True:
        user_input = input("Enter point (x,y): ")
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.split(','))
            points.append((x, y))
        except ValueError:
            print("Invalid input. Please enter the point as x,y.")
    
    if points:
        x_vals = [point[0] for point in points]
        y_vals = [point[1] for point in points]
        plt.scatter(x_vals, y_vals)
        plt.title('Plot of Points')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)
        plt.show()
    else:
        print("No points to plot.")


#for trignometric functions
def plot_trig_function():
    functions = {
        'sin': np.sin,
        'cos': np.cos,
        'tan': np.tan,
        'csc': lambda x: 1/np.sin(x),
        'sec': lambda x: 1/np.cos(x),
        'cot': lambda x: 1/np.tan(x)
    }

    print("Choose a trigonometric function to plot (sin, cos, tan, csc, sec, cot):")
    func = input().lower()
    if func in functions:
        x = np.linspace(-2*np.pi, 2*np.pi, 1000)
        y = functions[func](x)
        plt.plot(x, y, label=func)
        plt.title(f'Plot of {func}(x)')
        plt.xlabel('X-axis')
        plt.ylabel(f'{func}(x)')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True, which='both')
        plt.legend()
        plt.show()
    else:
        print("Invalid function. Please choose from sin, cos, tan, csc, sec, cot.")


#for quadratic euations
def plot_quadratic():
    print("Enter coefficients for the quadratic equation ax^2 + bx + c = 0:")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        x = np.linspace(-10, 10, 400)
        y = a * x**2 + b * x + c
        plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
        plt.title('Plot of Quadratic Equation')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.axhline(0, color='black',linewidth=0.5)
        plt.axvline(0, color='black',linewidth=0.5)
        plt.grid(True, which='both')
        plt.legend()
        plt.show()
    except ValueError: #in case of space of nonvalue
        print("Invalid input. Please enter numerical values for coefficients.")

#options to graph
def main():
    print("Choose the type of graph you want to plot:")
    print("1. Points")
    print("2. Trigonometric Function")
    print("3. Quadratic Equation")
    choice = input("Enter your choice (1/2/3): ")
    #loop
    if choice == '1':
        plot_points()
    elif choice == '2':
        plot_trig_function()
    elif choice == '3':
        plot_quadratic()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

