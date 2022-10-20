from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Users
from UserApp.serializers import UsersSerializer

# Create your views here.


@csrf_exempt
def usersAPI(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("New record Successfully added", safe=False)
        print(users_serializer.errors)
        return JsonResponse("Failed to add new record", safe=False)
    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users = Users.objects.get(UserId=users_data['UserId'])
        users_serializer = UsersSerializer(users, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Update data successful", safe=False)
        return JsonResponse("Update failed")
    elif request.method == 'DELETE':
        users = Users.objects.get(UserId=id)
        users.delete()
        return JsonResponse("Deleted successfully", safe=False)


def search(request):
    value = request.GET.get('value')
    users = Users.objects.filter(UserName__contains=value)
    users_serializer = UsersSerializer(users, many=True)
    return JsonResponse(users_serializer.data, safe=False)
