from django.urls import path
from api.views import DetailsListApiView
urlpatterns =[
    path('',DetailsListApiView.as_view())
]
