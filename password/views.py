from django.shortcuts import render
from django.views import generic

from django.shortcuts import get_object_or_404

from .models import User, AuthLevel, Account

# Create your views here.
def index(request):
    num_user = User.objects.all().count()
    num_authLevel = AuthLevel.objects.all().count()
    num_account = Account.objects.all().count()

    print(num_user, num_authLevel, num_account)

    context = {
        'num_user':num_user,
        'num_authLevel':num_authLevel,
        'num_account':num_account,
    }

    return render(request, 'index.html', context=context)

#==============ListView==============
class UserListView(generic.ListView):
    model = User
    def __init__(self):
        print(User.objects.all())

class AuthLevelListView(generic.ListView):
    model = AuthLevel

class AccountListView(generic.ListView):
    model = Account
    paginate_by = 10

#==============DetailView==============
class UserDetailView(generic.DetailView):
    model = User
# class UserDetailView:
#     def get(self, request, **primary_key):
#         print(request)
#         user = get_object_or_404(User, pk=primary_key)
#         return render(request, 'password/user_detail.html', context={'user': user})

class AuthLevelDetailView(generic.DetailView):
    model = AuthLevel

class AccountDetailView(generic.DetailView):
    model = Account
    paginate_by = 10
