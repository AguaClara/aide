# AIDE - Summer Research Report #1
This is a report on our progress so far on integrating the AIDE tool and its components.

## AIDE
AIDE is a Fusion 360 add-in that takes in user parameters for flow rate and temperature and produces the hydraulic design and building documentation for a water treatment plant. It utilizes/runs all five of its modules sequentially, while maintaining separation such that each module can be used to some degree on its own.

### How AIDE works
1. **Template**: Contains scalable 3D models of water treatment plants and their respective building documentation, maintained by the aide_template team.
2. **GUI** (Graphical User Interface): Displays a user interface in Fusion 360, collects the required input values from the user, and compiles them into a YAML file.
3. **Design**: Runs calculations to form all of the physical parameters of a water treatment plant, based off of the inputs collected by the GUI.
4. **Draw**: Updates and scales 3D models of water treatment plants, based off of the calculated physical parameters from Design.
5. **Document**: Updates and scales building documentation of water treatment plants, based off of the calculated physical parameters from Design.

Here is a chart detailing the flow of information throughout each module:
![](info_flow_modules.jpg)

Here is a chart detailing the flow of information relative to each file:
![](info_flow_files.jpg)

For an explanation of some of the terms that are used above, see our [ReadMe](https://github.com/AguaClara/aide/blob/master/README.md).

### Progress
#### Module organization
After much discussion, we came to a conclusion of having our AIDE module be the overall controller, separate from the individual submodules of AIDE. This AIDE module will essentially be in charge of running the whole AIDE program and running GUI, Design, Draw, and Document sequentially.

---

In this report, quoted lines give a more detailed description of how the components work in the background.
> Skip over them if you only want to read a high-level explanation of the modules.

## AIDE GUI
When AIDE is run, it also initializes and runs another Fusion 360 add-in, AIDE GUI (Graphical User Interface). This GUI allows the user to input values (such as desired flow rate) that affect the dimensions of the finished water treatment plant.

### How AIDE GUI works
In order to use a custom-made Fusion 360 add-in, you must move the folder containing all of your necessary files to a specified location on your hard drive.
> For each operating system, this location is:

>Windows – C:\Users\%username%\AppData\Autodesk\Autodesk Fusion 360\API\AddIns

>Mac – $HOME/Library/Application Support/Autodesk/Autodesk Fusion 360/API/AddIns

> For development, we make a symbolic link (like a web link, but between files and folders) from the Git repository to this specified location. The folders are usually hidden, so you must unhide them in order to access them.

You then open Fusion 360 > Scripts & Add-Ins > Add-Ins > aide_gui > Run. The palette window then opens on the right.

> Fusion uses `aide_gui.py` to begin running the palette. At the top are imports for all of the packages that are used and global variables that are referenced when the add-in is run.

> The `run(context)` function is then run. After loading global variables and helper functions, the `showPalette` command is defined. This command will be responsible for showing the palette. Normally, this would display a button under one of Fusion's dropdown menus, but we've omitted that functionality. Instead of manually showing the palette with a button, it opens and closes when the add-in is run or stopped.

> The `showPalette` command is then connected to an instance of the `ShowPaletteCommandCreatedHandler` class. Instances of this class, and of all other handler classes within `aide_gui.py`, become "event handlers", similar to event listeners in Java. They "listen" for events being triggered by Fusion 360 - when that happens, they run the `notify(self, args)` function from their respective class.

> This handler is then added to the global `handlers` list so that Fusion can begin listening for the event, and then it is immediately triggered by `showPaletteCmdDef.execute()`.

>In base.html, the

You can then click on the blue buttons and the dropdown menu to navigate throughout the GUI.

If you go to Designs > Load Design, you're then brought to the user inputs page, where you can give parameters that are necessary for generating the design that you selected.
> In `template.html`, there is a `<form>` element with a set `id` that contains all of the `<input>` elements defined in

### Progress
#### File reorganization
We started out by restructuring the files in the top-most directory to contain the following:
1. `aide_gui.py` and `helper.py` have the code to run the Fusion 360 add-in.
2. `data/` contains the files necessary for displaying the GUI:
    1. `display.html` shows the current page in the GUI when it's being used.
    2. `structure.yaml` gives a "sitemap" of all the pages in the GUI and what data they show.
    3. `templates/` contains the default HTML templates which are combined with the data in `structure.yaml` to display specific pages.
        - `base.html` contains Javascript script that sends button presses in `display.html` to `aide_gui.py`.
    4. `images/` contains pictures that are displayed in the palette.
3. `dependencies/` contains the Python packages for displaying the GUI and processing user inputs:
    - `jinja2`, `markupsafe`, `urllib3`, `yaml`

#### Added functionality
We now have the ability to output a YAML (`params.yaml` in the top level directory) containing the user's inputs for a given design. This is the YAML that will be passed on to the design team to do the calculations.
> To do this, we added the `formToDict` function in `base.html`'s JavaScript that collects inputs within a HTML `<form>` object in `template.html`.

## AIDE TEMPLATE

Template utilizes Fusion 360, a CAD software, to create 3D models of the water treatment plant. Fusion is the ideal software for template because it allows components to be parameterized with equations and numbers. Parameters are "user-defined values used to control any reference geometry."

For better understanding template, let's think of template as a burger. Usually when you order a burger, you get a patty, slice of cheese, lettuce, and tomato. The number of each part of the burger can be parametrized as seen below.

 Now if you wanted to order a double-double, you would input number of patties to equal 2. Fusion 360 will take this input and update the parameters for cheese, lettuce and tomato.

<font style="color:lightblue"> Number of patties = 2 </font>
<br>
<font style="color:orange"> Number of buns = 2 </font>
<br>
<font style="color:yellow"> Number of cheese slices = </font> <font style="color:lightblue"> Number of patties </font>
<br>
<font style="color:lightgreen"> Number of lettuce slices = </font> <font style="color:lightblue">Number of patties </font>
<br>
<font style="color:pink"> Number of tomato slices = </font> <font style="color:lightblue"> Number of patties </font>

<br>
The goal for the summer is to finish the 3D models of all the components and test the assemblies to make sure all the components are linked properly. As parameter value changes, the geometry of assemblies should change accordingly without interfering with other assemblies. Furthermore, we are trying to find the best naming convention for Template to use in order to have consistent parameter names throughout AIDE and prevent misunderstanding between subteams.

### Naming Convention

The current naming convention is not consistent throughout Template or AIDE. In order to standardize the parameter names, we referenced the water treatment plant flowchart.

![](waterplantflowchart.png)

---------------------------------------------------------------------------------
POTENTIAL NAMING CONVENTION #1

Currently, the naming convention for parameter names is in the form of:

(sub-assembly)\_(components)\_(parameters)

However, this was not consistently used during the previous semester, and different assemblies or components have inaccurate parameters. The new naming convention we are proposing is that the parameters do not describe which assembly or component they are part of.

Instead of <font style="color:pink">Flocculator </font> <font style="color:lightgreen">\_ConcreteChannels </font> <font style="color:khaki">\_Length </font>, the parameter will be just called <font style="color:khaki">Length</font>.




---------------------------------------------------------------------------------
POTENTIAL NAMING CONVENTION #2

The naming convention will in the form of:

<font style="color:pink"> (assembly) </font>
<font style="color:lightgreen">\_(component) </font>
<font style="color:khaki">\_(parameter) </font>

<br>
An example would be:

<font style="color:pink">Flocculator </font>
<font style="color:lightgreen">\_ConcreteChannels </font>
<font style="color:khaki">\_LengthWidth </font>

<br>
If the assembly does not have a component, then it will be in the form of:

<font style="color:pink"> (assembly) </font>
<font style="color:khaki">\_(parameter) </font>

<br>
An example would be:

<font style="color:pink"> EntranceTank </font>
<font style="color:khaki"> \_Height </font>

<br>
This naming convention is still in discussion. Since there are lots of subcomponents, we are not completely certain that this method of naming parameters will be sustainable for future Template and Design subteams.  

<br>
Thanks for reading! :D
