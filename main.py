import time
import vgamepad as vg

g = vg.VX360Gamepad()

start = time.time()
while time.time() - start < 50:
    g.left_joystick(x_value=0, y_value=32767)
    g.update()

g.left_joystick(x_value=0, y_value=0)
g.update()
