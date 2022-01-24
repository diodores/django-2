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
    }
}


def get_recipe(request, dishes):
    servings = int(request.GET.get('servings', 1))
    new_dish = {}
    for dish, ingredients in DATA.items():
        if dishes == dish:
            for item, nums in ingredients.items():
                new_dish[item] = nums * servings
    context = {
        'recipe': new_dish,
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)
