from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from . models import userinfo
from . serializers import ImageSerializer
# Create your views here.
class ImageViewSet(APIView):
    def get(self, request):
        userinfo1=userinfo.objects.all()
        
        serializer = ImageSerializer(userinfo1, many= True)
        return Response(serializer.data)
        

    def post(self):
        file = request.data['file']
        image = userinfo.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
