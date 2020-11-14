# Family Dashboard

This dashboard should motivate the whole family to be more active/sportly and to live a digital life. But in respect to privacy and data that exist as long as you want!
!!

## Usage

1. Run `docker-compose up -d` to start all services (except frontend)
1. Enter `frontend` directory and start dashboard frontend with `npm run serve`
1. (Optional) Enter `imageprocessing` directory and start the face processing script: `python face_detect_cam.py`.
1. Navigate to http://localhost:1024 into your browser to open the dashboard.
1. To log into django admin backend navigate to http://localhost:8000/admin and use the credentials: `root:root1234`

--> to change frontend from debug to prod mode; change main.js django and socketIo stub svc to real data (both true to false)

## Connect Django Server with Strava

This steps has do be done for every new athelete you want to retrieve events for. 
This process is pretty manual so far and is very annoying because of the secret management. 
We should refactor this this to an automatic process of "Adding new athletes to your dashboard".
This can be done on django server (as it is already our admin console).

1. Open on browser: https://www.strava.com/oauth/authorize?client_id=26790&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=auto&scope=activity:read 
1. Authorize the "Family Dashboard" app.
1. You gets redirected to an url similar to this one: http://localhost/exchange_token?state=&code=#your_code#&scope=read,activity:read
1. Copy over #your_code# and save it on clipboard.
1. Call on bash `curl -X POST https://www.strava.com/api/v3/oauth/token -d client_id=26790 -d client_secret=#client_secret# -d code=#copy_code_from_clipboard# -d grant_type=authorization_code`
1. You get a json response. Fill in the required information for an athlete (checkout stravapolling/main.py STRAVA_ATHLETES variable).
1. Afterwards you should receive events for the added strava athlete.

## 💻 Planned Features? 

- Stats
  - Sports
    - Show weekly/monthly/yearly statistics in contrast to last year (volume, pace, hours)
    - Any many more...
  - Living
    - Sugar consumption per day
    - Coffee consumption per month
    - Watched hours Netflix,Youtube... per week
    - Working time
    - Sleeping time
    - Ecological foodprint
  - Home
    - Monthly power consumption
- Gamification to have an low ecological foodprint
- Photo Slider
- Useful contextual information (Weather, TRAM, ...)
- Upcoming family or personal events (birthday's, events in your city, etc.)
- Competition between kids (depending on several stats)
- AI Stuff (Use cases):
  - What persons are standing in front of the dashboard?

## ⚙️ Under the Hood 

Technologies, that will take place in this project:
- Vue (Dynamicness into frontend)
- Django (Data input and retrieval as well as persistence)
- socket.io (Websocket Server)
- PostgresQL (Database)
- Redis (Key/Value Store, Ephemeral database for event stream between backend services)
- Docker (Application Packaging/Runtime)
- Tensorflow & ScitKit for face recognition and classification
Eventually:
- Kubernetes (Orchestration to handle the massive load, that comes from the family members ;) )
