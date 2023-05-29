import os

from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

API_KEY: str = os.getenv('YT_API_KEY')


def get_service() -> build:
    """Создать специальный объект для работы с youtube API."""
    service = build('youtube', 'v3', developerKey=API_KEY)
    return service


def get_channel_info(channel_id: str) -> dict[str, dict[str, str]]:
    """Получить информацию о канале по его идентификатору."""
    channel_info = get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
    return channel_info


def get_channel_playlists(channel_id: str, max_results: int = 50) -> list[dict[str, str]]:
    """Получить данные по play-листам канала."""
    playlists = get_service().playlists().list(channelId=channel_id,
                                               part='contentDetails,snippet',
                                               maxResults=max_results,
                                               ).execute()
    return playlists['items']


def get_playlist_videos(playlist_id: str, max_results: int = 50) -> list[str]:
    """Получить данные по видеороликам в плейлисте."""
    playlist_videos = get_service().playlistItems().list(playlistId=playlist_id,
                                                         part='contentDetails',
                                                         maxResults=max_results,
                                                         ).execute()
    video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]

    return video_ids


def get_video_info(video_id: str) -> dict[str, dict[str, str]]:
    """Получить статистику видео по его id."""
    video_info = get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                             id=video_id
                                             ).execute()
    return video_info


def get_video_stats(video_id: str) -> dict[str, int]:
    """Получить количество просмотров, лайков и комментариев для видео по его идентификатору."""
    video_info = get_video_info(video_id)
    video_stats = {
        'view_count': int(video_info['items'][0]['statistics']['viewCount']),
        'like_count': int(video_info['items'][0]['statistics']['likeCount']),
        'comment_count': int(video_info['items'][0]['statistics']['commentCount'])
    }
    return video_stats
