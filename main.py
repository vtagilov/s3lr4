import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns

f = open("imdb_top_1000.csv", "r")
df = pd.read_csv(f, sep=',')
f.close()
df['Released_Year'] = df['Released_Year'].astype('int')
df["Meta_score"] = df["Meta_score"].astype('float64')
df['IMDB_Rating'] = df['IMDB_Rating'].astype('float64')
YEARS_AVERAGE = 5


print(df.info())
pd.set_option('display.max_columns', None)
print(df.head(3))


sns.displot(data=df, x='Released_Year')
plt.title('Total Released Movie by Date', fontsize=18)
plt.subplots_adjust(top=0.9)
plt.show()


genres_list = []
for i in df['Genre']:
    genres_list.extend(i.split(', '))

df_plot = pd.DataFrame(Counter(genres_list).most_common(5), columns=['Genre', 'total'])
sns.barplot(data=df_plot, x='Genre', y='total')
plt.title('Top 5 Genres in Movies', fontsize=18)
plt.show()


years = []
years_imdb = []
years_meta = []
rating_imdb = []
rating_meta = []
temp_imdb = 0
temp_meta = 0
usedYears_imdb = 0
usedYears_meta = 0
for i in range(1930, 2020):
    tdf = df.loc[df["Released_Year"] == i]
    if tdf["IMDB_Rating"].mean() != 0:
        usedYears_imdb += 1
        temp_imdb += tdf["IMDB_Rating"].mean()
    if tdf["Meta_score"].mean() != 0:
        usedYears_meta += 1
        temp_meta += tdf["Meta_score"].mean()
    if i % YEARS_AVERAGE == 0:
        rating_imdb.append(temp_imdb/usedYears_imdb)
        rating_meta.append(temp_meta/usedYears_meta/10)
        years.append(i)
        temp_imdb = 0
        temp_meta = 0
        usedYears_imdb = 0
        usedYears_meta = 0

sns.lineplot(x=years, y=rating_imdb, legend='brief', label="IMDB score")
sns.lineplot(x=years, y=rating_meta, legend='brief', label="Meta score")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.title('Average rating films by years', fontsize=18)
plt.gcf().autofmt_xdate()
plt.show()

years = []
badFilms_imdb = []
badFilms_meta = []
MAX_BAD_FILM_SCORE = 6
temp = 0
for i in range(1930, 2020):

    tdf = df.loc[df["Released_Year"] == i]
    tdf_meta = tdf.loc[tdf["Meta_score"] < MAX_BAD_FILM_SCORE * 10]
    temp += tdf_meta["Meta_score"].count()
    if i % YEARS_AVERAGE == 0:
        badFilms_meta.append(temp)
        years.append(i)
        temp = 0

sns.barplot(x=years, y=badFilms_meta)
plt.gcf().autofmt_xdate()
plt.title('Failed films by years', fontsize=18)
plt.show()
#
