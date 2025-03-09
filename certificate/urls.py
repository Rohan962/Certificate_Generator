from django.urls import path
from .views import *

urlpatterns = [
	path('', create, name='certificate-home'),
	path('view_certificate_status', view_certificate_status, name="view_certificate_status"),
	path('<int:id>/<slug:slug>', track, name='track'),
	path('delete/<int:id>/<slug:slug>', delete_event, name='delete_event'),

]