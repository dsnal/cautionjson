from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cautionjson import views
from django.conf.urls import include
from django.contrib.auth.views import login

app_name = "cautionjson"
urlpatterns = [
    url(r'^trips/$', views.TripList.as_view()),
    url(r'^trips/(?P<pk>[0-9]+)$', views.TripDetail.as_view()),
	url(r'^trips/mainpage/$', views.mainpage, name='mainpage'),
	url(r'^trips/datainsert/$', views.datainsert, name='datainsert'),
	url(r'^trips/finish/$', views.finish, name='finish'),
	url(r'^trips/users/$', views.UserList.as_view()),
	url(r'^trips/register/$', views.register,name='register'),
	url(r'^trips/login/$', login,{'template_name':'cautionjson/login.html'},name='login')



]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]