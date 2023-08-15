======================================
Materials Compendium
======================================

The Materials Compendium package facilitates the parsing of
essential material composition data from the "Compendium of Material
Composition Data for Radiation Transport Modeling," a comprehensive
resource provided by the esteemed Pacific Northwest National Laboratory
(PNNL). This package equips radiation transport modelers with the
necessary tools to access material properties crucial for accurate
simulation within various radiation transport codes.

.. raw:: html

    <script language="javascript"> 
    function pyneToggle(title, showHideDiv, switchTextDiv) {
        var ele = document.getElementById(showHideDiv);
        var text = document.getElementById(switchTextDiv);
        if(ele.style.display == "block") {
                ele.style.display = "none";
            text.innerHTML = title + " [+]";
        }
        else {
            ele.style.display = "block";
            text.innerHTML = title + " [-]";
        }
    } 
    </script>

    <div id="pynemenuheader">
      <a id="startHeader" 
         href="javascript:pyneToggle('Getting Started', 'startContent', 'startHeader');">
         Getting Started [+]</a>
    </div>
    <div style="clear:both;"></div>
    <div id="pynemenucontent">
      <div id="startContent" style="display:none;">
        <ul>
          <li><a href="install/index.html">Install</a></li>
          <li><a href="examples/materials-compendium.html">Example</a></li>
        </ul>
      </div>
    </div>

    <br />
    <div id="pynemenuheader">
      <a id="usingHeader" 
         href="javascript:pyneToggle('Using PyNE', 'usingContent', 'usingHeader');">
         Using Materails Compendium [+]</a>
    </div>
    <div style="clear:both;"></div>
    <div id="pynemenucontent">
      <div id="usingContent" style="display:none;">
        <ul>
          <li><a href="usersguide/index.html">User's Guide</a></li>
          <li><a href="api/index.html">API Documentation</a></li>
          <li><a href="mailto:pyne-users+subscribe@googlegroups.com?subject=Subscribe&body=Send this message to subscribe to the list">Join</a> the <a href="https://groups.google.com/forum/#!forum/pyne-users" target="_blank"> Users</a> mailing list.
          <li><a href="https://github.com/pyne/materials-compendium/issues">Report an Issue</a></li>
        </ul>
      </div>
    </div>

    <br />
    <div id="pynemenuheader">
      <a id="contributeHeader" 
         href="javascript:pyneToggle('Contribute', 'contributeContent', 'contributeHeader');">
         Contribute [+]</a>
    </div>
    <div style="clear:both;"></div>
    <div id="pynemenucontent">
      <div id="contributeContent" style="display:none;">
        <ul>
          <li><a href="https://pyne.io/devsguide/index.html">Developer's Guide</a></li>
          <li><a href="http://github.com/pyne/materials-compendium">Source Code</a></li>
          <li><a href="mailto:pyne-users+subscribe@googlegroups.com?subject=Subscribe&body=Send this message to subscribe to the list">Join</a> the 
              <a href="https://groups.google.com/forum/#!forum/pyne-users" target="_blank">Developers</a> mailing list.
          <li><a href="https://pyne.io/dev_team.html">The PyNE Team</a></li>
        </ul>
      </div>
    </div>

    <br />
    <div id="pynemenuheader">
      <a id="learnHeader" 
         href="javascript:pyneToggle('Learn More', 'learnContent', 'learnHeader');">
         Learn More [+]</a>
    </div>
    <div style="clear:both;"></div>
    <div id="pynemenucontent">
      <div id="learnContent" style="display:none;">
        <ul>
          <li><a href="https://pyne.io/theorymanual/index.html">Theory Manual</a></li>
          <li><a href="https://pyne.io/pubs.html">Publications</a></li>
          <li><a href="previous/index.html">Release Notes</a></li>
          <li><a href="https://pyne.io/gsoc/index.html">Project Ideas</a></li>
        </ul>
      </div>
    </div>

.. toctree::
     :maxdepth: 1
     
     api/index

.. _GitHub project site: https://github.com/pyne

.. _github: https://github.com/pyne/materials-compendium

