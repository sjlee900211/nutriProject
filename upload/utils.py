import os
from uuid import uuid4

from django.utils import timezone


def upload_to_func(instance, filename):
    prefix = timezone.now().strftime("%Y/%m/%d")
    file_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower() # 확장자 추출
    print(instance.user.user_id)
    return "/".join(
        [prefix, file_name+extension,]
    )
