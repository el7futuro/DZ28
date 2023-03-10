import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from ads.models import Category


class CategoriesView(ListView):
    model = Category
    queryset = Category.objects.all().order_by('name')

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list, 10)
        num_pages = request.GET.get('page')
        pat_obj = paginator.get_page(num_pages)
        cities = []
        for i in pat_obj:
            cities.append({
                "id": i.id,
                "name": i.name,

            })

        response = {
            'total': paginator.count,
            'num_pages': paginator.num_pages,
            'fields': cities
        }
        return JsonResponse(response, safe=False)


class CategoryViewDetail(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object = self.get_object()

        return JsonResponse({"name": self.object.name
                             }, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"]
        )

        return JsonResponse(
            {
                "id": category.id,
                "text": category.name
            }
        )


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        cat_data = json.loads(request.body)
        self.object.name = cat_data['name']
        self.object.save()

        return JsonResponse({'id': self.object.id,
                             'name': self.object.name})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({'status': 'ok'}, safe=False)