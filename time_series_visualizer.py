import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def get_cleaned_data():
    """Carga y limpia los datos de acuerdo con los criterios especificados."""
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) & 
            (df['value'] <= df['value'].quantile(0.975))]
    return df

def draw_line_plot():
    # Obtener datos limpios
    df = get_cleaned_data()

    # Crear gráfico de línea
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    return fig

def draw_bar_plot():
    # Obtener datos limpios
    df = get_cleaned_data()

    # Preparar datos para el gráfico de barras
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    # Crear gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(15, 10)).figure
    plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June',
                                       'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')

    return fig

def draw_box_plot():
    # Obtener datos limpios
    df = get_cleaned_data()

    # Preparar datos para gráficos de caja
    df['year'] = df.index.year
    df['month'] = df.index.strftime('%b')
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Crear gráficos de caja
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    
    # Diagrama de caja por año
    sns.boxplot(x='year', y='value', data=df, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Diagrama de caja por mes
    sns.boxplot(x='month', y='value', data=df, order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    return fig
