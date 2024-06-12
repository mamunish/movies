from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializer import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Watchlist
from .serializer import WatchlistSerializer, ProfileSerializer
from django.contrib.auth.models import User


# Create your views here.

#Login User
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


#api/watchlist/<int:pk>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWatchlist(request, pk):
    watchlist = request.user.watchlist.get(id=pk)
    serializer = WatchlistSerializer(watchlist, many=False)
    return Response(serializer.data)



#api/watchlist/<int:pk>/delete
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteWatchlist(request, pk):
    watchlist = request.user.watchlist.get(id=pk)
    watchlist.delete()
    return Response('Watchlist was deleted')


#api/watchlist/create
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createWatchlist(request):
    user = request.user
    data = request.data
    watchlist = Watchlist.objects.create(
           user=user,
        movie_name=data['movie_name'],
        movie_id=data['movie_id'],
    )
    serializer = WatchlistSerializer(watchlist, many=False)
    return Response(serializer.data)


#api/profile 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getProfile(request):
    user = request.user
    serializer = ProfileSerializer(user, many=False)
    return Response(serializer.data)


#api/watchlist/user/<int:pk>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserWatchlist(request):
    user = request.user
    watchlist = Watchlist.objects.filter(user=user)
    serializer = WatchlistSerializer(watchlist, many=True)
    return Response(serializer.data)

#api/watchlist/movie/<int:pk>
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWatchlistMovieId(request, movie_id):
    user = request.user
    watchlist = Watchlist.objects.filter(movie_id=movie_id, user_id=user).first()
    if watchlist:
        serializer = WatchlistSerializer(watchlist, many=False)
        return Response(serializer.data)
    else:
        return Response({})