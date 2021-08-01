#!/bin/bash

dir=$(pwd)
cd ..
cd ..
dir=$(pwd)
catkin build
source $dir/devel/setup.bash

gnome-terminal --tab --title="tab 1" --command="bash -c 'roslaunch light_system light_s.launch; $SHELL'" >> log.txt #Executing the server node from another terminal tab

sleep 10s #waiting for the ROS server to initialize

#night simulation
#data: 5 is for all lamps which isnt connected to the radar
#states : 0 - off, 1 - on but low intensity, 2 - full capacity
rosservice call /light_server "lampa_id:
  data: 1
state:
  data: 1"

rosservice call /light_server "lampa_id:
  data: 2
state:
  data: 1"

rosservice call /light_server "lampa_id:
  data: 3
state:
  data: 1" 

rosservice call /light_server "lampa_id:
  data: 4
state:
  data: 1"

rosservice call /light_server "lampa_id:
  data: 5
state:
  data: 1" 

sleep 4s
rosservice call /light_server "lampa_id:
  data: 4
state:
  data: 2"

sleep 0.5s
rosservice call /light_server "lampa_id:
  data: 3
state:
  data: 2"

sleep 0.5s
rosservice call /light_server "lampa_id:
  data: 2
state:
  data: 2"

rosservice call /light_server "lampa_id:
  data: 4
state:
  data: 1"

sleep 0.5s
rosservice call /light_server "lampa_id:
  data: 1
state:
  data: 2"

rosservice call /light_server "lampa_id:
  data: 3
state:
  data: 1"

sleep 0.5s
rosservice call /light_server "lampa_id:
  data: 2
state:
  data: 1"

sleep 0.5s
rosservice call /light_server "lampa_id:
  data: 1
state:
  data: 1"



