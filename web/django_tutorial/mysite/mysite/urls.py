from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    # path('pollsa/', include('polls.urls')),
    # path('pollsb/', include('polls.urls')),
    # path('pollsc/', include('polls.urls')),
    # path('pollsd/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
#127.0.0.1/polls/
#127.0.0.1/pollsa/
#127.0.0.1/pollsc/
#127.0.0.1/pollsd/
#이런 사이트로 오면 연결시켜주는 명령어이다.
#127.0.0.1:8000/polls/