from django.shortcuts import render
from django.http import HttpResponse
from emp.models import Emp

def landing(request):
    # return HttpResponse("---------------Landing page -----------------------")
    return render(request, 'emp/landing.html')


emp = ['Ahmed', 'Emad', 'Asmaa', 'Ismail']

# MySQL:
# ALTER USER 'root'@'localhost' IDENTIFIED BY 'Ahmed1234567890_';
#  create user devops43 identified by 'Ahmed1234567890_';
# mysql -u devop43 -p

'''
user_name: ahmed
email: ahmed@gmail.com
123

'''

def get_emp(request):
    return render(request, 'emp/emp.html', context={"emp": emp})


def emp_index(request):
    emp = Emp.objects.all()
    return render(request, 'emp/index.html', context={"emp": emp})