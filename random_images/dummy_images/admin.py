from django.contrib import admin
from dummy_images.models import DummyImage


class DummyImageAdmin(admin.ModelAdmin):
    class Meta:
        model = DummyImage


admin.site.register(DummyImage, DummyImageAdmin)
