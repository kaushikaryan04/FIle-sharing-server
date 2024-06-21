from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FileUpload(models.Model) :
    choices = (
        ('pptx' , 'PowerPoint'),
        ('docx' , 'Word Document'),
        ('xlsx' , 'Excel File')
    ) 
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10 , choices=choices)
    file = models.FileField(upload_to="FileUploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    