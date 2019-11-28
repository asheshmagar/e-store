from rest_framework import routers
from contact.views import ContactViewset
from product.views import ProductViewset
from login.views import RegisterViewSet, LoginViewSet, LogoutViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewset)
router.register(r'products', ProductViewset)
router.register(r'login', LoginViewSet)
router.register(r'logout', LogoutViewSet)
router.register(r'register', RegisterViewSet)