essentially# AIDE - Summer Research Report #1
This is a report on our progress so far on integrating the AIDE tool and its components.

## AIDE
What AIDE tool is supposed to do (input and output)
After much discussion with Fletcher and Ethan, we came to a conclusion of having our AIDE tool be an outside controller, separate from the individual parts of AIDE. This AIDE tool will essentially be in charge of running the whole AIDE program and running the background modules, calling each separate parts of the design tool, including GUI, Design, Draw, and Document.


Add the chart (updated pls)


briefly describe what each subteam does?
Template:
GUI: Gets input values from the user and displays the interface on Fusion 360, and compress the collected inputs into a YAML form that is easily used by design functions
Design: Takes YAML from GUI and calculates
Draw:
Document:

## AIDE GUI

When AIDE is run, it also initializes and runs a Fusion 360 add-in in the form of AIDE GUI (Graphical User Interface). This GUI allows the user to input values (such as desired flow rate) that affect the dimensions of the finished water treatment plant.

### Progress
#### File reorganization
We started out by restructuring the files in the top-most directory to contain our:
1. Code to run the Fusion 360 add-in (`aide_gui.py` and `helper.py`)
2. A `data` folder containing the files necessary for displaying the GUI
3. A `dependencies` folders containing the Python packages for displaying the GUI and processing user inputs

Within `data`, we placed our HTML templates, YAML's, and images which are used to display the GUI.

## AIDE TEMPLATE

Template utilizes Fusion 360, a CAD software, to create 3D models of the water treatment plant. Fusion is the ideal software for template because it allows components to be parameterized with equations and numbers. Parameters are "user-defined values used to control any reference geometry."

For better understanding template, let's think of template as a burger. Usually when you order a burger, you get a patty, slice of cheese, lettuce, and tomato. The number of each part of the burger can be parametrized as seen below.

 Now if you wanted to order a double-double, you would input number of patties to equal 2. Fusion 360 will take this input and update the parameters for cheese, lettuce and tomato.

Number of patties = 2

Number of buns = 2

Number of cheese slices = Number of patties

Number of lettuce slices = Number of patties

Number of tomato slices = Number of patties



The goal for the summer is to finish the 3D models of all the components and test the assemblies to make sure all the components are linked properly. As parameter value changes, the geometry of assemblies should change accordingly without interfering with other assemblies. Furthermore, we are trying to find the best naming convention for Template to use in order to have consistent parameter names throughout AIDE and prevent misunderstanding between subteams.
