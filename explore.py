import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_variable_pairs(df):
    sns.set(style="whitegrid")

# Create subplots for regression plots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))

# List of independent variables
    independent_variables = ['Bedroom Count', 'Bathroom Count', 'Finished Square Feet', 'Year Built', 'Tax Amount']

    for col, ax in zip(independent_variables, axes.flatten()):
        sns.regplot(data=df, x=col, y='Tax Value', ax=ax)
        ax.set_title(f'Regression Plot: {col} vs. Tax Value')
    fig.delaxes(axes[2, 1])
    plt.tight_layout()
    plt.show()

    # Create a boxplot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='FIPS', y='Tax Value', data=df)
    plt.title('Boxplot: FIPS vs. Tax Value')
    plt.show()

    plt.figure(figsize=(20, 10))
    ax=sns.barplot(x='Property Land Use', y='Tax Value', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
    plt.title('Boxplot: Property Land Use vs. Tax Value')
    plt.show()


def heat_map(df):
    df=df.drop(columns=['FIPS','Property Land Use']).corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(df, cmap='Reds',annot=True,mask=np.triu(df))
    plt.show()
