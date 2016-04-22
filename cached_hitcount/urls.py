from django.conf.urls import url
from .views import update_hit_count_ajax



urlpatterns = [
    url(r'$', update_hit_count_ajax, name='update_hit_count_ajax')
]
