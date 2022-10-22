from django.urls import path
from graphene_django.views import GraphQLView
from quiz.schema import schema

urlpatterns = [
    # use only single route to access graphql
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema))
]