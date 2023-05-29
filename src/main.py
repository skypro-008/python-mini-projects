from utils import printj
from youtube_api import get_channel_info


def main() -> None:
    channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
    channel = get_channel_info(channel_id)
    printj(channel)


if __name__ == '__main__':
    main()
