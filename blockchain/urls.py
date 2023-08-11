from django.urls import path

from . import views

#하나의 프로젝트 내에 여러 개의 앱이 추가될 수 있으므로, app_name으로 이름공간을 지정
app_name = 'blockchain'

urlpatterns = [
    path('', views.db_test, name = 'db_test'),
    path('apitest', views.CoinNewsAPI),
    path('<int:news_id>/', views.detail, name= 'detail'),
    path('loadcoinnews', views.LoadCoinNews),
    path('reset', views.Reset),
    path('sendnews/<str:email_address>', views.SendNews),
]