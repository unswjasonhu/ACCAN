from django.conf.urls import url
from sensors import views

urlpatterns=[
    url(r'^sensor/$',views.DeviceID),
    url(r'^sensor/(?P<pk>[0-9]+)/$',views.Name),
]
