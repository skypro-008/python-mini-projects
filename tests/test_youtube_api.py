import os
from unittest import mock

import pytest
from dotenv import load_dotenv
from googleapiclient.errors import HttpError
from src.youtube_api import *

load_dotenv()

API_KEY: str = os.getenv('YT_API_KEY')


# Tests for get_service() function
def test_can_create_service(mocker):
    mocker.patch('youtube_api.build')
    get_service()
    youtube_api.build.assert_called_once_with('youtube', 'v3', developerKey=API_KEY)


# Tests for get_channel_info() function
def test_can_get_channel_info(mocker):
    mock_channel_info = mock.MagicMock()
    mocker.patch('youtube_api.get_service', return_value=mock_channel_info)
    channel_info = get_channel_info('test_channel_id')
    assert channel_info == mock_channel_info


# Tests for get_channel_playlists() function
def test_can_get_channel_playlists(mocker):
    mock_playlists = mock.MagicMock()
    mocker.patch('youtube_api.get_service', return_value=mock_playlists)
    playlists = get_channel_playlists('test_channel_id')
    assert playlists == mock_playlists['items']


# Tests for get_playlist_videos() function
def test_can_get_playlist_videos(mocker):
    mock_video_ids = ['test_video_id1', 'test_video_id2']
    mock_playlist_videos = {'items': [{'contentDetails': {'videoId': 'test_video_id1'}},
                                      {'contentDetails': {'videoId': 'test_video_id2'}}]}
    mocker.patch('youtube_api.get_service', return_value=mock_playlist_videos)
    video_ids = get_playlist_videos('test_playlist_id')
    assert video_ids == mock_video_ids


# Tests for get_video_info() function
def test_can_get_video_info(mocker):
    mock_video_info = mock.MagicMock()
    mocker.patch('youtube_api.get_service', return_value=mock_video_info)
    video_info = get_video_info('test_video_id')
    assert video_info == mock_video_info


# Tests for get_video_stats() function
def test_can_get_video_stats(mocker):
    mock_video_info = {'items': [{'statistics': {'viewCount': '1000', 'likeCount': '50', 'commentCount': '10'}}]}
    mocker.patch('youtube_api.get_video_info', return_value=mock_video_info)
    video_stats = get_video_stats('test_video_id')
    assert video_stats == {'view_count': 1000, 'like_count': 50, 'comment_count': 10}


def test_raises_error_if_video_not_found(mocker):
    mocker.patch('youtube_api.get_video_info', side_effect=HttpError(mock.MagicMock(), b'404 not found'))
    with pytest.raises(Exception):
        get_video_stats('nonexistent_video_id')
