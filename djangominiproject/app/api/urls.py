from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import (
    EpViewSet,
    # SingleCategoryRecipe, RecipesViewSet,
    # PublicRecipes, PublicRecipesDetail,
)

router = DefaultRouter()
# router.register('categories', CategoryViewSet, basename='categories')
# router.register('recipes', RecipesViewSet, basename='recipes')
router.register('eps', EpViewSet, basename='eps')
# router.register('songs', RecipesViewSet, basename='songs')

custom_urlpatterns = [
    # url(r'categories/(?P<category_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    url(r'eps/(?P<ep_pk>\d+)', Eps.as_view(), name='eps'),
    # url(r'eps/(?P<ep_pk>\d+)/recipes$', CategoryRecipes.as_view(), name='category_recipes'),
    # url(r'categories/(?P<category_pk>\d+)/recipes/(?P<pk>\d+)$', SingleCategoryRecipe.as_view(),
    #     name='single_category_recipe'),
    # url(r'public-recipes/$', PublicRecipes.as_view(), name='public_recipes'),
    # url(r'public-recipes/(?P<pk>\d+)/$', PublicRecipesDetail.as_view(), name='public_recipes_detail')
]
urlpatterns = router.urls
urlpatterns += custom_urlpatterns