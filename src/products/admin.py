from django.contrib import admin

from .models.category import Category
from .models.brand import Brand
from .models.unit import Unit
from .models.media import Media
from .models.variant import Variant
from .models.base_info import BaseInfo

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Media)
admin.site.register(Variant)
admin.site.register(BaseInfo)
admin.site.register(Unit)

# Register your models here.
