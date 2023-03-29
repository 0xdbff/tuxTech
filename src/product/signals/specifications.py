import json
import os
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from ..models import Specification

# Load default specifications from JSON file
default_specifications_path = os.path.join(
    os.path.dirname(__file__), "json/default_specifications.json"
)
with open(default_specifications_path, "r") as f:
    default_specifications = json.load(f)


@receiver(post_migrate)
def load_default_specifications(sender, **kwargs):
    for spec in default_specifications:
        Specification.objects.get_or_create(key=spec["key"], value=spec["value"])
