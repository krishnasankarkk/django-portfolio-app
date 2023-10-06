from .models import Menu, ChildMenu

def menu(request):
    menus = Menu.objects.all().order_by("id")
    menu_array = []
    for menu in menus:
        item = {
            'parent': menu.name,
            'child': ChildMenu.get_all_menus_by_parentid(menu.id),
        }
        menu_array.append(item)
    data = {
        'menus': menu_array
    }
    return data