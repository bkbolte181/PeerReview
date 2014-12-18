Manuscript Review System
============================
This course project for [*CS 485/540*](http://www.mathcs.emory.edu/~cs540000/) aims at building a Manuscript Review System to assist SCIENCE WRITERS COMMITTEE to help Emory researchers improve their manuscripts, learn from different research areas and gain more experience of reviewing others’ paper.
____________________________

Installation(Docs/installation.rst)
----------------------------------------
**Pre-requested programs**
* This system is written in [python / Django](https://www.djangoproject.com/). 
* Please download [python](https://www.python.org/) and install. 
* Please install [pip](), a tool for installing and managing Python packages
* `[OPTION]`Please install [sphinx](http://sphinx-doc.org/), a python documentation generator

**In Unix**
* Install virtual environment: <br><code>pip install virtualenv</code>
* Start virtual environment: <br><code>virtualenv prenv; source prenv/bin/activate</code>
* Install requirements: <br><code>cd PeerReview; pip install -r requirements.txt</code>

**In Windows**
* Install virtual environment: <br><code>pip install virtualenv</code>
* Start virtual environment: <br><code>virtualenv prenv; prenv\Scripts\activate</code>
* Install requirements: <br><code>cd PeerReview; pip install -r requirements.txt</code>

Deployment(Docs/deployment.rst)
----------------------------------------

**Using Django with WSGI

* A guide for using Django wish WSGI can be found here(https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/)
* Detailed instructions for installing and configuring Apache can be found elsewhere, such as here(http://httpd.apache.org/docs/2.4/install.html)
* Once Apache has been installed, you need to install and configure modwsgi. Complete instructions for this can be found here(http://httpd.apache.org/docs/2.4/install.html)
* The instructions below will assume you are running a Linux distribution.
* Download tarball for modwsgi from here(https://github.com/GrahamDumpleton/mod_wsgi/releases)
* Unpack the tarball:<code>tar xvfz mod_wsgi-4.4.0.tar.gz</code>
* Run:<code>make</code>

**Installations

* Python 2.7.6
* Pip
* Virtualenv (optional – use this if you plan to use shared hosting)
* Use the requirements document in the Django application database to install the dependencies for the project:<code>(sudo) pip install -r requirements.txt</code>

**Clone the Project from Github

* Clone the project:<code>git clone https://github.com/bkbolte181/PeerReview.git</code>
* Run tests:<code>./manage.py test</cdoe>
* The file wsgi.py will be in the project directory

**Configure modwsgi

* The steps for configuring modwsgi can be found here(https://code.google.com/p/modwsgi/wiki/QuickConfigurationGuide)
* Instructions for serving static files with Apache can be found here(https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/modwsgi/)

Try Our System
----------------------------
**In your own machine**
* Download all the codes from github
* Follow the installation instructions
* Enter the folder containing the file manage.py,<br>
<code>cd PeerReview</code><br>
<code>python manage.py migrate</code><br>
<code>python manage.py runserver</code>
* [normal user](http://127.0.0.1:8000/)
* [admin](http://127.0.0.1:8000/admin_login)

**Deploymented version**
*  [normal user](http://istanbul.mathcs.emory.edu/PeerReview/)
*  [admin](http://5ae8d563.ngrok.com/admin_login)
*  [docs](http://peerreview.readthedocs.org)

Mockups and codes
----------------------------
Mockups: [Design/Mockup/html demo/](https://github.com/bkbolte181/PeerReview/tree/master/Design/Mockup/html\ demo)<br>
Django codes: [PeerReview/PeerReviewApp/](https://github.com/bkbolte181/PeerReview/tree/master/PeerReview/PeerReviewApp)

Documents
----------------------------
Documents, sitting in the folder [Docs/_build/html/](https://github.com/bkbolte181/PeerReview/tree/master/Docs/_build/html), contains:
* Installation Instruction
* Deployment Instruction
* Code/Testing description
* On-line help for both admin and normal user
* Function list for implemented and planned functions

____________________________

Functions delivered in version 1.0 (2014/12)
---------------------------------------------
* Admin
  1. Log in as admin
  2. Browse reviewer and manuscript list
  3. Edit and save the assignments of the manuscripts to reviewers
  4. Submit final decisions of reviewer selections
* Normal User
  1. Create normal user account using Emory email adress.
  2. Log in as normal user.
  3. Edit own profile.
  4. Submit manuscripts.
  5. Save and edit a partially completed submission.
  6. Browse the list of submitted manuscripts.

Functions designed and planned for future
--------------------------------------------
* Admin
  1. Set up deadlines
  2. Set up and send email reminders
  3. Set up authors-reviewers meeting
  4. Set up the limitation number of manuscripts
  5. Request feedbacks from authors
* Normal User
  1. Email address validation through numbers generated by the system
  2. Manuscript adoption
  3. Review form submission
  4. Review form management
