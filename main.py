while True:
    print("light level: " + input.light_level())
if input.light_level() > 5:
    light.set_all(light.rgb(0, 0, 0))
elif input.light_level() < 5:
    light.set_all(light.rgb(255, 255, 255))
else :
    print ("Circuit has ran into error")
#while True:
    #    print("Light level: " + input.light_level())
#    if input.light_level() < 4:
    #         light.set_all(light.rgb(0, 0, 255))
#    elif input.light_level() >= 12:
    #        light.clear()
#    else:
    #        input.light_level() >=4 <12
#        light.set_all(light.rgb(255, 255, 0))
