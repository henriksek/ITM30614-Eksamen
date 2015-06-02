from django.conf.urls import patterns, url

from message_app import views

urlpatterns = patterns('',
    url(r'^new_message/$', views.new_message, name='new_message'),
    url(r'^message_detail/(\d+)/$', views.message_detail, name='message_detail'),
    url(r'^like_message/(\d+)/$', views.like_message, name='like_message'),
)