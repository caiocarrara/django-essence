from django.db import models

from django_essence.models import EssencePersistentModel, EssenceSlugModel, EssenceTimestampedModel


class TEssenceTimestampedModel(EssenceTimestampedModel):
    pass


class TEssencePersistentModel(EssencePersistentModel):
    pass


class TEssenceSlugModel(EssenceSlugModel):
    field_to_slug = 'title'

    title = models.CharField(max_length=30)
