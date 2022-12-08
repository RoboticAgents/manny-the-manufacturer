# Report by Katie Burgess, Pallas Cain, Danny Ullrich

## Project Summary

Describe the completed project. Provide motivation for your project, application
that your robot is utilized for, specific goals/tasks it completes, and include
any background references you used to develop the idea for your project
(links are okay).

Our project is a simulation of the multi-axis arm manipulators used in
manufacturing for automation. Our implementation of the arm is meant to move
our 3D printed boxes from the start zone, to a middle zone meant to represent
another machine performing a task on the box, and then finally to the finished
zone. Our concept came from Katie and Pallas's experiences working at Acutec.
Although there isn't a manufacturing process actually happening, this project
simulates an external form of automation. Utilizing an external arm that is
separate from the machine allows for a more customizable and flexible process
which allows for a generalized automation approach that is far less expensive
and allows for small businesses and small scale manufacturing to make use of
automated processes.

## Project Implementation Details

First, outline all steps one must take to run your project, including any needed
installations. Then describe **all** steps you took to implement the task,
including all non-technical and technical details. Please include references
(links are okay) to all resources you have used.

1. Plug in evo arm #302 2. Navigate to [evodyne](https://evoarm.evodyne.co/) 3.
Enter the ID of `627892372` 4. Use access code `evodyne2020` 5. Click the IP
address to connect to the robot 6. Go to the `Apps` tab 7. Before running the
application, line the robot up on the cardboard 8. Place all 4 cubes on the
right 4 squares 9. Run `manny.py` app

## Experimental Results

Conduct at least three experiments with your completed implementation, where
something is varied in each experiment (for example changes in the
environment). Produce visual representation of these experiments (pictures or
videos). Describe your observations of the outcome of these experiments(how did
the robot behave in these experiments? were there variations?).

### 1. going from one side to another

This task began with creating a working inverse kinematics script to convert an
XYZ coordinate set to the appropriate angles for the servos. We ended up
abandoning this script in favor of the evoarms built in systems. Utilizing the
sequence command structure we were able to get the arm, with a healthy dose of
trial and error, to move from the start side, to the middle "machine", and
finally to the finished side.

### 2. picking up the cubes

Picking up the cubes was the second part to the system, being able to pick up
the cube and combine that with the previous moving step, we are able to
transport the cube from one station to the next, with the exception of putting
it down.

### 3. putting down the cube in the correct spot

The last task was getting the robot to put the cube down in the correct spot,
this required a bit more finesse than simply opening the jaws. Rotation of the
wrist, vertical distance from the floor, and even the angle of the block in the
jaws all determine the final resting place of the block. Unfortunately, the
orientation of the block is largely out of our control.

## Ethical Implications

Based on your experiences with the project and from our discussions in class,
please provide answers for the following questions as related to the project
you chose to implement:

1. Who would typically make the technology of the similar type as your project?
Why?

Our robot simulates a process very similar to automated manufacturing. Robotic
arms and manipulators like our project are used by large manufacturing
companies to speed up the process and make it more consistent overall.

1. Who are the intended users of this robotic application? How does this
technology benefit them?

This is intended for use by manufacturing companies, or really anyone doing a
repeatable task. This technology can free up time to do other tasks that are
not mindless repeated tasks.

1. Who is not supposed to use this technology? Why?

Fish, they would probably get the boards wet and cause a short circuit. Although
access to this type of technology should be widely available, there are
legitimate concerns about the manufacturing of dangerous things such as weapons
or explosives. Lowering the cost and increasing the availability of products is
great, however that can unintentionally increase the availability of dangerous
goods.

1. How can the type of robotic application implemented in your project cause
harm?

One argument that people use against having automated robots in manufacturing is
that the robots take people's jobs or that people are getting replaced by
robots in manufacturing. Another possible harm is the environmental impact of
manufacturing process.

1. What solutions can be developed to avoid the harm caused by this type of
technology or to fix the harm?

Manufacturing businesses using robotics are often still desperate for people to
hire. Additionally, robotics creates more high paying jobs because people have
to run the robots too. The environmental impact of the manufacturing field
could be counteracted with being more environmental conscious and creating
programs to counteract the emissions put out by the plants.

## Team Working Strategy

Our team work strategy was to have at least two people testing at the same
time while one person worked on the report. Katie worked a lot with coding the
robots movements. Danny and Pallas helped to make the resin cubes. Pallas and
Katie designed the board for the robot to sit on. We all worked on the hardware
of the arm trying to fix the first robot. We all were also a part of the
testing process discussing what changes needed to be made and putting the
blocks back in order. Additionally, we all worked on the report.

## Challenges and Learning Experiences

The biggest challenge we faced during this assignment was finding a working arm.
The first arm we started with was put on backwards and the motor was not
working as well as we wanted so we had to switch robots. This meant we had to
rewrite our code for the new robot. It was very frustrating but we overcame
this with a lot of patience. One of the biggest learning takeaways was that we
spent a lot of time considering the design of the robot and how it would
interact with the environment. We learned the arm could only stretch so far and
only rotate so many degrees. This meant we had to work within the confines of
the arm's capabilities. Another learning takeaway was how much testing is
involved with robotics. This project definitely took the most testing of all
the projects we did this past semester. Every small edit in the positioning
needed to be tested to make sure the arm could still pick up the blocks. All
this testing took a lot of patience and critical thinking.
