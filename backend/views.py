from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.http import Http404
from django.contrib.auth.models import User
from .permissions import IsUserOrReadOnly
from .models import Cheese
from .serializers import CheeseSerializer, UserSerializer

class CheeseList(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, _request, _format=None):
        cheeses = Cheese.objects.all()
        serializer = CheeseSerializer(cheeses, many=True)
        return Response(serializer.data)


    def post(self, request, _format=None):
        serializer = CheeseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)



class CheeseDetail(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, IsUserOrReadOnly)

    def get_cheese(self, pk):
        try:
            return Cheese.objects.get(pk=pk)
        except Cheese.DoesNotExist:
            raise Http404


    def get(self, _request, pk, _format=None):
        cheese = self.get_cheese(pk)
        serializer = CheeseSerializer(cheese)
        return Response(serializer.data)


    def put(self, request, pk, _format=None):
        cheese = self.get_cheese(pk)
        serializer = CheeseSerializer(cheese, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)


    def delete(self, _request, pk, _format=None):
        cheese = self.get_cheese(pk)
        cheese.delete()
        return Response(status=HTTP_204_NO_CONTENT)



class UserList(APIView):

    def get(self, _request, _format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)



class UserDetail(APIView):

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404


    def get(self, _request, pk, _format=None):
        user = self.get_user(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
