from rest_framework import routers

from . import views


def get_user_coffee_app_router():
    coffee_app_router = routers.DefaultRouter()
    coffee_app_router.register(r'coffee-tasting', views.CoffeeTastingView)
    coffee_app_router.register(r'login', views.LoginView)
    coffee_app_router.register(r'register', views.RegisterView)
    return coffee_app_router

def get_backend_coffee_app_router():
    coffee_app_router = routers.DefaultRouter()
    coffee_app_router.register(r'roasted-coffee', views.RoastedCoffeeView)
    coffee_app_router.register(r'processing-type', views.ProcessingTypeView)
    coffee_app_router.register(r'coffee-farm', views.CoffeeFarmView)
    coffee_app_router.register(r'unprocessed-bean', views.UnprocessedBeanView)
    coffee_app_router.register(r'coffee-batch', views.CoffeeBatchView)

    return coffee_app_router