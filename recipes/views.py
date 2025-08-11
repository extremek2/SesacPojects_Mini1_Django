from django.shortcuts import render, redirect

from .models import RecipeInfo, RecipeCourse, RecipeIngredients

def recipes_index(request):
    recipe_info = RecipeInfo.objects.all()
    recipe_course = RecipeCourse.objects.all()
    recipe_ingredients = RecipeIngredients.objects.all()

    return render(request, 'recipes/index.html',
                  context = {'recipe_info': recipe_info,
                             'recipe_course': recipe_course,
                             'recipe_ingredients': recipe_ingredients})

def recipe_detail(request,pk):
    recipe_info = RecipeInfo.objects.get(pk=pk)
    recipe_course = RecipeCourse.objects.get(pk=pk)
    recipe_ingredients = RecipeIngredients.objects.get(pk=pk)
    return render(request, 'recipes/recipe_detail.html',
                  context = {'recipe_info': recipe_info,
                             'recipe_course': recipe_course,
                             'recipe_ingredients': recipe_ingredients})