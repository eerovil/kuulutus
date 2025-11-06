import pychromecast
import dotenv
import argparse


parser = argparse.ArgumentParser(description="Play audio on Chromecast device.")

# Positional arg, text to play
parser.add_argument("text", type=str, help="Text to play on Chromecast")

args = parser.parse_args()


dotenv.load_dotenv()

name = dotenv.get_key(dotenv.find_dotenv(), "MAIN_CHROMECAST_NAME")
base_url = dotenv.get_key(dotenv.find_dotenv(), "BASE_URL")

# Discover and connect to chromecasts named Kitchen display
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[name])

cast = chromecasts[0]
cast.wait()

# Replace spaces with _ and lowercase the text to form the filename
filename = args.text.replace(" ", "_").lower() + ".mp3"

print(f"Playing {filename} on {name} Chromecast")

mc = cast.media_controller
mc.play_media(f"{base_url}/{filename}", "audio/mp3")
mc.block_until_active()
