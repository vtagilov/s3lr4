import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

f = open("imdb_top_1000.csv", "r")
df = pd.read_csv(f, sep=',')
f.close()
print(df.head(5))
print(df.columns)
df['Released_Year'] = df['Released_Year'].astype('int')
df['IMDB_Rating'] = df['IMDB_Rating'].astype('float64')
sns.displot(data=df, x='Released_Year', kde=True, color='#fdc100', facecolor='#06837f')
plt.title('Total Released Movie by Date', fontsize=18, weight=600)
plt.show()

genres_list = []
for i in df['Genre']:
    genres_list.extend(i.split(', '))

df_plot = pd.DataFrame(Counter(genres_list).most_common(5), columns=['Genre', 'total'])
sns.barplot(data=df_plot, x='Genre', y='total')
plt.title('Top 5 Genres in Movies', fontsize=18, weight=600, color='#333d29')
plt.show()

years = []
years2 = []
rating = []

for i in range(1920, 2020):
    tdf = df.loc[df["Released_Year"] == i]
    years.append(i)
    rating.append(tdf["IMDB_Rating"].mean())

sns.barplot(x=years, y=rating)
plt.title('Average rating films by years', fontsize=18, weight=600, color='#333d29')
plt.show()
