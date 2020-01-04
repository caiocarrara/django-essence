from django.db import models


class EssencePersistentQuerySet(models.QuerySet):
    def delete(self):
        _rows_count = self.update(deleted=True)
        deleted = _rows_count > 0
        return deleted, _rows_count


class EssencePersistentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return EssencePersistentQuerySet(self.model, using=self._db)

    def all(self):
        return self.filter(deleted=False)
