import pytest


def test_get_cat_image(cat_api):
    random_image_link = cat_api.get_image_link
    assert cat_api.validate_image(random_image_link).status_code == 200, "Image was not download"


@pytest.mark.parametrize("limit",(10, 15))
def test_get_cat_images_array(cat_api, limit):
    images = cat_api.get_image_array(limit)
    assert len(images) == limit, "There should be 10 images in array"


def test_get_breeds(cat_api):
    breeds = cat_api.get_breeds
    assert len(breeds) >= 1, "There should be at least one breed"

