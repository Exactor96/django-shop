from os import path
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
from django.shortcuts import render
from shop.models import Category, Product

class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_products = Product.objects.filter(name__contains=question)

            # forming a URL string that will contain the last request.
            # This is important for correct operation of pagination
            context['last_question'] = f'?q={question}'

            current_page = Paginator(search_products, 10)

            page = request.GET.get('page')
            try:
                context['products'] = current_page.page(page)
            except PageNotAnInteger:
                context['products'] = current_page.page(1)
            except EmptyPage:
                context['products'] = current_page.page(current_page.num_pages)

        return render(request,template_name=self.template_name, context=context)



def search_index(request):
    return render(request,'search/index.html')

