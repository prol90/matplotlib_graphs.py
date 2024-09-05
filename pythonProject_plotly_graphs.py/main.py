import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd


# 1. Линейный график (Line Plot)
def line_plot():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Sine Wave'))
    fig.update_layout(title='Line Plot', xaxis_title='X Axis', yaxis_title='Y Axis')
    fig.show()


# 2. Гистограмма (Histogram)
def histogram():
    data = np.random.randn(1000)

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data, nbinsx=30))
    fig.update_layout(title='Histogram', xaxis_title='Value', yaxis_title='Frequency')
    fig.show()


# 3. Круговая диаграмма (Pie Chart)
def pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    fig = go.Figure(data=[go.Pie(labels=labels, values=sizes, hole=.3)])
    fig.update_layout(title='Pie Chart')
    fig.show()


# 4. Диаграмма рассеяния (Scatter Plot)
def scatter_plot():
    df = px.data.iris()

    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species',
                     title="Scatter Plot of Sepal Width vs Sepal Length")
    fig.show()


# 5. 3D-график (3D Surface Plot)
def surface_plot():
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x ** 2 + y ** 2))

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
    fig.update_layout(title='3D Surface Plot', scene=dict(
        xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
    fig.show()


# Основная функция, которая вызывает все графики
def main():
    line_plot()
    histogram()
    pie_chart()
    scatter_plot()
    surface_plot()


if __name__ == "__main__":
    main()

