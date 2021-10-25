# Create your views here.


from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets

from .models import Hunting
from .serializers import UserSerializer, GroupSerializer, HuntingSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class HuntingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hunting to be viewed or edited.
    """
    queryset = Hunting.objects.all()
    serializer_class = HuntingSerializer
    permission_classes = [permissions.IsAuthenticated]
