from django.urls import path
from . import views

urlpatterns = [
    #Authentication
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.RegisterView.as_view(), name='auth_register'),

    #Profile
    path('profile', views.getProfile, name='profile'),    

    #Watchlist
    path('watchlist/<int:pk>', views.getWatchlist, name="watchlist"),
    path('watchlist/movie/<str:movie_id>', views.getWatchlistMovieId, name="watchlist movieid"),
    path('watchlist/<int:pk>/delete', views.deleteWatchlist, name="delete-watchlist"),
    path('watchlist/users',views.getUserWatchlist, name="my-watchlist"),
    path('watchlist/create', views.createWatchlist, name="create-watchlist"),
]