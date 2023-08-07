from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
import requests
from .models import CoinNews
from .serializers import CoinNewsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from news import GetNewsContent
from gpt import gpt

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
    apiKey = "27ddvbcs5cv6gc0lubw0mte0xvp5mryumerjt8ij"
    
    for page in range(1,5):
        url = f"https://cryptonews-api.com/api/v1?tickers=BTC&items=3&page={page}&token={apiKey}"
        #print(url)
        r = requests.get(url).json()
        newsDataList = r['data']
        for newsData in newsDataList:
            coinNews = CoinNews()
            coinNews.news_title = newsData['title']
            coinNews.thumb_url = newsData['image_url']
            coinNews.views = 0 
            coinNews.src = newsData['news_url']
            coinNews.content = GetNewsContent(coinNews.src)
            coinNews.summary = gpt(coinNews.content)
            coinNews.save()
        #print(r.json())
    return HttpResponse(url)


@api_view(["GET", "POST"])
def detail(request, news_id):
    queryset = CoinNews.objects.filter(news_id=news_id)
    serializer = CoinNewsSerializer(queryset, many=True)
    print(type(serializer.data[0]))
    return Response(serializer.data[0])
