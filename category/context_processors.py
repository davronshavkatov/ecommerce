from .models import Category
def menu_links(request):
    catigoryies= Category.objects.all()
    return {'catigoryies':catigoryies}