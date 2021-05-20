# coding: utf-8

from pathlib import Path, PurePosixPath
from datetime import datetime
from operator import itemgetter
from urllib.parse import urljoin
from babel import Locale as BabelLocale
from babel.dates import format_date
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


def user_downloadable_files(filelist):
    """Filters the list of release files to only needed ones."""
    acceptable_suffixes = {'.zip', '.exe'}
    rv = [
        file for file in filelist
        if Path(file['filename']).suffix.lower() in acceptable_suffixes
    ]
    rv.sort(key=itemgetter('filename'))
    return rv


@contextfilter
def lang_display_name(c, lang_code):
    return BabelLocale.parse(lang_code).display_name

def is_rtl(lang_code):
    return BabelLocale.parse(lang_code).text_direction == 'rtl'


def formatdatetime(datestring):
    dt = datetime.fromisoformat(datestring)
    return format_date(dt, locale="en")
    