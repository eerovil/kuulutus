import time
import pychromecast
import zeroconf

# Create a browser which prints the friendly name of found chromecast devices
zconf = zeroconf.Zeroconf()
browser = pychromecast.CastBrowser(pychromecast.SimpleCastListener(lambda uuid, service: print(browser.devices[uuid].friendly_name)), zconf)
browser.start_discovery()
# Shut down discovery
pychromecast.discovery.stop_discovery(browser)

name = "Kitchen display"

# Discover and connect to chromecasts named Living Room
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[name])
[cc.cast_info.friendly_name for cc in chromecasts]

cast = chromecasts[0]
cast.wait()

mc = cast.media_controller
mc.play_media("test.mp3", "audio/mp3")
mc.block_until_active()
