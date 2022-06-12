from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_book(request, recipe_name, servings=1):

    for x in DATA[recipe_name]:
        DATA[recipe_name][x] = DATA[recipe_name][x] * servings
    context = {
            'recipe': DATA[recipe_name]
        }

    return render(request, 'calculator/index.html', context)

