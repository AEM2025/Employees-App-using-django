from django.urls import path
from emp.views import landing, get_emp, emp_index


'''

<li class="nav-item">
          <a class="nav-link" href="{% url 'emp.landingggg' %}">Landinggg</a>
</li>
'''
urlpatterns = [
    path('', landing, name="landing_page"),
    path('all', get_emp, name="emp.all"),
    path('index', emp_index, name="emp.index")
]
