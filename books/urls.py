"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from getbooks import views as getbooks_views
from getbooks import books as getbooks_books

urlpatterns = [
	url(r'^books$', getbooks_views.index, name='books'),
    url(r'^bookslist$', getbooks_books.getbookslist, name='downloadbook'),
    url(r'^downloadbook/(.*)$', getbooks_books.downloadbook, name='downloadbook'),
	url(r'^geturl$', getbooks_views.geturl, name='geturl'),
	url(r'^getbook/$', getbooks_views.getbook, name='getbook'),
	url(r'^$',getbooks_views.index),
    url(r'^admin/', admin.site.urls),
]
