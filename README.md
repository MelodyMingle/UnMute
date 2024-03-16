# Introduction

### What did we build?

UnMute is a revolutionary music social media application that integrates with Spotify's API to offer a seamless blend of music discovery and social interaction. 

__Key Features:__

* Personalized Music Discovery: Utilizes Spotify's API for tailored music recommendations and curated playlists based on personal tastes and social connections.

__Technologies and Languages Used:__

* __Frontend:__ Utilized modern responsive user interface, and vercel for deployment. Python, Javascript for efficient state management across the app.
Microservices, APIs, and 3rd Party Integrations:
* __Spotify API:__ The core of our music features, allowing access to Spotify's extensive music library, user data, and playback capabilities.
* __Auth0 for Authentication:__ Ensures secure login and user authentication.
In the landscape of digital music and social media, UnMute stands out by addressing the fragmentation in music discovery and social connectivity.

## Project: UnMute
## Authors: 
* MelodyMingle
    - Felix Taveras
    - Andrea Riley
    - Dominique McClaney
    - Christopher Acosta

### Main features

* Example app with custom user model

* TailwindCSS static files included

* User registration and logging

* Separated requirements files

* SQLite

# Usage

Create a virtual environment:

    $ python3 -m venv .venv

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/MelodyMingle/UnMute
    $ cd unmute
    
Activate the virtualenv for your project:
    
    $ source .venv/bin/activate

    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
