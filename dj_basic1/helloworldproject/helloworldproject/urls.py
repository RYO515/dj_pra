from django.contrib import admin
from django.urls import path, include
from .views import helloworldfunction, HelloworldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloworldView.as_view()),
    path('apppp/', include('helloworldapp.urls'))
]
