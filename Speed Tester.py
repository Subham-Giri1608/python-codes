#generating a speed tester using python

import speedtest as speedtest 

test = speedtest.Speedtest()
up_speed = test.upload()
down_speed = test.download()

print("The Uplaod Speed:", up_speed)
print("The Download Speed:", down_speed)