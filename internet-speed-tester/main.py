import speedtest

wifi=speedtest.Speedtest()
up=wifi.upload()/1048576
down=wifi.download()/1048576
print(f"Wifi Upload speed is {up},mbps")
print(f"Wifi Download speed is {down},mbps")
