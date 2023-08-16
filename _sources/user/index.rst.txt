.. _user:

Materials Compendium
====================

The **Materials Compendium** package facilitates the parsing of
essential material composition data from the “Compendium of Material
Composition Data for Radiation Transport Modeling,” a comprehensive
resource provided by the esteemed Pacific Northwest National Laboratory
(PNNL). This package equips radiation transport modelers with the
necessary tools to access material properties crucial for accurate
simulation within various radiation transport codes.

Installation
------------

Installation from PyPI
~~~~~~~~~~~~~~~~~~~~~~

To integrate the **Materials Compendium** package seamlessly into your
workflow, you can use the `Python Package
Index <https://pypi.org/project/materials-compendium/>`__ using ``pip``
command:

.. code:: sh

   pip install materials-compendium

Installation from Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, if you prefer to work directly from the repository,
follow these steps:

.. code:: sh

   git clone https://github.com/pyne/materials-compendium.git
   cd materials-compendium
   pip install .

For running tests, use:

.. code:: sh

   pip install .[test]

Disclaimer
----------

-  The material composition data enclosed within the JSON file are
   meticulously curated and aligned with Revision 2 of the Compendium.
   These data are thoughtfully annotated with references for user
   assurance. It’s imperative to acknowledge the potential variances in
   composition or densities for certain materials, and we’ve diligently
   included ranges in references whenever feasible.
-  For materials not cataloged in the provided references, users may
   find it necessary to supply application-specific impurity
   information.
-  We stress the importance of meticulously aligning simulation
   parameters, such as reaction cross sections, within your selected
   radiation transport code to uphold the integrity of simulation
   outcomes.

Noteworthy
----------

-  While this script is meticulously tailored to JSON file parsing for
   radiation transport modeling, its adaptability for other applications
   is an avenue worth exploring.

Contributions
-------------

We extend a warm invitation to contribute to the **Materials
Compendium**. We believe that fostering an environment of collaboration
is paramount. Should you wish to contribute, the process is as
straightforward as forking our repository on GitHub, implementing your
modifications, and subsequently initiating a pull request. Should
queries arise or assistance be required during this process, please
don’t hesitate to engage with us through the PyNE mailing list
(https://groups.google.com/forum/#!forum/pyne-dev,
pyne-dev@googlegroups.com). Your involvement will undoubtedly enrich the
package and its utility.