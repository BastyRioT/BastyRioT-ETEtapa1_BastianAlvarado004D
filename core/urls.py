from django.urls import path
from .views import index, verdatos, form_colabora, mod_colabora, del_colabora

urlpatterns = [
    path('', index, name="index"),
    path('verdatos', verdatos, name="verdatos"),
    path('form_colabora', form_colabora, name="form_colabora"),
    path('mod_colabora/<id>', mod_colabora, name="mod_colabora"),
    path('del_colabora/<id>', del_colabora, name="del_colabora")

]
