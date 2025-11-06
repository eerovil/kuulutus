import pychromecast
import dotenv

dotenv.load_dotenv()

name = dotenv.get_key(dotenv.find_dotenv(), "MAIN_CHROMECAST_NAME")
base_url = dotenv.get_key(dotenv.find_dotenv(), "BASE_URL")

# Discover and connect to chromecasts named Kitchen display
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[name])

cast = chromecasts[0]
cast.wait()

mc = cast.media_controller
mc.play_media(f"{base_url}/test.mp3", "audio/mp3")
mc.block_until_active()
