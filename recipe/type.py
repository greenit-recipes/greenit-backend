import graphene
from graphene.types.generic import GenericScalar
from graphene.types.scalars import String
from graphene_django import DjangoObjectType
from comment.models import CommentRecipe
from comment.type import CommentType

from ingredient.type import IngredientAmountType
from utensil.type import UtensilAmountType

from .models import Made, Recipe

# Imports language choices from .models to prevent code duplication
LanguageFilter = graphene.Enum.from_enum(Recipe.LanguageChoice)
DifficultyFilter = graphene.Enum.from_enum(Recipe.DifficultyChoice)

class MadeType(DjangoObjectType):
    class Meta:
        model = Made
        fields = (
            'recipe',
            'amount',
            'user'
        )


class RecipeType(DjangoObjectType):
    instructions = GenericScalar()

    def resolve_ingredients(parent, info):
        return parent.ingredients.through.objects.filter(recipe__id=parent.id)

    ingredients = graphene.List(
        graphene.NonNull(IngredientAmountType), default_value=[]
    )
    
    
    def resolve_utensils(parent, info):
        return parent.utensils.through.objects.filter(recipe__id=parent.id)

    utensils = graphene.List(
        graphene.NonNull(UtensilAmountType), default_value=[]
    )
    
    ################ comments ################
    def resolve_comments(parent, info):
        return CommentRecipe.objects.filter(recipe_id=parent.id).order_by('-created_at')

    
    @staticmethod
    def resolve_number_of_comments(parent, info):
        return CommentRecipe.objects.filter(recipe_id=parent.id).count()
    
    comments = graphene.List(
        graphene.NonNull(CommentType), default_value=[]
    )
    number_of_comments = graphene.Int()
    
    ################ substance ################
    number_of_substances = graphene.Int()
    
    @staticmethod
    def resolve_number_of_substances(self, parent):
        return self.substances.count()
    
    ################ likes ################
    number_of_likes = graphene.Int()
    is_liked_by_current_user = graphene.Boolean()
    
    @staticmethod
    def resolve_number_of_likes(self, parent):
        return self.likes.count()
    
    @staticmethod
    def resolve_is_liked_by_current_user(self, info):
        if info.context.user.is_authenticated:
            return self.likes.filter(id=info.context.user.id).exists()
        else:
            return False
        
    ################ favorites ################
    number_of_favorites = graphene.Int()
    is_add_to_favorite_by_current_user = graphene.Boolean()

    @staticmethod
    def resolve_number_of_favorites(self, parent):
        return self.favorites.count()    
    
    @staticmethod
    def resolve_is_add_to_favorite_by_current_user(self, info):
        if info.context.user.is_authenticated:
            return self.favorites.filter(id=info.context.user.id).exists()
        else:
            return False
        
     ################ mades ################
    is_made_by_current_user = graphene.Boolean()

    @staticmethod
    def resolve_is_made_by_current_user(self, info):
        if info.context.user.is_authenticated:
            return self.made.filter(user_id=info.context.user.id).exists()
        else:
            return False
        
    ################ ingredients ################
    number_of_ingredients = graphene.Int()
    @staticmethod
    def resolve_number_of_ingredients(parent, info):
        return parent.ingredients.through.objects.filter(recipe__id=parent.id).count()
    
    class Meta:
        model = Recipe
        fields = (
            'id',
            'name',
            'description',
            'text_associate',
            'video_url',
            'language',
            'difficulty',
            'ingredients',
            'rating',
            'duration',
            'author',
            'image',
            'tags',
            'substances',
            'nbr_view',
            'price_min',
            'price_max',
            'money_saved',
            'plastic_saved',
            'category',
            'utensils',
            'instructions',
            'url_id',
            'video',
            'expiry',
            'title_seo',
            'meta_description_seo',
            'notes_from_author',
            'nbr_view',
            'created_at'
        )

class RecipeConnection(graphene.relay.Connection):
    class Meta:
        node = RecipeType
