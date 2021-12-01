from .models import les_ville ,les_post

def  extras(request):
    cities = les_ville.objects.all()
    post = les_post.objects.filter()[:4]
    return {
        'cities' : cities,
        'post': post
    }



