from django.urls import path
from myapp import views



urlpatterns=[

    path('',views.index,name='index'),
    path('game/',views.game,name='game'),
    path('game_end/',views.game_end,name='game_end'),
    path('game1/',views.game1,name='game1'),
    path('game_end1/',views.game_end1,name='game_end1'),
    path('game2/',views.game2,name='game2'),
    path('game_end2/',views.game_end2,name='game_end2'),
    path('game3/',views.game3,name='game3'),
    path('game_end3/',views.game_end3,name='game_end3'),
    path('game4/',views.game4,name='game4'),
    path('game_end4/',views.game_end4,name='game_end4'),
    path('game5/',views.game5,name='game5'),
    path('game_end5/',views.game_end5,name='game_end5'),
]
