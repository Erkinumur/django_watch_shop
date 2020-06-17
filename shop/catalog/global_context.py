from .models import Group, Brand

def get_categories_brands(request):
    '''Вывод всех категорий и брэндов'''

    categories = Group.objects.all()
    brands = Brand.objects.all()
    return {'all_categories': categories, 'all_brands': brands}