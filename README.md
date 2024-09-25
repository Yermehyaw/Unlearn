# Unlearn

Redefining the biochemical learning experience. . .

## Un. . . What?
Unlearn is a web app created to serve as a coaching and practice platform to biochemist students in their second year of study, sytruggling to understand or remember cumbersome biochemistry concepts/information. 

It features a lessons and tips section for coaching and a quiz section for practice. It integrates a user-centered approach geared towards optimizing comprehension and exam preparedness amongst students with as little time and effort as possible.

## Why Do I Need this "Unlearn"?
Well. . . firstly if you are not a student of biochemistry nor interested in learning/mastering some basic/intermediate [biochemical cocepts](), contained in the web app, then  this application is not for you. Alternatively, if you find yourself having to understand, memorize or master biochemical cocepts especially for an upcoming exam/test, then this app was made with you in mind!

## Okay. . . How Do I Get Started?
Firstly, you'll need a working internet connection, then a good web browser or an ssh client application. The ssh client application will allow you to use the console feature of the web app, the [Git bash]() app is highly recommended if you're on windows or MAC and [Termux]() or [Termuis]() for android and apple users.
Now you're almost fully set up. Next install openssl, this would allow you communicate with the console via secure ssh. It will be:
sudo pkg install ssh (for Termux users)
Git bash already comes with ssh preinstalled.

Also allow the ssh client to install any additional prerequisite packages(if any) as required by the ssh client application you'll be using.

I will be using the [console]() vs I will be using my [web browser]()


### WEB BROWSER
Using the web app on your browseer is pretty straightforward!

Visit [unlearn.com](www.contrite.unlearn.com) to get started.

Once youre on the web site, youll need to either create an account or log in, but if you dont have the time for such, you can always explore the app and take a quick quiz session or as I like to call it, a quick 'unlearn session'. Note that all progress made in such asession is unsaved and wont be recoverably when you use the app another time.

### CONSOLE
To use the console, youll need to be able to communicate to the server via ssh. To do this, youll need a valid ssh key. To generate one, visit [here](www.contrite.unlearn.com/ssh). You can only create a maximum of **two** ssh keys per ip address.

Next follow the prompt, copy the connection details shown, paste this in your client and youll set up and ready to begin.

For more indepth documentation/details, kindly visit the [wiki]()

## APIs
The Unlearn web app utilizes a RESTFul API to provide information on the internals of the app to outsiders (especilaly fellow developers), who would be interested in utlizing this information i n their personal research or other web activities. If this sounds like you, then please continue reading.
### Using the APIs
