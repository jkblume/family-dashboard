<template>
  <div>
      Activity Feed:
      <div v-for="activity in activityFeed">
          {{ activity }}
      </div>
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
    name: "base-activity-feed",
    data() {
        return {
            socket: null,
            eventBusUrl: "http://localhost:8080",
            activityFeed: []
        }
    },
    mounted() {
        this.createNotificationConnection();
    },
    methods: {
        createNotificationConnection: function () {
            this.socket = io(this.eventBusUrl);
            this.socket.on(`notifications_server`, function(data) {
                let json = JSON.parse(data);
                this.activityFeed.unshift(json);
            }.bind(this));
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
