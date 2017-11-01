from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('hello.urls')),
    url(r'', include('post.urls')),
    url(r'', include('signupLogin.urls')),
    url(r'^userprofile/', include('userprofile.urls')),
    url(r'', include('order.urls')),
    url(r'', include('report.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
