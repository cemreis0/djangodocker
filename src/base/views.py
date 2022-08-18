from django.http import HttpResponse
from django.contrib.auth.models import User
import json
from .serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view

@api_view(['POST'])
def adduser(request):
  if request.method == 'POST':
    username = json.loads(request.body)["username"]
    User.objects.create(username=username)
    response = json.dumps({'username': username})
  else:
    response = json.dumps({'error': 'Request must be POST!'})
  return HttpResponse(response)

def getuser(request, username):
  user = User.objects.get(username=username)
  if request.method == 'GET':
    response = json.dumps({'username':user.username})
  else:
    response = json.dumps({'error': 'Request must be GET!'})
  return HttpResponse(response)

def getallusers(request):
  if request.method == 'GET':
    allusers = User.objects.all()
    serializer = UserSerializer(allusers, many=True)
    response = JSONRenderer().render(serializer.data)
  else:
    response = json.dumps({'error': 'Request must be GET!'})
  return HttpResponse(response)