from rest_framework import routers

from . import views


def get_coffee_app_router():
    coffee_app_router = routers.DefaultRouter()
    coffee_app_router.register(r'coffee-drinker', views.CoffeeDrinkerView)
    coffee_app_router.register(r'coffee-tasting', views.CoffeeTastingView)
    coffee_app_router.register(r'roasted-coffee', views.RoastedCoffeeView)
    return coffee_app_router