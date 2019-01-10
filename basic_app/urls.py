from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.form_view, name="form_view"),
    url(r'^$', views.prediction_result_view, name="prediction_result_view")
]