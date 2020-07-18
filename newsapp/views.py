from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User 
from django import forms
from .forms import NewUserForm, Data
from django.contrib import messages
from .news import indian_news, international_news, sport_news, business_news, lifestyle_news, add_news, national_news, sharemarket_news, bollywood_news, space_news, corona_news, motivation_news
import datetime
from newsapi import NewsApiClient
import requests
import json

from newsapp.models import Userinfo, News, Sourcenews

# Create your views here.
status= "previously_updated"
news=None
def main(request):

    api = NewsApiClient(api_key="37e0227c41fa4972a5bc0a6a871a62b8")
    news=News.objects.all().first()
    sourcenews = Sourcenews.objects.all().first()

    if request.user.is_authenticated:
        if len(News.objects.all())==0:
            updatenews()
            status="currently_updated"
            
        elif(datetime.datetime.now().date() != news.date.date()):
            updatenews()
            status="currently_updated"
        else:
            status="previously_updated"

        
        if len(Sourcenews.objects.all())==0 or datetime.datetime.now().date() != sourcenews.date.date():
            update_sourcenews()

        
        news=News.objects.all().first()

        indian_news= json.loads( news.indian_news )
        international_news= json.loads( news.international_news )
        sport_news= json.loads( news.sport_news )
        business_news= json.loads( news.business_news )
        national_news= json.loads( news.national_news )
        sharemarket_news= json.loads( news.sharemarket_news )
        bollywood_news= json.loads( news.bollywood_news )
        space_news= json.loads( news.space_news )
        corona_news= json.loads( news.corona_news )
        lifestyle_news= json.loads( news.lifestyle_news )
        motivation_news= json.loads( news.motivation_news )

        news= Sourcenews.objects.all().first()
      
        hindu = json.loads( news.hindu )
        gnews = json.loads( news.gnews )
        toi = json.loads( news.toi )
        bloom = json.loads( news.bloom )
        bus = json.loads( news.buss )
        fortune = json.loads( news.fortune )
        bbc = json.loads( news.bbc )
        espn = json.loads( news.espn )
        foxsport = json.loads( news.foxsport )
        natgeo = json.loads( news.natgeo )
        nextbig = json.loads( news.nextbig )
        tech = json.loads( news.tech )
        newsci = json.loads( news.newsci )
        mtv = json.loads( news.mtv )
        buzz = json.loads( news.buzz )
        mnt = json.loads( news.mnt )

        
        
        sourcess = [{'id':'m1', 'news':hindu, 'title':'the-hindu'}, {'id':'m2', 'news': gnews, 'title':'the-google-news'}, {'id':'m3', 'news': toi, 'title':'the-times-of-india'}, 
                {'id':'m4', 'news': bloom, 'title':'bloomberg'},
                {'id':'m5', 'news': bus, 'title':'business-insider'}, {'id':'m6', 'news': fortune, 'title':'fortune'}, {'id':'m7', 'news': bbc, 'title':'bbc-sports'},
                {'id':'m8', 'news': espn, 'title':'espn'},
                {'id':'m9', 'news':foxsport, 'title':'foxsport'}, {'id':'m10', 'news':natgeo, 'title':'national-geography'}, {'id':'m11', 'news':nextbig, 'title':'ext-big-future'},
                {'id':'m12', 'news':tech, 'title':'tech-radar'},
                {'id':'m13', 'news':newsci, 'title':'new-scientist'}, {'id':'m14', 'news':mtv, 'title':'the-mtv'}, {'id':'m15', 'news':buzz, 'title':'buzzfeed'},
                {'id':'m16', 'news':mnt, 'title':'medical-news-today'}]

 
        username = request.user.username

        userinfo = Userinfo.objects.filter(username=username).first()

        if userinfo.last_date.date()!=datetime.datetime.now().date():
            update_personalnews(username)
            status = "updated"

        elif userinfo.state_news == '' or userinfo.city_news == '' or userinfo.bestpick_news == '':
            update_personalnews(username)
            status = "updated"


        
        userinfo = Userinfo.objects.filter(username=username).first()
        state_news= json.loads(userinfo.state_news)
        city_news= json.loads(userinfo.city_news)
        bestpick_news= json.loads(userinfo.bestpick_news)
        state = userinfo.state
        city = userinfo.city
        

        context = {"bestpick_news": bestpick_news, "indian_news": indian_news, "international_news": international_news, "sport_news": sport_news, "business_news": business_news,
            "national_news": national_news, "lastupdated": news.date.date(), "status":status, "city_news":city_news, "state_news": state_news, "state": state, "city": city,
            "sharemarket_news": sharemarket_news, "bollywood_news": bollywood_news, "space_news": space_news, "corona_news": corona_news,
            "lifestyle_news": lifestyle_news, "motivation_news" : motivation_news ,"username": username, "sourcess" : sourcess}
            
        return render(request, 'index.html',context)
    else:
        messages.warning(request, f"Oops! please login with your account")
        return redirect('/')

