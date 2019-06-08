from django.contrib import admin
from django.urls import path, include
# from graphene_django.views import GraphQLView

# from podaripodarok.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/', include('pp_app.urls')),
    # path(r'graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
