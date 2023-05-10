from rest_framework import routers
from repairsapi.views import CustomerView
from repairsapi.views import EmployeeView
from repairsapi.views import TicketView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from repairsapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'customers', CustomerView, 'customer')

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'employees', EmployeeView, 'employee')

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tickets', TicketView, 'ticket')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]