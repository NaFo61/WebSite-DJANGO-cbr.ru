from django.shortcuts import render


def views_first_page(request):
    context = {}
    template_dir = 'first_page/first_page.html'
    return render(request, template_dir, context=context)