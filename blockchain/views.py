from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
import json
import requests
from .models import CoinNews
from .serializers import CoinNewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from news import GetNewsContent
from gpt import gpt
from gpt2 import gpt_title, gpt_content
from newsletter import NewsLetter


# Create your views here.
def db_test(request):
    if request.method == "POST":
        #print(request.POST)
        #body = json.loads(request.body)
        #name = body["name"]
        data = {
            "name": "choi",
            "age": 20,
            "hobbies": ["Coding", "Art", "Gaming", "Cricket", "Piano"]
        }
        print(data)
        return JsonResponse(data, safe = False)
    else:
        return HttpResponse("Hello API")


def index(request):
    news_list = CoinNews.objects.order_by('-create_date')
    context = {'news_list': news_list}
    return render(request, 'pybo/question_list.html', context)


@api_view(["GET", "POST"])
def CoinNewsAPI(request): 
    queryset = CoinNews.objects.all() 
    print(queryset)
    serializer = CoinNewsSerializer(queryset, many=True) 
    return Response(serializer.data)


def LoadCoinNews(request):
    apiKey = "nsez6m6xbgcn5cpookmjdbwwwartzly8gyahjojz"
    
    for page in range(1,5):
        url = f"https://cryptonews-api.com/api/v1?tickers=BTC&items=3&page={page}&token={apiKey}"
        #print(url)
        r = requests.get(url).json()
        newsDataList = r['data']
        for newsData in newsDataList:
            coinNews = CoinNews()
            coinNews.news_title = gpt_title(newsData['title'])
            coinNews.thumb_url = newsData['image_url']
            coinNews.view = 0 
            coinNews.create_date = timezone.now()
            coinNews.src = newsData['news_url']
            coinNews.tickers= newsData['tickers']
            coinNews.source_name = newsData['source_name']
            coinNews.content = gpt_content(GetNewsContent(coinNews.src))
            coinNews.summary = gpt(coinNews.content)
            coinNews.save()
        #print(r.json())
    return HttpResponse(url)



def LoadCoinNewsContent(request):
    apiKey = "nsez6m6xbgcn5cpookmjdbwwwartzly8gyahjojz"
    
    for page in range(1,5):
        url = f"https://cryptonews-api.com/api/v1?tickers=BTC&items=3&page={page}&token={apiKey}"
        #print(url)
        r = requests.get(url).json()
        newsDataList = r['data']
        for newsData in newsDataList:
            coinNews = CoinNews()
            coinNews.news_title = newsData['title']
            coinNews.thumb_url = newsData['image_url']
            coinNews.view = 0 
            coinNews.create_date = timezone.now()
            coinNews.src = newsData['news_url']
            coinNews.tickers= newsData['tickers']
            coinNews.source_name = newsData['source_name']
            coinNews.content = GetNewsContent(coinNews.src)
            
            coinNews.save()
        #print(r.json())
    return HttpResponse(url)


def TranslateCoinNewsById(request, news_id):
    apiKey = "nsez6m6xbgcn5cpookmjdbwwwartzly8gyahjojz"
    coinNews = CoinNews.objects.get(news_id = news_id)
    coinNews.news_title = gpt_title(coinNews.news_title)
    coinNews.content = gpt_content(coinNews.content)
    coinNews.summary = gpt(coinNews.content)
    coinNews.save()

    return HttpResponse('Translate Success')


def Reset(request):
    queryset = CoinNews.objects.all()
    for coinNews in queryset:
        coinNews.delete()
    return HttpResponse('reset')


@api_view(["GET", "POST"])
def detail(request, news_id):
    queryset = CoinNews.objects.get(news_id=news_id)
    print(queryset.view)
    queryset.view += 1
    queryset.save()
    serializer = CoinNewsSerializer(queryset)
    #print(type(serializer.data[0]))
    return Response(serializer.data)


def SendNews(request, email_address):
    NewsLetter(email_address = email_address)
    return HttpResponse("Email Success")