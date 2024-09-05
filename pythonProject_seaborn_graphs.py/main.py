import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Загружаем стандартные датасеты для примеров
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
flights = sns.load_dataset('flights')

# 1. Гистограмма (Histogram)
def histogram():
    sns.histplot(tips['total_bill'], bins=30, kde=True)
    plt.title('Histogram of Total Bill with KDE')
    plt.xlabel('Total Bill')
    plt.ylabel('Frequency')
    plt.show()

# 2. Диаграмма рассеяния (Scatter Plot)
def scatter_plot():
    sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=iris)
    plt.title('Scatter Plot of Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.legend(title='Species')
    plt.show()

# 3. Тепловая карта (Heatmap)
def heatmap():
    flights_pivot = flights.pivot(index='month', columns='year', values='passengers')
    sns.heatmap(flights_pivot, annot=True, fmt='d', cmap='YlGnBu')
    plt.title('Heatmap of Flight Passengers')
    plt.show()

# 4. Boxplot
def boxplot():
    sns.boxplot(x='day', y='total_bill', data=tips, palette='Set3', hue='day', legend=False)
    plt.title('Boxplot of Total Bill by Day')
    plt.xlabel('Day')
    plt.ylabel('Total Bill')
    plt.show()

# 5. Парные графики (Pairplot)
def pairplot():
    sns.pairplot(iris, hue='species', palette='bright')
    plt.suptitle('Pairplot of Iris Dataset', y=1.02)
    plt.show()

# Основная функция, которая вызывает все графики
def main():
    histogram()
    scatter_plot()
    heatmap()
    boxplot()
    pairplot()

if __name__ == "__main__":
    main()




