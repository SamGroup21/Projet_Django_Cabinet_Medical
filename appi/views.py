# views.py
from django.shortcuts import render, get_object_or_404  # Import indispensable pour l'étape 5
from .models import Article  # Import indispensable pour toutes les étapes CRUD


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/detail.html', {'article': article})
# views.py
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})
def article_create(request):
    titre = request.GET.get('titre')
    contenu = request.GET.get('contenu')
    message = ""
    if titre and contenu:
        Article.objects.create(titre=titre, contenu=contenu)
        message = "Article créé."
    else:
        message = "Titre ou contenu manquant."
    return render(request, 'articles/create.html', {'message': message})
def article_update(request, id):
    article = get_object_or_404(Article, id=id)
    titre = request.GET.get('titre')
    contenu = request.GET.get('contenu')
    message = ""
    if titre and contenu:
        article.titre = titre
        article.contenu = contenu
        article.save()
        message = "Article modifié."
    else:
        message = "Paramètres manquants."
    return render(request, 'articles/update.html', {'article': article, 'message': message})
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    confirm = request.GET.get('confirm')
    message = ""
    if confirm == "oui":
        article.delete()
        message = "Article supprimé."
    else:
        message = "Confirmez avec ?confirm=oui"
    return render(request, 'articles/delete.html', {'message': message})
def article_form(request):
    return render(request, 'articles/form.html')

def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    confirm = request.GET.get('confirm')
    message = ""
    if confirm == "oui":
        article.delete()
        message = "Article supprimé."
        context = {'message': message}
    else:
        message = "Confirmez avec ?confirm=oui"
        context = {'article': article, 'message': message}
    return render(request, 'articles/delete.html', context)