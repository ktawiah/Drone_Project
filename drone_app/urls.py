from django.urls import path
from . import views

app_name = "drone_app"

urlpatterns = [
    path("", views.ApiRootView.as_view(), name="api-root"),
    path("drones/", views.DroneList.as_view(), name="drone-list"),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name="drone-detail"),
    path(
        "drone_categories/",
        views.DroneCategoryList.as_view(),
        name="drone-category-list",
    ),
    path(
        "drone_categories/<int:pk>/",
        views.DroneCategoryDetail.as_view(),
        name="drone-category-detail",
    ),
    path("pilots/", views.PilotList.as_view(), name="pilot-list"),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name="pilot-detail"),
]
