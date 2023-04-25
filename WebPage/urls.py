##First Main Page
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Victor's Portfolio"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Wassup"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls'))    
]
