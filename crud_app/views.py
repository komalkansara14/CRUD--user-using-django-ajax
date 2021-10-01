from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import User
from django.http import JsonResponse
# Create your views here.

def home(request):
 form = UserRegistrationForm
 data = User.objects.all()
 return render(request, 'crud_app/home.html', {'form': form, 'data':data})

def save_data(request):
 if request.method == 'POST':
  form = UserRegistrationForm(request.POST)
  if form.is_valid():
   uid = request.POST.get('userid')
   name = request.POST['name']
   email = request.POST['email']
   department = request.POST['department']
   #print(uid)

   if(uid == '' ):
     u = User(name=name, email=email, department=department)
   else:
     u = User(id=uid, name=name, email=email, department=department)

   u.save()
   user = User.objects.values()
   user_data = list(user)
     #print(user_data)
   return JsonResponse({'status': 'Save', 'user_data':user_data})
  
  else:
   return JsonResponse({'status': 'Fail'})
 else:
  pass

# deleting the data
def delete_data(request):
 if request.method == 'POST':
  id = request.POST.get('sid')
  #print(id)
  pid = User.objects.get(pk=id)
  pid.delete()
  return JsonResponse({'status':1}) 
 else:
  return JsonResponse({'status':0})

# Editing the data 
def edit_data(request):
  if request.method == 'POST':
    id = request.POST.get('sid')
    print(id)
    user = User.objects.get(pk=id)
    user_data = {'id':user.id, 'name':user.name, 'email':user.email, 'department':user.department}
    return JsonResponse(user_data)

