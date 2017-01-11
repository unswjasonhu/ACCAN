from django.conf.urls import url
from sensors import views

urlpatterns=[
    url(r'^sensor/$',views.Sensor_list),
    url(r'^sensor/(?P<pk>[0-9]+)/$',views.Sensor_detail),
]
