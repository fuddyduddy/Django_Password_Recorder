from django.shortcuts import render
from django.views import generic

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

class AuthLevelListView(generic.ListView):
    model = AuthLevel

class AccountListView(generic.ListView):
    model = Account
    paginated_by = 10
