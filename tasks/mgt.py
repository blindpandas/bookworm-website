# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from pathlib import Path
from packaging.version import parse as parse_version
from invoke import task
from invoke.util import cd
from more_itertools import first_true
from github import Github
from yaml import dump

ROOT = Path.cwd()
RELEASE_INFO_FILENAME = ROOT / "release_info.yaml"
REPO_NAME = "blindpandas/bookworm"
USER_GUIDE_SRC  = ROOT / "bookworm" / "bookworm" / "resources" / "userguide"
USER_GUIDE_DST = ROOT / "content" / "pages" / "user-guide"
USER_GUIDE_SLUG = 'user-guide'
USER_GUIDE_TEMPLATE = "userguide"

@task(name="release")
def update_release_info(c):
    """Pulls release information from GitHub and updates the release file."""
    print("Retrieving release information from GitHub...")
    github = Github(
        login_or_token=c['github']['github-api-token'],
        user_agent=c['github']['username']
    )
    repo = github.get_repo(REPO_NAME)
    releases = repo.get_releases()
    info = {}
    for rel in releases:
        if ("dev" in info) and ("stable" in info ):
            break
        if not (release_info := get_release_info(c, rel)):
            continue
        if rel.prerelease:
            if "dev" not in info:
                info["dev"] = release_info
                print(f"Found latest development release: {release_info['title']}")
        else:
            if "stable" not in info:
                info["stable"] = release_info
                print(f"Found latest stable release: {release_info['title']}")
    if ("dev" in info) and ("stable" in info ):
        dev_version = parse_version(info['dev']['version'])
        stable_version = parse_version(info['stable']['version'])
        if dev_version < stable_version:
            info.pop("dev")
    RELEASE_INFO_FILENAME.write_text(dump(info))
    print("Release information updated successfully!")


def get_release_info(c, release):
    info = dict(
        title=release.title,
        tag=release.tag_name,
        published="" if release.published_at is None else release.published_at.isoformat(),
        url=release.html_url
    )
    assets = {
        asset.name: asset
        for asset in release.get_assets()
    }
    files = info.setdefault('files', [])
    for asset in assets.values():
        files.append(dict(
            filename=asset.name,
            size=asset.size,
            download_url=asset.browser_download_url
        ))
    if not info['files']:
        return {}
    release_info_asset = assets['release-info.json']
    release_info_url = "https://{token}:@api.github.com/repos/{repo}/releases/assets/{asset_id}".format(
        token=c['github']['github-api-token'],
        repo=REPO_NAME,
        asset_id=release_info_asset.id
    )
    release_metadata = requests.get(release_info_url, headers={'Accept': 'application/octet-stream'}).json()
    info['version'] = release_metadata.pop('version')
    info['metadata'] = release_metadata
    return info


@task(name='userguide')
def make_user_guide(c):
    USER_GUIDE_DST.mkdir(parents=True, exist_ok=True)
    langs = set(
        item.name
        for item in USER_GUIDE_SRC.iterdir()
        if item.is_dir()
    )
    for lang in langs:
        translation = 'true' if lang != 'en' else 'false'
        md_content = (USER_GUIDE_SRC / lang / "bookworm.md"  ).read_text()
        localized_title = md_content.strip().splitlines()[0].replace("#", "")
        outfile = USER_GUIDE_DST / f"user-guide-{lang}.md"
        file_content = (
            f"title: {localized_title}\n"
            f"slug: {USER_GUIDE_SLUG}\n"
            f"modified: {datetime.utcnow().isoformat()}\n"
            f"lang: {lang}\n"
            f"translation: {translation}\n"
            f"template: {USER_GUIDE_TEMPLATE}\n"
            f"{ '-' * 15}\n\n"
        )
        file_content += md_content
        outfile.write_text(file_content)
