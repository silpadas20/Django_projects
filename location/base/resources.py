from import_export import resources
from .models import Direction

class DirectionResource(resources.ModelResource):
    class Meta:
        model = Direction
