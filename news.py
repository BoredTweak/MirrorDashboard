from newsapi import NewsApiClient
with open('credentials.config', 'r') as config:
    credentials=config.read().replace('\n','')

newsapi = NewsApiClient(api_key = credentials)
top_headlines = newsapi.get_top_headlines(country='us')

articles = top_headlines['articles']

#print articles[0]
   
taglines = [ (o['title'], o['source']['name']) for o in articles]
print taglines