import matplotlib.pyplot as plt
import numpy as np

# 1. Линейный график
def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y, label='Sine Wave')
    plt.title('Line Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# 2. Гистограмма
def histogram():
    data = np.random.randn(1000)
    plt.hist(data, bins=30, edgecolor='black')
    plt.title('Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# 3. Круговая диаграмма (Pie Chart)
def pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # Выделение сектора B
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Pie Chart')
    plt.axis('equal')  # Сделать круг
    plt.show()

# 4. Диаграмма рассеяния (Scatter Plot)
def scatter_plot():
    x = np.random.rand(50)
    y = np.random.rand(50)
    sizes = 1000 * np.random.rand(50)
    colors = np.random.rand(50)
    plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')
    plt.title('Scatter Plot')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.grid(True)
    plt.colorbar()  # Показать цветовую шкалу
    plt.show()

# 5. Столбчатая диаграмма (Bar Plot)
def bar_plot():
    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [23, 45, 56, 78]
    plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'])
    plt.title('Bar Plot')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.grid(True)
    plt.show()

# Основная функция, которая вызывает все графики
def main():
    line_plot()
    histogram()
    pie_chart()
    scatter_plot()
    bar_plot()

if __name__ == "__main__":
    main()
