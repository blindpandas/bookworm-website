# -*- coding: utf-8 -*-

from pathlib import Path
from invoke import task
from invoke.util import cd
from github import Github
from yaml import dump

RELEASE_INFO_FILENAME = Path.cwd() / "release_info.yaml"
REPO_NAME = "blindpandas/bookworm"


@task(name="release-info")
def update_release_info(c):
    """Pulls release information from GitHub and updates the release file."""
    print("Retrieving release information from GitHub...")
    github = Github()
    repo = github.get_repo(REPO_NAME)
    releases = repo.get_releases()
    info = {}
    for rel in releases:
        if ("dev" in info) and ("stable" in info ):
            break
        if not (release_info := get_release_info(rel)):
            continue
        if rel.prerelease:
            if "dev" not in info:
                info["dev"] = release_info
                print(f"Found latest development release: {release_info['title']}")
        else:
            if "stable" not in info:
                info["stable"] = release_info
                print(f"Found latest stable release: {release_info['title']}")
    RELEASE_INFO_FILENAME.write_text(dump(info))
    print("Release information updated successfully!")


def get_release_info(release):
    info = dict(
        title=release.title,
        tag=release.tag_name,
        published=release.published_at.isoformat(),
        url=release.html_url
    )
    files = info.setdefault('files', [])
    for asset in release.get_assets():
        files.append(dict(
            filename=asset.name,
            size=asset.size,
            download_url=asset.browser_download_url
        ))
    return info if info['files'] else {}
