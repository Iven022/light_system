# light_system
This ros package is the simulation of a smart lightning system of a smart city. The diagram below shows the road system of the city.
<!--

 |   |   |L                         L|   |   |
 |       |                           |       |
L|   |   |                           |   |   |L
 |       |                           |       | 
 |   |   |L                         L|   |   |
 |       |                           |       |
L|   |	 |                           |   |   |L
 |	 | SL1    SL2    SL3     SL4 |       |
 |   |   ----------------------------    |   |
L|    _  _  _  _  _  _  _  _  _   _   _      |L
 |                                           |
  -------------------------------------------
      SL1      SL2          SL3       SL4

L :  Standard lights, when ambient light is low, lights are turned on
SL : Smart lights, which when the road is empty are turned on at a low voltage, producing a weak light and when detecting motion, it changes to full capacity.
The node will be publishing a json string of 5 lights states. 
Lights 1 - 4 will be the smart lights.
and Light 5 are the non smart one.
The smarts lights are connected in parallel to the one which is in front. 
states : 0 - off, 1 - on but low intensity, 2 - full capacity
-->
## To install this package and run its simulation

clone it into the src folder in your catkin workspace

```sh
cd ~/catkin_ws/src/light_system
./simulation.sh
```

