from newsapi import NewsApiClient
import datetime

indian_news = {'date': 1, 'news': 'null'}
national_news = {'date': 1, 'news': 'null'}
international_news = {'date': 1, 'news': 'null'}
bollywood_news = {'date': 1, 'news': 'null'}
lifestyle_news = {'date': 1, 'news': 'null'}
sport_news = {'date': 1, 'news': 'null'}
business_news = {'date': 1, 'news': 'null'}
sharemarket_news = {'date': 1, 'news': 'null'}
corona_news = {'date': 1, 'news': 'null'}
space_news = {'date': 1, 'news': 'null'}
motivation_news = {'date': 1, 'news': 'null'}


def add_news():
    api = NewsApiClient(api_key="37e0227c41fa4972a5bc0a6a871a62b8")
    x = datetime.datetime.now().date()
    src = ['the-times-of-india', 'google-news-in', 'google-news-in']
    indian=[]
    for sources in src:
        indian.extend( api.get_top_headlines(sources=sources)['articles'] )
    
    indian_news.update({'date':x, 'news': indian})
    
    nat = api.get_everything(q='india', page_size=30, sort_by='publishedAt', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1) )
    national_news.update({'date':x, 'news': nat['articles']})

    abroad = api.get_top_headlines(page_size=30)
    international_news.update({'date':x, 'news': abroad['articles']})

    boll = api.get_everything(q='bollywood', page_size=10, sort_by='publishedAt', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1) )
    bollywood_news.update({'date':x, 'news': boll['articles']})

    lif = api.get_everything(q='lifestyle', page_size=10, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    lifestyle_news.update({'date':x, 'news': lif['articles']})

    spo = api.get_everything(q='cricket football sport', page_size=30, sort_by='publishedAt',from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    sport_news.update({'date':x, 'news': spo['articles']})
    
    buss = api.get_everything(q='business', page_size=30, sort_by='publishedAt', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    business_news.update({'date':x, 'news': buss['articles']})

    shar = api.get_everything(q='sensex nifty market', page_size=30, sort_by='publishedAt', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    sharemarket_news.update({'date':x, 'news': buss['articles']})

    cor = api.get_everything(q='corona', page_size=10, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    corona_news.update({'date':x, 'news': cor['articles']})

    spa = api.get_everything(q='space', page_size=10, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
    space_news.update({'date':x, 'news': spa['articles']})
    
    mot = api.get_everything(q='motivation', page_size=10, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1) )
    motivation_news.update({'date':x, 'news': mot['articles']})

