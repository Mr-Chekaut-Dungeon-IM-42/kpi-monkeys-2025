from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: str
    username: str
    email: str
    created_at: datetime

    channels: list[Channel]
    playlists: list[Playlist]
    subscriptions: list[Channel]
    comments: list[Comment]
    histories: list[History]


@dataclass
class Channel:
    id: str
    name: str
    created_at: datetime
    owner: User

    videos: list[Video]
    subscribers: list[User]

    @property
    def sub_count(self) -> int: ...  # type: ignore


@dataclass
class Video:
    id: str
    title: str
    description: str
    uploaded_at: datetime

    channel: Channel

    comments: list[Comment]
    playlists: list[Playlist]
    histories: list[History]

    @property
    def views(self) -> int: ...  # type: ignore


@dataclass
class Comment:
    id: str
    comment_text: str
    commented_at: datetime

    user_id: User
    video_id: Video


@dataclass
class Playlist:
    id: str
    name: str
    created_at: datetime

    owner: User
    videos: list[Video]


@dataclass
class History:
    id: str
    watched_at: datetime
    video: Video
    user: User | None
