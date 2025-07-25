from django.urls import include, path, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

app_name = 'blogicum'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
          'auth/registration/',
          CreateView.as_view(
          template_name='registration/registration_form.html',
          form_class=UserCreationForm,
          success_url='/auth/login/',
          ),
      name='registration',
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
