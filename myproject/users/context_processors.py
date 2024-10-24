from myapp.utils import menu


def get_recipe_context(request):#контекстные процессор. во все шаблоны юудет передаваться меню
    return {'mainmenu': menu}