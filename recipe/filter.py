from tag.models import Category, Tag


def get_tag(name):
    return str(Tag.objects.get(name=name).pk)


def get_category(name):
    return str(Category.objects.get(name=name).pk)


filter = [
    {
        "title": "Category",
        "name": "category",
        "options": [
            {"title": "Maison", "value": get_category("Maison")},
            {"title": "Corps", "value": get_category("Corps")},
            {"title": "Visage", "value": get_category("Visage")},
            {"title": "Cheveux", "value": get_category("Cheveux")},
            {"title": "Bien-être", "value": get_category("Bien-être")},
        ],
    },
    {
        "title": "Tag",
        "name": "tags",
        "options": [
            {"title": "Permier pas", "value": ""},
            {"title": "Zéro-déchet", "value": get_tag("Zéro-déchet")},
            {
                "title": "Ingrédients du frigo",
                "value": get_tag("Ingrédients du frigo"),
            },
        ],
    },
    {
        "title": "Temps",
        "name": "duration",
        "options": [
            {"title": "Moins de 15 min", "value": 15},
            {"title": "Moins de 30 min", "value": 30},
            {"title": "Moins de 1 heure", "value": 60},
        ],
    },
    {
        "title": "Difficulté",
        "name": "difficulty",
        "options": [
            {"title": "Facile", "value": "BEGINNER"},
            {"title": "Intermediaire", "value": "INTERMEDIATE"},
            {"title": "Expert", "value": "ADVANCED"},
        ],
    },
]
