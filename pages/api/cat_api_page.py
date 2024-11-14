from pages.api.base_api_page import BaseAPIPage


class CatAPIPage(BaseAPIPage):
    GET_IMAGE_LINK_ENDPOINT = 'v1/images/search'
    GET_IMAGE_ARRAY_LINK_ENDPOINT = 'v1/images/search?limit={}'
    GET_BREEDS_LINK_ENDPOINT = 'v1/breeds'

    def __init__(self, base_url, headers=None):
        super().__init__(headers)
        self.base_url = base_url

    @property
    def get_image_link(self):
        response = self.get(f"{self.base_url}{self.GET_IMAGE_LINK_ENDPOINT}").json()
        return response[0]['url']

    @property
    def get_breeds(self):
        response = self.get(f"{self.base_url}{self.GET_BREEDS_LINK_ENDPOINT}").json()
        return response

    def get_image_array(self, limit):
        response = self.get(f"{self.base_url}{self.GET_IMAGE_ARRAY_LINK_ENDPOINT.format(limit)}").json()
        return response

    def validate_image(self, image_link):
        resp = self.get(image_link)
        return resp
