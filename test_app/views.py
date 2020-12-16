from django.shortcuts import render
from test_app.serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from test_app.models import Customer

# Create your views here.

@api_view(['GET','POST'])
def customer_list(request):
    if request.method=="GET":
        cust=Customer.objects.all()
        serializer=CustomerSerializer(cust,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
