# Family Dashboard

This dashboard should motivate the whole family to be more active/sportly and to live a digital life. But in respect to privacy and data that exist as long as you want!

## Usage

1. Run `docker-compose up -d` to start all services (except frontend)
1. Start dashboard frontend with `npm run serve`
1. Change directory to imageprocessing. Start the face processing script: `python face_detect_cam.py`.
1. Navigate to http://localhost:1024 into your browser to open the dashboard.

--> to change frontend from debug to prod mode; change main.js django and socketIo stub svc to real data (both true to false)

## Infrastructure Setup

Be warned: Traffic is currently transfered over http (not encrypted) and you are opening port 8000 to the internet.

1. You need to create a DynDNS Entry (https://ddnss.de/) to get a static IP
    1. Jakob: familydashboard.ddnss.org
    1. Max: jarlmax.ddnss.org
1. Open your FritzBox UI in browser and route to: Internet > Freigaben > DynDNS
    1. Enter your data like in the following screenshot. Get the update link from the actions provided on https://ddnss.de/ua/vhosts_list.php ![Fritzbox DynDNS Configuration](/docs/fritzbox-dyndns.png?raw=true "Fritzbox")
1. You have to also provide a "Portfreigaben" in your fritzbox, to route incoming traffic from your fritzbox to the device that is running the djangoserver. 
    1. Route to Internet > Freigaben > Portfreigaben and press "Gerät für Freigabe hinzufügen"
    1. Select your device, where the django server is currently running.
    1. Press "Neue Freigabe" and use the configuration: "Protokoll": TCP, "Port an Gerät": 8000 to 8000, "Port extern  gewünscht": 8000
    1. Save it!
1. Check if requests are routed to your django server:
    1. Execute in shell: `curl http://jarlmax.ddnss.org:8000/`
    1. You should get a response from django server and see a log entry in django server logs if everything works.

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
