from django.db import models
# from .validators import FileValidator
from django.core.validators import FileExtensionValidator


# validate_file = FileValidator(max_size=1024 * 100, content_types=('application/xml',))
class Document(models.Model):
#     description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',

            validators=[FileExtensionValidator( ['doc', 'docx'] ) ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

class TxtToDoc(models.Model):
        text = models.TextField()
        