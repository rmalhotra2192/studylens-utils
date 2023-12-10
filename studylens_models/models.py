from django.db import models


class Resource(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.IntegerField(null=True)
    last_review_status = models.CharField(max_length=128, null=True)
    last_review_by = models.CharField(max_length=128, null=True)
    last_review_on = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = "studylens_models"


class Book(Resource):
    isbn = models.CharField(max_length=13, unique=True, null=True)
    authors = models.CharField(max_length=128, null=True)
    publisher = models.CharField(max_length=128, null=True)
    first_published_date = models.DateField(null=True)
    last_published_date = models.DateField(null=True)
    page_count = models.IntegerField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")

    class Meta:
        app_label = "studylens_models"


class Course(Resource):
    course_id = models.CharField(max_length=128, unique=True, null=True)
    course_provider = models.CharField(max_length=128, null=True)
    course_instructor = models.CharField(max_length=128, null=True)
    course_free = models.BooleanField(default=False)
    course_mode_of_instruction = models.CharField(
        choices=[
            ("online-recorded", "Online Recorded"),
            ("online-live", "Online Live"),
            ("offline", "Offline"),
            ("text", "Text"),
            ("mix-text-video", "Mix of Text and Video"),
            (
                "mix-text-video-interactivecode",
                "Mix of Text, Video and Interactive Code",
            ),
            ("mix-text-interactivecode", "Mix of Text and Interactive Code"),
        ],
        max_length=128,
        null=True,
    )
    course_duration_scale = models.CharField(
        choices=[
            ("hours", "Hours"),
            ("days", "Days"),
            ("weeks", "Weeks"),
            ("months", "Months"),
            ("years", "Years"),
        ],
        max_length=128,
        null=True,
    )
    course_duration_value = models.IntegerField(null=True)
    course_start_date = models.DateField(null=True)
    course_end_date = models.DateField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")

    class Meta:
        app_label = "studylens_models"


class Video(Resource):
    video_id = models.CharField(max_length=128, unique=True, null=True)
    video_provider = models.CharField(max_length=128, null=True)
    channel = models.CharField(max_length=128, null=True)
    upload_date = models.DateField(null=True)
    duration = models.IntegerField(null=True)
    language = models.CharField(max_length=128, null=True, default="English")
    course_instance = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    course_sequence = models.IntegerField(null=True)

    class Meta:
        app_label = "studylens_models"


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
