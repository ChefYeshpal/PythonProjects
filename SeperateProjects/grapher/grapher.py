import matplotlib.pyplot as plt

def get_points():
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
    return points

def plot_points(points):
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]

    plt.scatter(x_vals, y_vals)
    plt.title('Plot of Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def main():
    points = get_points()
    if points:
        plot_points(points)
    else:
        print("No points to plot.")

if __name__ == "__main__":
    main()

