Introduction
============================
The Peer Review project is a course project for CS 485/540. This project aims at building a Manuscript Review System to assist SCIENCE WRITERS COMMITTEE which aims at helping Emory researchers improve their manuscripts, learn from different research areas and gain more experience of reviewing others’ paper.
____________________________
<h3>How to edit:</h3>

Install virtual environment: <code>pip install virtualenv</code><br>
Start virtual environment: <code>virtualenv prenv; source prenv/bin/activate</code><br>
Install requirements: <code>cd PeerReview; pip install -r requirements.txt</code><br>


In windows:<br>
Install virtual environment: <code>pip install virtualenv</code><br>
Start virtual environment: <code>virtualenv prenv; prenv\Scripts\activate;</code><br>
Install requirements: <code>cd PeerReview; pip install -r requirements.txt;  </code><br>


Original Design
============================
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
