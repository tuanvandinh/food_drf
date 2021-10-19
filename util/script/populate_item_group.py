import django_base
from core.models import ItemGroup, Item, AddOn
import sys, json, glob
from django.utils import timezone

# from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile
from PIL import Image


item_group_path = sys.argv[1]
images = sorted(glob.glob(sys.argv[2] + "/*.jpg"))


def prepare_img(path, image, count):
    img = Image.open(path)
    output_file = StringIO()
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(output_file, "JPEG")
    image.save(str(count) + ".jpg", ContentFile(output_file.getvalue()), save=False)


item_group_file = json.load(open(item_group_path, "r"))
count = 0
for item in item_group_file["itemGroups"]:
    count += 1
    item_group = ItemGroup()
    for key, val in item.items():
        if key == "id":
            item_group.id = val
            for img_path in images:
                i = img_path.strip(sys.argv[2])
                i = i.split(".")[0]
                if int(val) == int(i):
                    #                    print(val)
                    #                    print(i)
                    #                    print(img_path)
                    img = Image.open(img_path)
                    buffer = BytesIO()
                    img.save(fp=buffer, format="JPEG")
                    item_group.image.save(i, ContentFile(buffer.getvalue()))

        #                    item_group.image.save("fasd", File(img))

        if key == "name":
            item_group.name = val
    item_group.date_created = timezone.now()
    item_group.date_modified = timezone.now()
    item_group.save()
