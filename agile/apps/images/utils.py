import requests

from django.core.files.base import ContentFile

from agile.apps.images.models import Image, HashTag


'''
{'id': 'd3f812bc62be33098bb6',
 'author': 'Weekly Attack',
 'camera': 'Nikon D800E',
 'tags': '#photo ',
 'cropped_picture': 'http://interview.agileengine.com/pictures/cropped/kimorg-20000111-125136.jpg',
 'full_picture': 'http://interview.agileengine.com/pictures/full_size/kimorg-20000111-125136.jpg'}
}
'''


class ImageStorageHandler:
    url = 'http://interview.agileengine.com/images/'
    auth_url = 'http://interview.agileengine.com/auth'

    def get_auth_token(self):
        resp = requests.post(
            self.auth_url, json={"apiKey": "23567b218376f79d9415"}
        )
        if resp.status_code == requests.codes.ok:
            return resp.json()['token']
        # else:
        #     raise CustomException

    def update_image_cache(self):
        token = self.get_auth_token()
        headers = {"Authorization": f"Bearer {token}"}
        rsp = requests.get(self.url, headers=headers)
        page_count = rsp.json()['pageCount']

        for page in range(1, page_count):
            pictures = requests.get(self.url, headers=headers, params={"page": page}).json()["pictures"]
            for picture in pictures:
                pcid = picture["id"]
                if Image.objects.filter(pcid=pcid).exists():
                    continue
                response = requests.get(self.url+pcid, headers=headers)
                if response.status_code != requests.codes.ok:
                    continue

                image_data = response.json()
                print(image_data.keys())

                img = Image(
                    pcid=pcid,
                    author=image_data.get('author', None),
                    camera=image_data.get('camera', None),
                )
                tags = self.get_tags(image_data['tags'])

                file_name, file = self.get_picture(image_data['full_picture'])

                img.picture.save(file_name, file)
                img.hashtags.add(*tags)
                img.size = str(img.picture.size)
                img.name = file_name
                img.save()

    def get_picture(self, pic_url):
        file_name = pic_url.split("/")[-1]
        response = requests.get(pic_url)
        file = ContentFile(response.content)

        return file_name, file

    def get_tags(self, data):
        tag_names = [t.strip() for t in data.split('#') if bool(t)]
        tag_list = []
        for name in tag_names:
            tag_obj, created = HashTag.objects.get_or_create(tag_name=name)
            tag_list.append(tag_obj)

        return tag_list
