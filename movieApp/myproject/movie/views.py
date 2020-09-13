from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets, permissions
from .models import MovieDetail
from .serializers import MovieDetailSerializer


class MovieDetailView(viewsets.ModelViewSet):

    queryset = MovieDetail.objects.all()
    serializer_class = MovieDetailSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)