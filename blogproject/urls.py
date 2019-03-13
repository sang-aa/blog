from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static # 이거랑 이거 위에거는 media 파일을 사용하기 위해서 import 해와야 하는 것임 걍 외우셈

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>',blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name='new'),
    path('blog/create', blogapp.views.create, name="create"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#걍 외우셈
