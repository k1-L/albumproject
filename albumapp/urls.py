from django.urls import path
from .import views

app_name = 'albumapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='top_page'),
    path('index/', views.TopView.as_view(), name='index'),
    path('post/',views.CreateAlbumView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('albums/<int:category>', views.CategoryView.as_view(), name = 'album_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name = 'user_list'),
    path('album-detail/<int:pk>', views.DetailView.as_view(), name = 'album_detail'),
    path('mypage/', views.MypageView.as_view(), name = 'mypage'),
    path('albumapp/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name = 'album_delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
