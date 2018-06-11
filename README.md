# aide
The integrated AIDE tool that provides a GUI, Fusion drawing capabilities, and a documentation engine.

## Glossary

Terms are *italicized* when referenced later on.

* **Design** - GitHub repository of all of the necessary starting files

    * **Design YAML** - lists unassigned parameters in the 3D models

    * **Design F3D** - contains 3D models of components with parametrized values

    * **Design Docs** - MarkDown files/photos of documentation with unassigned plant parameters

    * All the subsequent files the *Design* needs are located at specific locations in here. Think of this as akin to pointing to a particular package and all of the sub-packages are located where they should be. This makes it necessary to develop a strict skeleton directory for what to name the various resources.

* **aide_gui** - F360 plugin where the user enters in their parameters

    * **User YAML** - contains plant parameter values entered by the user

* **aide_design** - performs calculations on *User YAML* values to produce specific plant parameters

    * **Design Class** - performs calculations for a given plant component

    * **Design Instance YAML** - contains scaled, explicit values of plant component parameters

* **aide_draw** - Assigns *Specific Plant YAML* values to make updated, plant-specific 3D models

    * **Design Instance F3D** - contains 3D models of components with explicitly assigned parameters

* **aide_document** - Generates documentation files for the construction of a given plant

    * **Design Instance Docs** - documentation files with explicitly assigned parameters

    * **Special Words YAML**- list of specially translated words in a YAML

        * *NOTE*: Would this be stored with the *Design*, or given locally by the user?

    * **Design Instance Website** - website built using Jekyll and uploaded to GitHub Pages, containing all documentation

## Installation

1. Desired *Design* repository (This step can be skipped if the user would like to use the online GitHub repository directly)

    1. git clone

    2. ZIP file

2. Fusion 360

3. Fusion 360 Add-In

    3. *aide* package

        1. *aide_gui* package

        2. *aide_design* package

        3. *aide_draw* package

        4. *aide_document* package

* All of the dependencies can be included as sdists (source code distributions) directly under the main package. This will also be reflected within our aide repo online, but we’ll keep each project separate on GitHub so that the sdists within aide will be clones of the latest released version of the aide pip packages.

## Initial Setup

1. Open F360/*aide_gui*

    1. Input:

        1. Desired parameters

        2. Desired *Design* location - options:

            1. Local file location: downloaded repository

            2. URL: link to the desired *Design* GitHub URL

            * This is when the user chooses what they are going to build

        3. GitHub credentials (for *Design Instance Website* upload)

    2. Output *User YAML*

## Parameter Processing

* *NOTE*: What should be the user’s "springboard" - the very initial step to running everything past this point? Some choices we’ve been discussing:

    * Making a separate GUI (This is the best option in my opinion, and processing changes to files would be much easier)

    * Opening command line Python (More difficult and intimidating for the user, but could be a good initial product)

1. Run *aide_design*

    1. Generate *Design Instance YAML *from:

        1. *Design YAML*

        2. *User YAML*

2. Run *aide_draw*

    2. Generate *Design Instance F3D* from:

        3. *Design F3D*

        4. *Design Instance YAML*

## Documentation Creation

1. Run *aide_document*

    1. Generate *Design Instance Docs* from:

        1. *Design Docs*

        2. *Design Instance YAML*

    2. Translate *Design Instance Docs* with *Special Words YAML* accounted for

    3. Convert *Design Instance Docs* to PDF and/or DOCX

    4. Upload *Design Instance Docs* via Jekyll+GitHub Pages to *Design Instance Website*

## User-Made Changes

* *NOTE*: Let’s say that the user makes changes to the general documentation within their local *Design Template*, and then we need to send out some changes via the remote repo. We’ll need to be able to preserve their changes, while at the same time merging them with ours. Having the user resolve merge conflicts is out of the question, but we could possibly make a local branch for the user to edit? That doesn’t solve the issue of having to resolve merge conflicts, though. We could also make separate repos for the *General Plant Docs* and the *General Plant YAML/F3D*.

    * How about this: if the user is fine with the design as is, have them input a URL when running *aide_gui*. If the user would like to make changes, have them download the *Design* repository and make changes there.

## AIDE Pseudo-code MVP1
```python
import aide_design
import aide_document
import aide_draw
import aide_render
import aide_gui

#design_repository_path = get_user_design_repository_path() #get input from the User
user_params_yaml_path = aide_gui.run(design_repository_path)  
# User opens top level design in Fusioin that is already downloaded
design_yaml_path = aide_design.design(user_params_yaml_path)
aide_draw.draw(open_fusion_document, design_yaml_path)
aide_document.document(open_documentation, design_yaml_path)

```
default user params path: user_params_YYYY_MM_DD_HH_SS.yaml
default design path: design_YYYY_MM_DD_HH_SS.yaml
