from django.urls import path
from . import views

app_name = "questions"  # 같은 index라는 name을 가지고 있는 여러개의 앱이 있을 수 있으니까
# 이 앱의 이름으로 한번 더 그룹해서 겹쳐도 구분 가능하게 한다
urlpatterns = [
    # Read
    path('', views.index, name="index"),  # '' 를 보여주는 페이지이름을 index라고 부른다.
    path('<int:id>/', views.detail, name="detail"),

    path('create/', views.create, name="create"),
]
