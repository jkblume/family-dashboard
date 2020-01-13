<template>
    <div class="layout-wrapper">
        <div class="main">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-3">
                        <activity-feed :activity-events="activityEvents"/>
                    </div>
                    <div class="col-6">
                        <center :activity-events="activityEvents"/>
                    </div>
                    <div class="col-3">
                        <who-is-home :activity-events="activityEvents"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ActivityFeed from "../components/dashboard/ActivityFeed";
    import WhoIsHome from "../components/dashboard/WhoIsHome";
    import Center from "../components/dashboard/Center";
    import io from 'socket.io-client';
    import { services } from "@/main";

    export default {
        name: "dashboard",
        components: {
            ActivityFeed,
            WhoIsHome,
            Center,
        },
        data() {
            return {
                activityEventsResult: [], //services.djangoServerService.getEvents(),
                activityEvents: [],
                socket: services.socketIoService.getActivityNotificationSocket(),
            }
        },
        watch: {
          "activityEventsResult.loaded": function () {
              if (!this.activityEventsResult.hasLoaded()) {
                  return;
              }

              this.activityEvents = this.activityEventsResult.apiData;
          },
        },
        mounted() {
            this.socket.on('notifications_server', function(data) {
                let json = JSON.parse(data);
                this.activityEvents.unshift(json);
            }.bind(this));
        },
        methods: {
        }
    };
</script>

<style lang="scss" scoped>
    .layout-wrapper {
        display: flex;
        width: 100vw;
        height: 100vh;

        .main {
            padding: 2rem 2rem;
            overflow-y: scroll;
            width: 100%;
            background-color: #f5f4f7;
        }
    }
</style>
