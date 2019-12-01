<template>
  <div>
      Activity Feed:
      <div v-for="activity in activityFeed">
        {{activity.person}}
        <img v-bind:src="'data:image/png;base64,' + toImage(activity.image)" />
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
            activityFeed: [],
            window: null,
        }
    },
    mounted() {
        this.window = window
        this.createNotificationConnection();
    },
    methods: {
        createNotificationConnection: function () {
            this.socket = io(this.eventBusUrl);
            this.socket.on(`notifications_server`, function(data) {
                let json = JSON.parse(data);
                console.log(json);
                this.activityFeed.unshift(json);
            }.bind(this));
        },
        toImage: function(string) {
            string = string.replace(/\r\n/g,"\n");
            var utftext = "";

            for (var n = 0; n < string.length; n++) {

                var c = string.charCodeAt(n);

                if (c < 128) {
                    utftext += String.fromCharCode(c);
                }
                else if((c > 127) && (c < 2048)) {
                    utftext += String.fromCharCode((c >> 6) | 192);
                    utftext += String.fromCharCode((c & 63) | 128);
                }
                else {
                    utftext += String.fromCharCode((c >> 12) | 224);
                    utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                    utftext += String.fromCharCode((c & 63) | 128);
                }

            }

            return utftext;
        }
    }
};
</script>

<style lang="scss" scoped>
</style>
