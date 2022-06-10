'''
app module contains the definition of ThingsBoard Application
which is used for communication with ThingsBoard.
'''

import asyncio
import json
import threading

import paho.mqtt.client as mqtt


class ThingsBoardApp:
    def __init__(self, access_token: str, tb_ip: str, tb_port: int = 1883):
        # MQTT Up and Running
        self.client = mqtt.Client()
        self.client.username_pw_set(access_token)
        self.client.connect(tb_ip, tb_port)
        self.client.on_connect = self._on_connect

        # Event loop
        self.loop = asyncio.new_event_loop()

    def run(self):
        t = threading.Thread(target=self._run)
        t.daemon = True
        t.start()

    def log(self, states):
        self.client.publish('v1/devices/me/telemetry', json.dumps(states))

    def _run(self):
        asyncio.set_event_loop(self.loop)
        self._mqtt_loop()
        try:
            self.loop.run_forever()
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            self.loop.close()

    def _mqtt_loop(self):
        self.client.loop()
        self.loop.call_soon(self._mqtt_loop)

    def _on_connect(self, client, userdata, flags, rc):
        print("Connected to ThingsBoard")
