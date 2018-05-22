# In The Name Of God
# ========================================
# [] File Name : example.py
#
# [] Creation Date : 22-05-2018
#
# [] Created By : Parham Alvani <parham.alvani@gmail.com>
# =======================================

from tb.app import ThingsBoardApp


t = ThingsBoardApp('DHT11_DEMO_TOKEN', '127.0.0.1')
t.run()
t.log({'temperature': 10})

while True:
    pass
