from django.urls import path
from geos.views import SimpleMapView


urlpatterns = [
    path("", SimpleMapView.as_view(), name="show_simple_map"),
]
