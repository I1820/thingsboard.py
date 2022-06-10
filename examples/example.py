from tb.app import ThingsBoardApp

t = ThingsBoardApp('DHT11_DEMO_TOKEN', '127.0.0.1')
t.run()
t.log({'temperature': 10})

while True:
    pass
