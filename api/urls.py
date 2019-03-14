# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView,UndoTaskView,DoTaskView

urlpatterns = {
    url(r'^api/tasks/$', CreateView.as_view(), name="create"),
    url(r'^api/tasks/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
     url(r'^api/tasks/(?P<pk>[0-9]+)/done$',
         DoTaskView.as_view(), name="details"),
     url(r'^api/tasks/(?P<pk>[0-9]+)/undone$',
         UndoTaskView.as_view(), name="details")
}


urlpatterns = format_suffix_patterns(urlpatterns)