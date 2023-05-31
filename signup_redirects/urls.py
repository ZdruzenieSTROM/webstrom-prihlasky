from django.urls import path

from .views import ActiveRedirects, FollowRedirect

app_name = "redirects"

urlpatterns = [
    path("", ActiveRedirects.as_view(), name="active"),
    path("<slug:origin>/", FollowRedirect.as_view(), name="redirect"),
]
