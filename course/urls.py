
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_view
from django.contrib.auth import views as auth_views
from blog.sitemap import MyCOurseSiteMap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'news' : MyCOurseSiteMap(),
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/',sitemap, {'sitemaps':sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('', include('blog.urls')),
    path('register/',users_view.register,name="register"),
    path('profile/',users_view.profile,name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name="logout"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
