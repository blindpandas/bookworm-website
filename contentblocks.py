# coding: utf-8


import yaml
from dataclasses import dataclass
from pathlib import Path


CONTENT_INFO_FILE = Path(__file__).parent / "content_info.yaml"

with open(CONTENT_INFO_FILE, "r", encoding="utf-8") as file:
    CONTENT_INFO = yaml.safe_load(file)

# Site metadata
HERO_TITLE = "Bookworm"
HERO_LEAD = "The universally accessible document reader"

# Twitter embed
TWITTER_USER = 'blindpandas'
TWITTER_EMBED_TITLE = "Tweets by Blind Pandas Team"
TWITTER_EMBED_WIDTH = 500
TWITTER_EMBED_HEIGHT= 500
