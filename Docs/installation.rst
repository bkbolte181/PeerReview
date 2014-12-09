Installation Instruction
========================================


Pre-requested programs
-----------------------
* This system is written in python / Django. 

* Please download python_ and install. 

* Please install pip_, a tool for installing and managing Python packages

.. * [OPTION]Please install sphinx_, a python documentation generator

In Unix
--------
* Install virtual environment::

    pip install virtualenv

* Start virtual environment::

    virtualenv prenv; source prenv/bin/activate

* Install requirements::

    cd PeerReview; pip install -r requirements.txt

In Windows
-----------
* Install virtual environment::

    pip install virtualenv

* Start virtual environment::

    virtualenv prenv; prenv\Scripts\activate;

* Install requirements: cd PeerReview::

    pip install -r requirements.txt; 

.. _python: https://www.python.org/
.. _pip: https://pip.pypa.io/en/latest/installing.html
.. _sphinx: http://sphinx-doc.org/

Adding the App
---------------
* Create your Django app::

    django-admin.py startproject myproj; cd myproj;

* Make sure it works::

    ./manage.py runserver

* Clone the latest PeerReviewApp::

    git clone 'https://github.com/bkbolte181/PeerReviewApp.git'

* Update the settings file using the parameters in sample-settings.py

* Test to make sure everything works::

    ./manage.py test
