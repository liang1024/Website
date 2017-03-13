from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StockSerializer
from .models import Stock
# Create your views here.


# 返回一个列表集合:
#stock/
class StockList(APIView):
    # get方法
    def get(self,request):
        stocks=Stock.objects.all()
        serializer=StockSerializer(stocks,many=True)
        return Response(serializer.data)

    # Post
    def post(self):
        pass