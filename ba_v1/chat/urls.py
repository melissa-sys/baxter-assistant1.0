from django.urls import path
from django.urls import include

from . import views
from .views import HomePage
#from .views import Chat
from .views import SetupBaxter
from .views import Cosa
#from .views import messageDelete
from .viewset import MessageViewSet


from rest_framework import routers

router = routers.SimpleRouter()  # Me da las rutas
router.register('message', MessageViewSet)

app_name = 'chat'
urlpatterns = [
    path('home/', HomePage.as_view(), name='home'),
    path('send/', views.receiveChatInfo, name='send'),
    path('cosa/', Cosa.as_view(), name='cosa'),
    #path('chat/', Chat.as_view(), name='chat'),
    #path('delete/', messageDelete, name='delete'),

    # Pre-programming baxter actions
    path('homeBaxter/', SetupBaxter.as_view(), name='bax_home'),

    # API urls
    path('api/', include(router.urls), name='api'),
]