def register1(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            age = request.POST['age']
            state = request.POST['state']
            city = request.POST['city']
            gender =  request.POST['gender']
            profession = request.POST['profession']
            date = datetime.datetime.now().date()
            key_words= [profession]
            key_words = json.dumps(key_words)
            userinfo = Userinfo(username=username, city=city, state=state, age=age, last_date=date, gender=gender, profession=profession, key_words = key_words)
            userinfo.save()
            form.save()
            messages.success(request, "registration succesfull please login your account!!")
            return redirect('/')
        else:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1!=password2:
                messages.warning(request, "password1 is not equal to password2 please ensure password is typed correctly!!")
            elif User.objects.filter(username=username).exists():
                messages.warning(request, "Username is already taken!!")
            else:
                messages.warning(request, "Password criteria is not meet, please use strong password!!")






    form =NewUserForm
    return render(request, 'register.html', {"form":form})

def login1(request):
    if request.user.is_authenticated:
         return redirect('news/')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('news/')
        else:
            messages.warning(request, f"Username or Password is incorrect, please try again!!")
        
    form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})

def logout1(request):
    logout(request)
    return redirect('/')


def search(request):
    if request.method == "POST":
        username = request.user.username
        userinfo = Userinfo.objects.filter(username=username).first()
        lst1 = json.loads(userinfo.key_words)
        api = NewsApiClient(api_key="37e0227c41fa4972a5bc0a6a871a62b8")
        search = request.POST['search']
        lst = list(search.split(" "))
        news= []
        for item in lst:
            temp =api.get_everything(q=item, page_size=5, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
            temp = temp['articles']
            if temp is not None:
                if item not in lst1:
                    lst1.append(item)
                news.extend(temp)
        
        userinfo.key_words = json.dumps(lst1)
        userinfo.save()
        

        return render(request, 'search.html', {"search_news":news, "list":lst})


def updatenews():
    add_news()
    india=json.dumps(indian_news['news'] )
    inter=json.dumps(international_news['news'] )
    sport=json.dumps(sport_news['news'] )
    buss=json.dumps(business_news['news'] )
    nat=json.dumps(national_news['news'] )
    sha=json.dumps(sharemarket_news['news'] )
    bol=json.dumps(bollywood_news['news'] )
    spa=json.dumps(space_news['news'] )
    cor=json.dumps(corona_news['news'] )
    lif=json.dumps(lifestyle_news['news'] )
    motv= json.dumps(motivation_news['news'] )

    if len(News.objects.all())==0:
        
        news=News(date = datetime.datetime.now().date(), indian_news = india, national_news = nat, international_news = inter,
        bollywood_news = bol, lifestyle_news = lif, sport_news = sport, business_news = buss,
        sharemarket_news = sha, corona_news = cor, space_news = spa, motivation_news =motv )
        
        news.save()

    else:
        news=News.objects.all().first()
        news.date =  datetime.datetime.now().date()
        news.indian_news = india
        news.international_news = inter
        news.sport_news = sport
        news.business_news=buss
        news.national_news=nat
        news.sharemarket_news=sha
        news.bollywood_news=bol
        news.space_news=spa
        news.corona_news=cor
        news.lifestyle_news=lif
        news.motivation_news=motv

        news.save()

    
def  update_personalnews(username):
    
    userinfo = Userinfo.objects.filter(username=username).first()
    api = NewsApiClient(api_key="37e0227c41fa4972a5bc0a6a871a62b8")
    userinfo.last_date = datetime.datetime.now().date()
    state_news=api.get_everything(q=userinfo.state, page_size=20, sort_by='publishedAt', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1) )
    city_news=api.get_everything(q=userinfo.city, page_size=20, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1) )
    state_news = state_news['articles']
    city_news = city_news['articles']
    userinfo.state_news = json.dumps(state_news)
    userinfo.city_news = json.dumps(city_news)
    
    lst = json.loads(userinfo.key_words)

    news= []
    for item in lst:
        temp =api.get_everything(q=item, page_size=5, sort_by='relevancy', from_param =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month, 1 ))
        temp = temp['articles']
        if temp is not None:
            news.extend(temp)
    
    userinfo.bestpick_news = json.dumps(news)
    userinfo.save()


