from profileapp.views import ProfileCreateView
from django.urls import path, include
app_name = "profileapp"

urlpatterns = [
    path('create/',ProfileCreateView.as_view(), name='create'),
]