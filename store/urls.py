
from django.contrib import admin
from django.urls import path , include


admin.site.site_header = "Book Store"
admin.site.site_title = "Book Store site admin"
admin.site.index_title = "Book Store site administration"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('userapp.urls')),

]
