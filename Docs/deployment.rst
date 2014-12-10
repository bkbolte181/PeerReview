Deployment Instruction
======================

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
