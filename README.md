# Manny the Manufacturer

## Project Summary

Our project is a simulation of the multi-axis arm manipulators used in manufacturing for automation. Our implementation of the arm is meant to move our 3D printed boxes from the start zone, to a middle zone meant to represent another machine performing a task on the box, and then finally to the finished zone. Our concept came from Katie and Pallas's experiences working at Acutec. Although there isn't a manufacturing process actually happening, this project simulates an external form of automation. Utilizing an external arm that is separate from the machine allows for a more customizable and flexible process which allows for a generalized automation approach that is far less expensive and allows for small businesses and small scale manufacturing to make use of automated processes.

## Project Implementation Details

1. Plug in evo arm #302

2\. Navigate to [evodyne](https://evoarm.evodyne.co/)

3\. Enter the ID of `627892372`

4\. Use access code `evodyne2020`

5\. Click the IP address to connect to the robot

6\. Go to the `Apps` tab

7\. Before running the application, line the robot up on the cardboard

8\. Place all 4 cubes on the right 4 squares

9\. Run `manny.py` app

## Experimental Results

- going from one side to another

This task began with creating a working inverse kinematics script to convert an XYZ coordinate set to the appropriate angles for the servos. We ended up abandoning this script in favor of the evoarms built in systems. Utilizing the sequence command structure we were able to get the arm, with a healthy dose of trial and error, to move from the start side, to the middle "machine", and finally to the finished side.

- picking up the cubes

Picking up the cubes was the second part to the system, being able to pick up the cube and combine that with the previous moving step, we are able to transport the cube from one station to the next, with the exception of putting it down.

- putting down the cube in the correct spot

The last task was getting the robot to put the cube down in the correct spot, this required a bit more finesse than simply opening the jaws. Rotation of the wrist, vertical distance from the floor, and even the angle of the block in the jaws all determine the final resting place of the block. Unfortunately, the orientation of the block is largely out of our control.

## Ethical Implications

1. Who would typically make the technology of the similar type as your project? Why?

Our robot simulates a process very similar to automated manufacturing. Robotic arms and manipulators like our project are used by large manufacturing companies to speed up the process and make it more consistent overall.

2. Who are the intended users of this robotic application? How does this technology benefit them?

This is intended for use by manufacturing companies, or really anyone doing a repeatable task. This technology can free up time to do other tasks that are not mindless repeated tasks.

3. Who is not supposed to use this technology? Why?

Fish, they would probably get the boards wet and cause a short circuit. Although access to this type of technology should be widely available, there are legitimate concerns about the manufacturing of dangerous things such as weapons or explosives. Lowering the cost and increasing the availability of products is great, however that can unintentionally increase the availability of dangerous goods.

4. How can the type of robotic application implemented in your project cause harm?

One argument that people use against having automated robots in manufacturing is that the robots take people's jobs or that people are getting replaced by robots in manufacturing. Another possible harm is the environmental impact of manufacturing process.

5. What solutions can be developed to avoid the harm caused by this type of technology or to fix the harm?

Manufacturing businesses using robotics are often still desperate for people to hire. Additionally, robotics creates more high paying jobs because people have to run the robots too. The environmental impact of the manufacturing field could be counteracted with being more environmental conscious and creating programs to counteract the emissions put out by the plants.
