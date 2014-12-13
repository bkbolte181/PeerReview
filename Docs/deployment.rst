PeerReview Deployment Instructions
==================================

Using Django with WSGI
----------------------

* A guide for using Django wish WSGI can be found here::

    https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/ 

* Detailed instructions for installing and configuring Apache can be found elsewhere, such as here::

    http://httpd.apache.org/docs/2.4/install.html

* Once Apache has been installed, you need to install and configure modwsgi. Complete instructions for this can be found here::

    http://httpd.apache.org/docs/2.4/install.html.

* The instructions below will assume you are running a Linux distribution.

* Download tarball for modwsgi from here::

    https://github.com/GrahamDumpleton/mod_wsgi/releases

* Unpack the tarball::

    tar xvfz mod_wsgi-4.4.0.tar.gz

* Run::

    make

Installations
-------------

* Python 2.7.6
* Pip
* Virtualenv (optional – use this if you plan to use shared hosting)
* Use the requirements document in the Django application database to install the dependencies for the project::

    (sudo) pip install -r requirements.txt

Clone the Project from Github
-----------------------------

* Clone the project::

    git clone https://github.com/bkbolte181/PeerReview.git

* Run tests::

    ./manage.py test

* The file wsgi.py will be in the project directory

Configure modwsgi
-----------------

* The steps for configuring modwsgi can be found here::

    https://code.google.com/p/modwsgi/wiki/QuickConfigurationGuide

* Instructions for serving static files with Apache can be found here::

    https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/
