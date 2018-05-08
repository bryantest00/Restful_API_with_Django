from django.urls import path
# from django.conf.urls import url
from games import views


urlpatterns = [
    path('game-categories/', views.GameCategoryList.as_view(),
         name=views.GameCategoryList.name),
    path('game-categories/<int:pk>/', views.GameCategoryDetail.as_view(),
         name=views.GameCategoryDetail.name),
    path('games/', views.GameList.as_view(),
         name=views.GameList.name),
    path('games/<int:pk>/', views.GameDetail.as_view(),
         name=views.GameDetail.name),
    path('players/', views.PlayerList.as_view(),
         name=views.PlayerList.name),
    path('players/<int:pk>/', views.PlayerDetail.as_view(),
         name=views.PlayerDetail.name),
    path('player-scores/', views.PlayerScoreList.as_view(),
         name=views.PlayerScoreList.name),
    path('player-scores/<int:pk>/', views.PlayerScoreDetail.as_view(),
         name=views.PlayerScoreDetail.name),
    path('users/', views.UserList.as_view(),
         name=views.UserList.name),
    path('users/<int:pk>/', views.UserDetail.as_view(),
         name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(),
         name=views.ApiRoot.name),

    # path('games/', views.game_list),
    # path('games/<int:pk>/', views.game_detail),

    # **Uncomment if you're planning on using Django 1.11 or lower**
    # url(r'^games/$', views.game_list),
    # url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]
