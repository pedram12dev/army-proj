from django.urls import path
from . import views


app_name = 'core'
urlpatterns = [
    path('',views.HomeView.as_view(),name='base_page'),
    path('page-one/', views.PageOneView.as_view(), name='page_one'),
    path('page-two/', views.PageTwoView.as_view(), name='page_two'),
    path('page-three/', views.PageThreeView.as_view(), name='page_three'),
    path('page-four/', views.PageFourView.as_view(), name='page_four'),
    path('page-five/', views.PageFiveView.as_view(), name='page_five'),
    path('page-six/', views.PageSixView.as_view(), name='page_six'),
    path('page-seven/', views.PageSevenView.as_view(), name='page_seven'),
    path('page-eight/', views.PageEightView.as_view(), name='page_eight'),
    path('page-nine/', views.PageNineView.as_view(), name='page_nine'),
    path('page-ten/', views.PageTenView.as_view(), name='page_ten'),
    path('page-eleven/', views.PageElevenView.as_view(), name='page_eleven'),
    path('page-twelve/', views.PageTwelveView.as_view(), name='page_twelve'),
    path('page-thirteen/', views.PageThirteenView.as_view(), name='page_thirteen'),
    path('page-fourteen/', views.PageFourteenView.as_view(), name='page_fourteen'),
    path('page-fifteen/', views.PageFifteenView.as_view(), name='page_fifteen'),
    path('page-sixteen/', views.PageSixteenView.as_view(), name='page_sixteen'),
    path('admin-page/', views.AdminDataView.as_view(), name='admin-data'),
    path('admin-data/<str:file_name>/', views.download_file,name='download_data'),
]