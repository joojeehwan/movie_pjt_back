from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserCreationForm
from django.http import JsonResponse
User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
	# 1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	# 1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 1-3. 아이디 중복 여부 체크
    if User.objects.filter(username=request.data.get('username')).exists():
        return Response({'error': '중복하는 아이디가 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	# 2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	# 3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
        # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)







# @require_http_methods(['GET', 'POST'])
# def login(request):
#     if request.user.is_authenticated:
#         return redirect('community:index')

#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect(request.GET.get('next') or 'community:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts/login.html', context)


# @require_POST
# def logout(request):
#     auth_logout(request)
#     return redirect('community:index')


# @login_required
# def profile(request, username):
#     person = get_object_or_404(get_user_model(), username=username)
#     context = {
#         'person': person,
#     }
#     return render(request, 'accounts/profile.html', context)


# @require_POST
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         person = get_object_or_404(get_user_model(), pk=user_pk)
#         user = request.user
#         if person != user:
#             if person.followers.filter(pk=user.pk).exists():
#                 person.followers.remove(user)
#                 isFollowed = False
#             else:
#                 person.followers.add(user)
#                 isFollowed = True
            
#             context = {
#                 'isFollowed': isFollowed,
#                 'followersCnt': person.followers.count(),
#                 'followingsCnt': person.followings.count(),
#             }
#             return JsonResponse(context)
#     return redirect('accounts:profile', person.username)
