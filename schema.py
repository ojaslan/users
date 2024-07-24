import graphene
from graphene_django import DjangoObjectType
from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("user_id", "username", "first_name", "last_name", "email", "phone_number", "role")

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, user_id=graphene.Int())

    def resolve_all_users(root, info):
        return User.objects.all()  # Fix: 'User' instead of 'Users'

    def resolve_user_by_id(root, info, user_id):
        try:
            return User.objects.get(pk=user_id)  # Fix: 'User' instead of 'Users'
        except User.DoesNotExist:  # Fix: 'User' instead of 'Users'
            return None

schema = graphene.Schema(query=Query)