import random
from django.views.generic.base import TemplateView
from django.http import Http404
from dummy_images.models import DummyImage


class ImageView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        imgs = DummyImage.objects.all()
        if len(imgs) == 0:
            raise Http404
        img = random.choice(imgs)
        context = super(ImageView, self).get_context_data(**kwargs)
        size = self.kwargs['size']
        context['size'] = size
        context['img'] = img
        return context
