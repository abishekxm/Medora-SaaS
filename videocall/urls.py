from django.urls import path

from .views import (
    CreateVideoRoom,
    VideoRoomDetail,
    DoctorRooms,
    PatientRooms,
    EndConsultation,
)

urlpatterns = [
    path(
        "create/<int:appointment_id>/",
        CreateVideoRoom.as_view(),
        name="create-video-room",
    ),

    path(
        "<int:pk>/",
        VideoRoomDetail.as_view(),
        name="video-room-detail",
    ),

    path(
        "doctor/",
        DoctorRooms.as_view(),
        name="doctor-video-rooms",
    ),

    path(
        "patient/",
        PatientRooms.as_view(),
        name="patient-video-rooms",
    ),

    path(
        "end/<int:pk>/",
        EndConsultation.as_view(),
        name="end-consultation",
    ),
]