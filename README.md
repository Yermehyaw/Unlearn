# Unlearn

Redefining the biochemical learning experience. . .
![unlearn logo](https://www.imghippo.com/i/keMyq1727286125.png)

# Introduction
## Un. . . What?
Unlearn is a web app created to serve as a coaching and practice platform to biochemist students in their second year of study, sytruggling to understand or remember cumbersome biochemistry concepts/information. 

It features a lessons/tips section for coaching and a quiz section for practice. It integrates a user-centered approach geared towards optimizing comprehension and exam preparedness amongst students with as little time and effort as possible.

## Why Create "another quiz app" ?
Unlearn is more than "another quiz app", it comes in a critical moment in time, when students need somethingbto ameliorate the time spent studying this subject. With one of the highest percentage of students fails in any course in many universities(if not every university), I believe its hight time we "changed the narrative" and more or less thats all what this app seeks to do: make biochemistry do easy to comprehend and master that I, you or anyother unfortunate fellow wont have to start preparing for a carryover, when the invigilator commands, "Pens Up!".
So there we go, its more about redefining abd changing the narrative on biochemistry, than it is about .... or even getting an A in the course. I want fellow students like myself to see the intricacies of this course as a wonder, strughle to wrap their heads around iits ever changing diversity, smile at its and with a little bit of luck, maybe even start to grow a fellowship with their once 'most dusliked course'. Because I believe if you look deep enough into this course, you mist just find the complex mind of a biological orchestrator.

## Why Do I Need this "Unlearn"?
Well. . . firstly if you are not a student of biochemistry nor interested in learning/mastering some basic/intermediate [biochemical cocepts](), contained in the web app, then  this application is not for you. Alternatively, if you find yourself having to understand, memorize or master biochemical cocepts especially for an upcoming exam/test, then this app was made with you in mind!
I never really struggled with this course(to be honest, I never did) because I alwsys saw it in this light, and with this coaching and pravtice app, I believe you can too. So theres it, dear reader. Redefining the biochemical learnibg experience

# Installation
## Okay. . . How Do I Get Started?
Firstly, you'll need a working internet connection, then a good web browser or an ssh client application. The ssh client application will allow you to use the console feature of the web app, the [Git bash]() app is highly recommended if you're on windows or MAC and [Termux]() or [Termuis]() for android and apple users.
Now you're almost fully set up. Next install ssh, this would allow you communicate with the console via secure ssh. It will be:
```sudo pkg install openssh``` (for Termux users)
Git bash already comes with ssh preinstalled.

Also allow the ssh client to install any additional prerequisite packages(if any) as required by the ssh client application you'll be using.

I will be using the [console](#console) vs I will be using my [web browser](#web-browser)

# Usage
### WEB BROWSER (Coming Soon . . .)
Using the web app on your browseer is pretty straightforward!

Visit [unlearn.com](www.contrite.unlearn.com) to get started.

Once youre on the web site, youll need to either create an account or log in, but if you dont have the time for such, you can always explore the app and take a quick quiz session or as I like to call it, a quick 'unlearn session'. Note that all progress made in such asession is unsaved and wont be recoverably when you use the app another time.

### CONSOLE
To use the console, you'll need to clone this repo into yoir terminal.
After cloning it simply run tge following commabds:
```cd Unlearn```
```./console.py```
and you're good to go!

#### Command List
**start**: Begin a quick quiz
**login**: login to retrieve previous progress
**signup**: new user signup
**n**: next question on a quiz
**p**: previous question on a quix
**i**: tip on a question
**submit**: submit quiz attempt
For more indepth documentation/details, kindly visit the [wiki]()

### APIs
The Unlearn web app utilizes a RESTFul API to provide information on the internals of the app to outsiders (especilaly fellow developers), who would be interested in utlizing this information i n their personal research or other web activities. If this sounds like you, then please continue reading.
#### Using the APIs
- api/v1/login
POST: Take the username and password hash to the authentication/validation result
- /api/v1/profile
GET: With a student_id, returns a dict of the details of the student
Else: {response:  invalid credential}
- /api/v1/status
GET: Login status [i.e logged in Vs not logged in]
- /api/courses
GET: Returns a list of all available courses
- /api/courses/<course_code>
GET: Return a list of topics in the course
POST: Creates a new course
- /api/topics/
GET:
Returns a list of all available topics
- /api/topics/<course_title>
GET:
With a valid course title entered, returns a list of all the topics of the specified course ELSE;
Returns a list of all available topics
POST:
Creates a new topic
- /api/lessons/<lesson_title>
GET:
With valid lesson title, return a dict comprising lesson title,  lesson content lesson description (and lesson_matr [coming soon])
Fail: An empty dict
POST:
With lesson content and description, Create a new lesson else;
Fails and return a 400 error
/- api/quiz/<course_title>
GET:
Returns a dict of all questions of a specified course ELSE;
Returns an empty dict
- /api/quiz/<course_title>/<topic_title>
GET:
Returns a dict of questions in the specified course and topic else
An empty dict
- /api/result/<quiz_id>/<student_id>
GET:
With valid student id, return the latest result of a student on a specified quiz id Else
Fail: An empty dict
- /api/result/<topic_title>/<quiz_id>/<student_id>
GET:
With a valid topic_title, quiz_id and student_id, return the latest result of a student on a specified quiz on a specific topic
Fail: An empty dict


# Contributing
(@yermehyaw) Akor Jeremiah <omoakor@gmail.com>
If you wist to collaborate on this project, kindly clone it and majevthe changes ad you deem fit.
It is highly recommended you begin by improving/making changes to the api and then in later version the web app can be easily added to those endloints.

# Related Projects


# Licencing
MIT licence
