import sys
import robot

if len(sys.argv) > 2: #take in the serial port name and filename from the args
    PORT = sys.argv[1]
    file = open(sys.argv[2], "r")
else:
    print("Please specify a port and a file to run.")
    raise SystemExit

bot = robot.Robot(PORT, -15, -22, False, 0.09) #settings for T3

lines = file.readlines()
for line in lines:
    bot.send(line)