import graphene

from ingredient.models import Ingredient
from tag.models import Category, Tag
from utensil.models import Utensil

from .models import Recipe
from .type import DifficultyFilter, LanguageFilter, RecipeType


class RecipeInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    video_url = graphene.String()
    duration = graphene.Int()
    tags = graphene.List(graphene.String)
    ingredients = graphene.List(graphene.String)
    utensils = graphene.List(graphene.String)
    expiry = graphene.String()
    notes_from_author = graphene.String()
    category = graphene.List(graphene.String)
    language = LanguageFilter()
    difficulty = DifficultyFilter()
    # instructions
    # image


class CreateRecipe(graphene.Mutation):
    class Arguments:
        data = RecipeInput(required=True)

    recipe = graphene.Field(RecipeType)

    def mutate(root, info, data):
        recipe = Recipe.objects.create(
            name=data.name,
            description=data.description,
            video_url=data.video_url,
            duration=data.duration,
            expiry=data.expiry,
            notes_from_author=data.notes_from_author,
            language=data.language,
            difficulty=data.difficulty,
        )
        recipe.tags.set([Tag.objects.get(pk=id) for id in data.tags])
        recipe.ingredients.set(
            [Ingredient.objects.get(pk=id) for id in data.ingredients]
        )
        recipe.utensils.set([Utensil.objects.get(pk=id) for id in data.utensils])
        recipe.category.set([Category.objects.get(pk=data.category)])
        recipe.save()

        return CreateRecipe(recipe=recipe)
