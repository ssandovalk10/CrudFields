from django.urls import path

from apps.bancoCampos.views import FieldsBankView


urlpatterns = [
   path('fieldsbank/', FieldsBankView.as_view(), name="fieldsbank")

]
