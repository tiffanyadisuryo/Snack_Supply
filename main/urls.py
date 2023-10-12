from django.urls import path
from main.views import show_main
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register 
from main.views import login_user
from main.views import logout_user
from main.views import add_item
from main.views import min_item
from main.views import remove_item
from main.views import get_item_json
from main.views import create_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create_item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_item/<int:id>/', add_item, name='add_item'),
    path('min_item/<int:id>/', min_item, name='min_item'),
    path('remove_item/<int:id>/', remove_item, name='remove_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax')
]
