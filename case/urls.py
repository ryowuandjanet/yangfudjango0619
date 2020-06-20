from django.urls import path
from .views import *

urlpatterns = [
	path('', CaseListView.as_view(), name='home'),
	path('case/<int:pk>/',CaseDetailView.as_view(),name="case_detail" ),
	path('case/new/',CaseCreateView.as_view(),name="case_new" ),
	path('case/<int:pk>/edit/',CaseUpdateView.as_view(),name="case_edit" ),
	path('case/<int:pk>/delete/',CaseDeleteView.as_view(),name="case_delete" ),
	path('ajax/load_township/', load_township, name='ajax_load_township'),
]
