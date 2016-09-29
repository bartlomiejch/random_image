import random
from dummy_images.models import DummyImage
from django.views.generic.base import TemplateView


class ImageView(TemplateView):
    template_name = "index.html"

    def index(self, **kwargs):
        imgs = DummyImage.objects.all()
        img = random.choice(imgs)
        context = super(ImageView, self).get_context_data(**kwargs)
        print (img.image.url)
        context['img'] = img
        return context
