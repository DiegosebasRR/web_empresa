from .models import Link
def extender_contexto(request):
    ctx ={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx