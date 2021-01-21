from django.shortcuts import render

# Create your views here.
def posts_list(request):
    names = ['Oleg', 'Olga']
    context = {
        'names': names
    }
    return render(request, 'blog/index.html', context=context)
