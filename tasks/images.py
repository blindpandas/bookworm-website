# coding: utf-8

import shutil
from pathlib import Path
from itertools import chain
from invoke import task
from PIL import Image
from PIL.ImageColor import getrgb


COLOR_BLACK = tuple(range(0, 50))
COLOR_WHITE = tuple(range(155, 255))
IMAGES_SRC= Path.cwd() / 'images'
IMAGES_DST = Path.cwd() / "content" / "static" / "images"
IMAGE_SIZES = (
    ("", "ico", 32),
    ("16x16", "png", 16),
    ("32x32", "png", 32),
    ("64x64", "png", 64),
    ("128x128", "png", 128),
    ("180x180", "png", 180),
    ("256x256", "png", 256),
    ("320x320", "png", 320),
    ("512x512", "png", 512),
)
LOGOS_SRC= IMAGES_SRC / 'branding_src'
LOGOS_DST = IMAGES_SRC / 'logos'
LOGOS_COLORS = {
    'blindpandas': ('#325d88', '#AEA79F'),
    'bookworm': ('#77216F', '#AEA79F'),
}
FOLDERS_TO_COPY_FROM = {
    LOGOS_DST.name,
    "authors",
}
IMAGE_GLOBS = {"*.png", "*jpg",}


def recolor_image(image, old_color_range, color):
    new_color = getrgb(color)
    img = image.convert('RGBA')
    data = img.getdata()
    new_data = []
    for item in data:
        if (item[-1] != 0) and (item[0] in old_color_range):
            new_data.append(new_color)
        else:
            new_data.append(item)
    img.putdata(new_data)
    return img



@task
def logos(c):
    LOGOS_DST.mkdir(parents=True, exist_ok=True)
    for logo in LOGOS_SRC.glob("*.png"):
        logo_name = logo.stem
        if logo_name not in LOGOS_COLORS:
            raise ValueError(f"Unknown logo image: '{logo_name}'")
        black, white = LOGOS_COLORS[logo_name]
        print(f"Recoloring logo: {logo.name}")
        print(f"Replacing white with '{white}' and black with '{black}'")
        img = recolor_image(Image.open(logo), COLOR_BLACK, black)
        recolor_image(img, COLOR_WHITE, white)
        img.save(LOGOS_DST / logo.name )
        print(f"Saved recolored logo: {logo}")

@task
def resize(c):
    print("Saving images with different sizes")
    IMAGES_DST.mkdir(parents=True, exist_ok=True)
    images_to_process = chain.from_iterable(
        IMAGES_SRC.joinpath(folder).rglob(glb)
        for folder in FOLDERS_TO_COPY_FROM
        for glb in IMAGE_GLOBS
    )
    for imgfile in images_to_process:
        img = Image.open(imgfile)
        dst_path = IMAGES_DST.joinpath(
            imgfile.relative_to(IMAGES_SRC)
        )
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        for suffix, ext, size in IMAGE_SIZES:
            filename = dst_path.with_name(f"{imgfile.stem}{suffix}.{ext}")
            img.resize((size, size)).save(str(filename))
            print(f"Saved image '{imgfile.stem}' with size: {size}x{size}")
    print("Images task finished.")


@task(default=True, pre=(logos, resize,))
def default(c):
    """Recolors the logos and resizes all the images."""