from django.shortcuts import render


def about(request):
    template = 'pages/about.html'
    context = {'about': about}
    return render(request, template, context)


def rules(request):
    template = 'pages/rules.html'
    context = {'rules': rules}
    return render(request, template, context)
