#!/usr/bin/env python
import rospy
import json
from light_system.srv import *
from std_msgs.msg import String

"""
Road system :

 |   |   |5                         5|   |   |
 |       |                           |       |
5|   |   |                           |   |   |5
 |       |                           |       | 
 |   |   |5                         5|   |   |
 |       |                           |       |
5|   |	 |                           |   |   |5
 |	 |   1      2      3     4   |       |
 |   |   ----------------------------    |   |
5|    _  _  _  _  _  _  _  _  _   _   _      |5
 |                                           |
  -------------------------------------------
         1        2          3         4

5 :  Standard lights, when ambient light is low, lights are turned on
1-4 : Smart lights, which when the road is empty are turned on at a low voltage, producing a weak light and when detecting motion, it changes to full capacity.
The smarts lights are connected in parallel to the one which is in front. 
"""

class light_server:
    def __init__(self):
	rospy.init_node("light_server_state")
	rospy.Service("light_server", light_sys, self.callback)
	self.pub = rospy.Publisher('light_state', String, queue_size=10)
	self.rate = rospy.Rate(15) # 15hz
	self.light = {
	"light1" : 0,
	"light2" : 0,
	"light3" : 0,
	"light4" : 0,
	"light5" : 0 }
	#light5 is for all non smart lights.
	#light1 - 4 is for all smarts lights.

    def callback(self,req):
	light_id=req.lampa_id.data
	state_change=req.state.data
	response=light_sysResponse()

	if((light_id > 0 ) & (light_id < 6) & (state_change >= 0) & (state_change <= 2)):
		self.light["light%d"%(light_id)]=state_change
		response.res.data=True
		return response
	else:
		response.res.data=False
		return response
		
	
    def run(self):
	while not rospy.is_shutdown():
		json_msg=json.dumps(self.light)
		self.pub.publish(json_msg)
		self.rate.sleep()

if __name__ == '__main__':
    try:
	node=light_server()
	node.run()
    except rospy.ROSInterruptException:
	pass
