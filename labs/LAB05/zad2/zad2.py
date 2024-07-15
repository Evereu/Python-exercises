import pandas as pd
import matplotlib.pyplot as plt


def imdb():

    csv = pd.read_csv('imdb_top_1000.csv')

    csv['Gross'] = csv['Gross'].str.replace(',', '').astype(float)

    pd.options.display.float_format = '{:.2f}'.format

    mean_gross_by_genre = csv.groupby('Genre')['Gross'].mean().sort_values(ascending=False)

    plt.figure(figsize=(14, 6))
    mean_gross_by_genre.plot(kind='bar', color='skyblue')
    plt.title('Średnie zarobki filmów według gatunku')
    plt.xlabel('Gatunek filmu')
    plt.ylabel('Średnie zarobki w $')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

    q3 = csv['Gross'].quantile(0.75)

    my_filtered_data = mean_gross_by_genre[mean_gross_by_genre>q3]

    plt.figure(figsize=(12, 6))
    my_filtered_data.plot(kind='bar', color='skyblue')
    plt.title('Średnie zarobki filmów według gatunku')
    plt.xlabel('Gatunek filmu')
    plt.ylabel('Średnie zarobki w $')
    plt.xticks(rotation=45, fontsize=8, ha='right')
    plt.ticklabel_format(axis='y', style='plain')
    plt.ylim(min(mean_gross_by_genre) * 0.9, max(mean_gross_by_genre)* 1.1)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

imdb()



















