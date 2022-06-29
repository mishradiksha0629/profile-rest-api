from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_app import serializers
from rest_framework import viewsets
# Create your views here.

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer
    def get(self,request,format = None):
        an_apiview = ["APIview is used to get data",
                        "Hello World",
                        "it is maually mapped to URL"]
        return Response({"message":"Hello","an_apiview":an_apiview})
    def post(self,request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk = None):
        """handles update on object ,replaces object with new object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk = None):
        """handles update on object ,and updates only field which is provided"""
        return Response({'method':'PATCH'})

    def put(self,request,pk = None):
        """Delete an object"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""
    def lists(self,request):
        api = ["hello"]
        return Response({'message':'diksha','api':api})
    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})
