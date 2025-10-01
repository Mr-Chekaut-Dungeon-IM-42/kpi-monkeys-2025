from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    id: str
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)

    channels: list[Channel] = field(default_factory=list)
    playlists: list[Playlist] = field(default_factory=list)
    subscriptions: list[Subscription] = field(default_factory=list)
    comments: list[Comment] = field(default_factory=list)
    histories: list[History] = field(default_factory=list)


@dataclass
class Channel:
    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)
    user_id: str = field(default_factory=str)

    videos: list[Video] = field(default_factory=list)
    subscriptions: list[Subscription] = field(default_factory=list)

    @property
    def subscribers(self) -> int: ...  # type: ignore


@dataclass
class Video:
    id: str
    title: str
    description: str = ""
    uploaded_at: datetime = field(default_factory=datetime.now)

    channel_id: str = field(default_factory=str)

    comments: list[Comment] = field(default_factory=list)
    playlists: list[PlaylistVideo] = field(default_factory=list)
    histories: list[History] = field(default_factory=list)

    @property
    def views(self) -> int: ...  # type: ignore


@dataclass
class Comment:
    id: str
    comment_text: str
    commented_at: datetime = field(default_factory=datetime.now)

    user_id: str = field(default_factory=str)
    video_id: str = field(default_factory=str)


@dataclass
class Playlist:
    id: str
    name: str
    created_at: datetime = field(default_factory=datetime.now)

    user_id: str = field(default_factory=str)
    videos: list[PlaylistVideo] = field(default_factory=list)


@dataclass
class PlaylistVideo:
    playlist_id: str
    video_id: str


@dataclass
class Subscription:
    user_id: str
    channel_id: str


@dataclass
class History:
    id: str
    watched_at: datetime = field(default_factory=datetime.now)
    user_id: str | None = None
    video_id: str = field(default_factory=str)
