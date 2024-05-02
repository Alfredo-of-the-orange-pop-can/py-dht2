import gpiozero
import time

relay = gpiozero.OutputDevice(20, active_high=False, initial_value=False)
print(relay)

time.sleep(2.0)
relay.on()
print(relay)
time.sleep(2.0)
relay.off()
print(relay)
time.sleep(2.0)
relay.toggle()
print(relay)
