from django.views.generic import TemplateView


class SimpleMapView(TemplateView):
    template_name = "geos/map.html"