def update_sourcenews():
    api = NewsApiClient(api_key="37e0227c41fa4972a5bc0a6a871a62b8")
    date = datetime.datetime.now().date()
    hindu = json.dumps( api.get_top_headlines(sources='the-hindu')['articles'] )
    gnews = json.dumps( api.get_top_headlines(sources='google-news-in')['articles'] )
    toi = json.dumps( api.get_top_headlines(sources='the-times-of-india')['articles'] )
    bloom = json.dumps( api.get_top_headlines(sources='bloomberg')['articles'] )
    buss =json.dumps( api.get_top_headlines(sources='business-insider')['articles'] )
    fortune = json.dumps( api.get_top_headlines(sources='fortune')['articles'] )
    bbc = json.dumps( api.get_top_headlines(sources='bbc-sport')['articles'] )
    espn = json.dumps( api.get_top_headlines(sources='espn')['articles'] )
    foxsport = json.dumps( api.get_top_headlines(sources='fox-sports')['articles'] )
    natgeo  =json.dumps( api.get_top_headlines(sources='national-geographic')['articles'] )
    nextbig = json.dumps( api.get_top_headlines(sources='next-big-future')['articles']  )
    tech = json.dumps( api.get_top_headlines(sources='techradar')['articles'] )
    newsci  = json.dumps( api.get_top_headlines(sources='new-scientist')['articles'] )
    mtv = json.dumps( api.get_top_headlines(sources='mtv-news')['articles'] )
    buzz = json.dumps( api.get_top_headlines(sources='buzzfeed')['articles'] )
    mnt = json.dumps( api.get_top_headlines(sources='medical-news-today')['articles'] )

    if len(Sourcenews.objects.all())==0:
        sourcenews = Sourcenews(date=date, hindu=hindu, gnews=gnews, toi=toi, bloom=bloom, buss=buss, fortune=fortune,
                    bbc=bbc, espn=espn, foxsport=foxsport, natgeo=natgeo, nextbig=nextbig,
                    tech=tech, newsci=newsci, mtv=mtv, buzz=buzz, mnt=mnt)

        sourcenews.save()
    
    else:
        news= Sourcenews.objects.all().first()
        news.date=date
        news.hindu=hindu
        news.gnews=gnews
        news.toi=toi
        news.bloom=bloom
        news.buss=buss
        news.fortune=fortune
        news.bbc=bbc
        news.espn=espn
        news.foxsport=foxsport
        news.natgeo=natgeo
        news.nextbig=nextbig
        news.tech=tech
        news.newsci=newsci
        news.mtv=mtv
        news.buzz=buzz
        news.mnt=mnt

        news.save()
        


    pass