import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django_essence.managers import EssencePersistentManager


class EssenceTimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EssenceModel(EssenceTimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class EssencePersistentModel(EssenceModel):
    deleted = models.BooleanField(default=False, editable=False)

    objects = EssencePersistentManager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class EssenceSlugModel(EssenceModel):
    slug = models.SlugField(
        _("Slug"), max_length=250, unique=True, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            value_to_slugify = getattr(self, self.field_to_slug)
            self.slug = slugify(value_to_slugify)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
