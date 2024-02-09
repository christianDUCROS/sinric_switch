import network
import mip
ssid= "xxxxxxx"
password= "xxxxxxxxx"

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

try:
    connect()
    mip.install("github:sinricpro/micropython-sinricpro-sdk")
except KeyboardInterrupt:
    machine.reset()






