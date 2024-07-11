from .views import ContactList, ContactDetail
from django.urls import path

urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('<int:pk>', ContactDetail.as_view(), name='contact_detail')
]
