from django.conf.urls import patterns, url

from message_app import views

urlpatterns = patterns('',
    url(r'^new_message/$', views.new_message, name='new_message'),
)