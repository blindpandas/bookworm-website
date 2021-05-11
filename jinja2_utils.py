# coding: utf-8

from pathlib import Path, PurePosixPath
from urllib.parse import urljoin
from jinja2.filters import contextfilter
from PIL import Image


@contextfilter
def resize_image(context, image_path, requested_size):
    site_url = context["SITEURL"]
    image_filename = Path(
        context["PATH"],
        image_path.rstrip(site_url)
    )
    resized_image_filename =         "{}-{}{}".format(
        image_filename.stem,
        "x".join(requested_size),
        image_filename.suffix
    )
    target_filename = image_filename.parent.joinpath(resized_image_filename)
    if not target_filename.exists():
        Image.open(image_filename).resize(requested_size).save(target_filename)
    uri_parts = list(Path(image_path.rstrip(site_url)).parts)
    uri_parts[-1] = resized_image_filename
    return urljoin(
        site_url,
        "/".join(uri_parts)
    )


@contextfilter
def make_absolute_url(context, value):
    if "://" in value:
        return value
    return urljoin(context['SITEURL'], value)
