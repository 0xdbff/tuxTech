from django.contrib import admin

from .models.category import Category
from .models.brand import Brand
from .models.unit import Unit
from .models.media import Media
from .models.variant import Variant
from .models.base_info import BaseInfo
from .models.variant_media import VariantMedia
from .models.sub_category import SubCategory
from .models.type import Type

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Type)
admin.site.register(Variant)
admin.site.register(VariantMedia)
admin.site.register(Media)
admin.site.register(BaseInfo)
admin.site.register(Unit)
