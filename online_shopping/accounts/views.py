from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            
            if username and email and password:
                user = User.objects.create_user(username=username, email=email, password=password)
                UserProfile.objects.create(user=user)
                return JsonResponse({"message": "User registered successfully."})
            return JsonResponse({"error": "Missing fields!"}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
    return JsonResponse({"error": "Only POST method is allowed."}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Logged in successfully."})
            return JsonResponse({"error": "Invalid credentials."}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
    return JsonResponse({"error": "Only POST method is allowed."}, status=405)
