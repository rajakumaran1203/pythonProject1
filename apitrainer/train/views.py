from .models import Employes
from .serializers import Empserial
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['POST'])
def create_employee(request):
    if request.method == 'POST':
        serialize_data = Empserial(data=request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response(serialize_data.data, status=status.HTTP_201_CREATED)
        return Response(serialize_data.data, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def getting_data(request):
    data = Employes.objects.all()
    result=Empserial(data, many=True)
    return Response(result.data,status=status.HTTP_200_OK)
@api_view(['GET'])
def getall(request):
    myname = request.GET.get('name', None)
    try:
        dta = Employes.objects.filter(name=myname)
    except Exception as e:
        print(e)
    results = Empserial(dta, many=True)
    if results:
        return Response( results.data, status=status.HTTP_302_FOUND)
    return Response({"error": "No records found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update(request):
    try:
        dats = Employes.objects.get(name="raja")
        print(dats)
    except Exception as e:
        print(e)
    results = Empserial(dats, data=request.data)
    if results.is_valid():
        results.save()
        return Response(results.data , status=status.HTTP_302_FOUND)

    return Response({'Bad request': 'No records found'}, status=status.HTTP_404_NOT_FOUND)
'''
@api_view(['DELETE'])
def delete(request):
    dats = Employes.objects.get(name="kumaran")
    if dats:
        dats.delete()
        return Response("Sucess" , status=status.HTTP_302_FOUND)
    return Response({'Bad request': 'No records found'}, status=status.HTTP_404_NOT_FOUND)

'''
@api_view(['GET'])
def delete(request):
    x = request.GET.get('name',None)
    dats = Employes.objects.get(name = x)
    if dats:
        dats.is_delete=True
        dats.save()
        return Response("Record sucessfully" , status=status.HTTP_302_FOUND)
    return Response({'Bad request': 'No records found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def delete_data(request):
    record=Employes.objects.filter(is_delete=True)
    result=Empserial(record,many=True)
    return Response(result.data,status=status.HTTP_302_FOUND)


@api_view(['GET'])
def current_data(request):
    record=Employes.objects.filter(is_delete=False)
    result=Empserial(record,many=True)
    return Response(result.data,status=status.HTTP_302_FOUND)
