import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # create figure and axis
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.plot(df.index, (df['value']))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # copy_df
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_pivot = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot.columns = [month_names[m-1] for m in df_pivot.columns]
    # create figures and columns
    # plot as grouped bar graph
    fig, ax = plt.subplots(figsize=(12, 7))
    df_pivot.plot(kind='bar', ax=ax)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # copy_df
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month
    month_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month_abbr'] = df_box['month'].apply(lambda m: month_abbr[m-1])
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(data=df_box, x='month_abbr', y='value', order=month_abbr, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    fig.tight_layout()
    fig.savefig('box_plot.png')
    return fig
