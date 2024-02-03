from django.views.generic import TemplateView

class HomePageView(TemplateView):
 template_name = 'home.html'


# We’re using Django’s TemplateView generic class-based view which means we only need to specify our template_name to use it.