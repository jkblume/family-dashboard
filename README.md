# Family Dashboard

This dashboard should motivate the whole family to be more active/sportly and to live a digital life. But in respect to privacy and data that exist as long as you want!

## Usage

1. Run `docker-compose up -d` to start all services (except frontend)
1. Start dashboard frontend with `npm run serve`
1. Change directory to imageprocessing. Start the face processing script: `python face_detect_cam.py`.
1. Navigate to http://localhost:1024 into your browser to open the dashboard.

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
Eventually:
- Kubernetes (Orchestration to handle the massive load, that comes from the family members ;) )
