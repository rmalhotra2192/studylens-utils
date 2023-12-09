from django.db import models
from ..models.resources import Resource


class ExternalDataProvider(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    logo = models.CharField(max_length=512, null=True)

    class Meta:
        app_label = "studylens_models"


class ExternalUrl(models.Model):
    SERVICE_TYPES = [
        ("resource-purchase", "Resource Purchase"),
        ("resource-view", "Resource View"),
    ]

    url = models.CharField(max_length=512)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    external_provider = models.ForeignKey(
        ExternalDataProvider, on_delete=models.CASCADE
    )
    external_provider_service_type = models.CharField(
        choices=SERVICE_TYPES, max_length=128, null=True
    )

    class Meta:
        app_label = "studylens_models"


class Thumbnail(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    external_provider = models.ForeignKey(
        ExternalDataProvider, on_delete=models.CASCADE
    )
    url = models.CharField(max_length=500)
    size = models.IntegerChoices("size", "small medium large extra_large")

    class Meta:
        app_label = "studylens_models"


class Metric(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    external_provider = models.ForeignKey(
        ExternalDataProvider, on_delete=models.CASCADE, null=True
    )
    metric_category = models.CharField(
        max_length=128, null=True
    )  # e.g. "ratings, engagement, etc."
    metric_key = models.CharField(
        max_length=128, null=True
    )  # e.g. "views, likes, etc."
    metric_type = models.CharField(
        max_length=128, null=True
    )  # e.g. "integer, float, etc."
    metric_value = models.CharField(max_length=128, null=True)  # e.g. "4.5, 100, etc."
    metric_max = models.CharField(max_length=128, null=True)  # e.g. "5, 100, etc."

    class Meta:
        app_label = "studylens_models"


class Tag(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    tag = models.CharField(max_length=128)

    class Meta:
        app_label = "studylens_models"
