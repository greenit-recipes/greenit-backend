from django.core.exceptions import ValidationError

def file_size_image(value):
    limit = 10000000 # 10 mo
    if value.size > limit:
        raise ValidationError('Image too large. Size should not exceed 10000000 mo.')
    
def file_size_video(value):    
    limit = 800000000  # 800 mo
    if value.size > limit:
        raise ValidationError('Video too large. Size should not exceed 800 mo.')