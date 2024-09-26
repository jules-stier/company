from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "666-666-6666"
        return context
    
class ProductsPageView(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_1"] = "Thumbtacks"
        context["product_2"] = "10 lb Wheel of Cheese"
        context["product_3"] = "2004 Subaru Forester Engine Replacement"
        context["product_4"] = "T-Shirt that says 'Howdy'"
        return context