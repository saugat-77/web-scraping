import bs4
import requests
import pandas as pd

req = requests.get('https://www.imdb.com/chart/top')
soup = bs4.BeautifulSoup(req.text ,'html.parser')
#print(soup)

name_year_container = soup.find_all("td", class_="titleColumn")
names = [i.a.text for i in name_year_container]

years = [i.span.text for i in name_year_container]

rating_container = soup.find_all('td', class_='ratingColumn imdbRating')
ratings = [i.strong.text for i in rating_container] #td>strong

df = pd.DataFrame({
    'Names': names,
    'Years': years,
    'Ratings': ratings,
})
#print(df)
print(df.head())
df.to_csv('IMDb.csv', index=False)
