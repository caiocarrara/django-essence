Django Essence
==============

Simple project with base common resources for almost any Django project.

Installation
------------

The installation is performed by using pip::

  pip install django-essence

To enable `django-essence` in a Django project it's needed to add it to `INSTALLED_APPS`
in the project settings file::

  INSTALLED_APPS = [
      ...
      'django_essence',
      ...
  ]

Resources
---------

The current implementation of `django-essence` offers only common base abstract models
listed below:

  * `TimestampedModel`: model with attributes (fields) useful for audit
    purposes. Fields:

    * `created_at`
    * `updated_at`

  * `EssenceModel`: model inherited from `TimestampedModel` with an `UUIDField`. Fields:

    * `id`
    * `created_at`
    * `updated_at`

  * `EssencePersistentModel`: model inherited from `EssenceModel` with "soft delete"
    feature. Fields:

    * `id`
    * `created_at`
    * `updated_at`
    * `deleted`

  * `EssenceSlugModel`: model inherited from `EssenceModel` with a enhanced `slug` field.
    Fields:

    * `id`
    * `created_at`
    * `updated_at`
    * `slug`


All models are available importing from::

    from django_essence.models import *


Running tests (development)
---------------------------

First install development dependencies with::

  make install

Than run tests with::

  pytest