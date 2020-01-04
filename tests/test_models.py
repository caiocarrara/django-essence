from datetime import datetime

import pytest
from freezegun import freeze_time
from mixer.backend.django import mixer

from tests.models import TEssencePersistentModel, TEssenceSlugModel, TEssenceTimestampedModel

pytestmark = pytest.mark.django_db


@pytest.mark.parametrize("field_to_check", ("created_at", "updated_at"))
def test_timestamped_model_is_created_with_correct_defaults(field_to_check):
    freezed_datetime = "2020-01-01 12:00:00"
    expected_datetime = datetime.strptime(freezed_datetime, "%Y-%m-%d %H:%M:%S")

    with freeze_time(freezed_datetime):
        model_instance = mixer.blend(TEssenceTimestampedModel)
        assert getattr(model_instance, field_to_check) == expected_datetime


def test_timestamped_model_has_updated_at_updated():
    freezed_datetime = "2020-01-01 12:00:00"
    expected_datetime = datetime.strptime(freezed_datetime, "%Y-%m-%d %H:%M:%S")

    model_instance = mixer.blend(TEssenceTimestampedModel)

    with freeze_time(freezed_datetime):
        model_instance.save()
        assert model_instance.updated_at == expected_datetime


def test_persistent_model_is_not_deleted():
    model_instance = mixer.blend(TEssencePersistentModel)
    model_instance.delete()
    model_instance.refresh_from_db()
    assert TEssencePersistentModel.objects.get(id=model_instance.id)
    assert model_instance.deleted


def test_persistent_model_is_not_deleted_via_manager():
    model_instance = mixer.blend(TEssencePersistentModel)
    TEssencePersistentModel.objects.filter(pk=model_instance.pk).delete()
    model_instance.refresh_from_db()
    assert TEssencePersistentModel.objects.get(id=model_instance.id)
    assert model_instance.deleted


def test_persistent_model_manager_delete_returns_deleted_count():
    _models_count = 2
    mixer.cycle(_models_count).blend(TEssencePersistentModel)
    deleted, count = TEssencePersistentModel.objects.all().delete()
    assert deleted
    assert count == _models_count


def test_persistent_model_manager_doesnt_return_deleted_objects():
    model_instance = mixer.blend(TEssencePersistentModel)
    model_instance.delete()
    assert not TEssencePersistentModel.objects.all()


def test_slug_model_slugify_on_save():
    slugged_model = mixer.blend(TEssenceSlugModel, title="title for test")
    assert slugged_model.slug == "title-for-test"
