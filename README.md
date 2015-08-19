College Gameday Board of Science
================================

The College Gameday Board of Science (CGBS) is a simple sport picking app to
provide a way for people to compare their right-wrong record.  The project
is also an attempt for me to gain exposure and practice with a web framework,
as well as maintain general web development skills.

CGBS is built on top of the django webapp framework.  It does not make use of any
sort of external api ( sports api's are expensive :c ), so games must be entered
manually by an admin.

Known Issues
------------

* Passed games list in the season detail will get very long very quick.
* Backing out of a game detail shows old picks if user picked before viewing game detail.

Priority Todo
-------------

* Back Buttons

* At least some basic tests, especially when we get management working.

* Spread out CSS

* Have left and right sections prefer the bottom.

Stretch Todo
------------

* Management
  * Simulate week
  * Increment week
  * Clear games
  * Clear picks
  * Clear teams

* Game detail revamp
* Fancy jquery widget to show pick proportion?
 * http://p.ar2oor.pl/cprogress/
 * http://designscrazed.org/jquery-css3-progress-bars/

* Create user_pick_history snippit

* User Detail
  * List User's Pick History

* User Preferences
    *Display Name

* Utilize team colors when displaying
* Blogify Front Page News 

* Team Detail
 * List passed/upcomming games
 
Housekeeping
------------
* Split style.css into functional parts
* Clean picker.models
* Back up users in a fixture

Live Server
-----------

If this project is still active, it can be found at

https://cgbs.herokuapp.com/

Development Console
-------------------

Development is hosted on Cloud9 IDE.

https://ide.c9.io/lebull/cgbs

Source
------

Source is hosted by github.

https://github.com/lebull/cgbs

