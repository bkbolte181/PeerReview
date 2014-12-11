Manuscript Review System
============================
This course project for [*CS 485/540*](http://www.mathcs.emory.edu/~cs540000/) aims at building a Manuscript Review System to assist SCIENCE WRITERS COMMITTEE to help Emory researchers improve their manuscripts, learn from different research areas and gain more experience of reviewing others’ paper.
____________________________
<h3>How to edit:</h3>

Install virtual environment: <code>pip install virtualenv</code><br>
Start virtual environment: <code>virtualenv prenv; source prenv/bin/activate</code><br>
Install requirements: <code>cd PeerReview; pip install -r requirements.txt</code><br>


In windows:<br>
Install virtual environment: <code>pip install virtualenv</code><br>
Start virtual environment: <code>virtualenv prenv; prenv\Scripts\activate;</code><br>
Install requirements: <code>cd PeerReview; pip install -r requirements.txt;  </code><br>

Installation
----------------------------
**Pre-requested programs**
* This system is written in [python / Django](https://www.djangoproject.com/). 
* Please download [python](https://www.python.org/) and install. 
* Please install [pip](), a tool for installing and managing Python packages
* `[OPTION]`Please install [sphinx](http://sphinx-doc.org/), a python documentation generator

**In Unix**
* Install virtual environment: <code>pip install virtualenv</code>
* Start virtual environment: <code>virtualenv prenv; source prenv/bin/activate</code>
* Install requirements: <code>cd PeerReview; pip install -r requirements.txt</code>

**In Windows**
* Install virtual environment: <code>pip install virtualenv;</code>
* Start virtual environment: <code>virtualenv prenv; prenv\Scripts\activate;</code>
* Install requirements: cd PeerReview: <code>pip install -r requirements.txt;</code>

Deployment
----------------------------
**Adding the App**
* Create your Django app: <code>django-admin.py startproject myproj; cd myproj;</code>
* Make sure it works: <code>./manage.py runserver<code>
* Clone the latest PeerReviewApp: <code>git clone 'https://github.com/bkbolte181/PeerReviewApp.git'</code>
* Update the settings file using the parameters in sample-settings.py
* Test to make sure everything works: <code>./manage.py test<code>

Original Design
----------------------------
We have presented our mockup demo twice, you can check the design in the 
folder [Design/Mockup/html demo/](https://github.com/bkbolte181/PeerReview/tree/master/Design/Mockup/html\ demo)

Code for functional demo
============================
For our functional demo version 1.0, please reference all the codes located in  
the folder [PeerReview/PeerReviewApp/](https://github.com/bkbolte181/PeerReview/tree/master/PeerReview/PeerReviewApp)

Documents
============================
Documents, sitting in the folder [Docs/_build/html/](https://github.com/bkbolte181/PeerReview/tree/master/Docs/_build/html), contains:

* Installation Instruction
* Deployment Instruction
* Code/Testing description
* On-line help for both admin and normal user
* Function list for implemented and planned functions

Try the system locally
============================
Download all the codes and enter the folder containing the file manage.py, run<br>
<code>cd PeerReview</code><br>
<code>python manage.py migrate</code><br>
<code>python manage.py runserver</code>

Deploymented version
============================
The project has been employed, so it can be visited in the following link,<br>
*  [normal_user](http://5ae8d563.ngrok.com/)
*  [admin](http://5ae8d563.ngrok.com/admin_login)
*  [docs](http://peerreview.readthedocs.org)
