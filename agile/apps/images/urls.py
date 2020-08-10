from django.conf.urls import url

from .views import ImageView, SearchView


urlpatterns = [
    url(r'^images/(?P<pcid>.*)/$', ImageView.as_view()),
    url(r'^search/(?P<search_term>.*)/$', SearchView.as_view()),
]
