from controller import Robot,Keyboard,Motion

timestep= 32
robot= Robot()

keyboard= Keyboard()
keyboard.enable(timestep)

wave = Motion('../../motions/wave.motion')

while robot.step(timestep) != -1:
    
    key = keyboard.getKey()
    
    if key == Keyboard.UP:
        wave.play() 