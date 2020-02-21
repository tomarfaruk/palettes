
from django.http import HttpResponse
from django.views import generic
from .models import Palette
from django.db.models import Q
from django.shortcuts import render
from rest_framework import permissions

from rest_framework import viewsets, filters, renderers, generics
from rest_framework.views import APIView
from .serializers import PaletteSerializer, LoginSerializer
from django.contrib.auth import login as django_login
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class LoginView(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class PaletteView(viewsets.ModelViewSet):
    renderer_classes = [renderers.JSONRenderer]
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer
    filter_backends = (DjangoFilterBackend, )
    filter_fields = [
        'color_name',
        'color_domain_one',
        'color_domain_two',
        'color_accent_one',
        'color_accent_two',
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def PaletteList(request):

    queryset = Palette.objects.filter(
        status=1).all()  # get all publish palettes

    template_name = 'index.html'

    query = request.GET.get('q')  # get search parameter fro filter
    if query:
        queryset = queryset.filter(
            Q(color_name__icontains=query) |
            Q(color_domain_one__icontains=query) |
            Q(color_domain_two__icontains=query) |
            Q(color_accent_one__icontains=query) |
            Q(color_accent_two__icontains=query)
        ).distinct()

    context = {
        "palettes": queryset
    }
    return render(request, template_name, context)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
