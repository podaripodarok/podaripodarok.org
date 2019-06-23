import graphene
# import graphql_jwt
from pp_app import schema


class Query(schema.Query, graphene.ObjectType):
    pass


class Mutation(schema.Mutation, graphene.ObjectType):
    #token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    #verify_token = graphql_jwt.Verify.Field()
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

