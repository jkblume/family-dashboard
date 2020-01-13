<template>
    <div>
        <div class="activity-message" v-html="getWelcomeMessage(detectedPersonActivityEvents[0])"></div>
        <img class="responsive" :src="'data:image/png;base64,' + toImage(detectedPersonActivityEvents[0].data.image)"/>
    </div>
</template>

<script>
    import moment from "moment"

    export default {
        name: "center",
        props: {
            activityEvents: {
                type: Array,
                default: [],
            },
        },
        data() {
            return {
                whoIsHome: []
            }
        },
        computed: {
            detectedPersonActivityEvents() {
                return this.activityEvents.filter((activityEvent) => activityEvent.activityType === 'DETECTED_PERSON')
            }
        },
        methods: {
            toImage: function (string) {
                string = string.replace(/\r\n/g, "\n");
                var utftext = "";

                for (var n = 0; n < string.length; n++) {

                    var c = string.charCodeAt(n);

                    if (c < 128) {
                        utftext += String.fromCharCode(c);
                    } else if ((c > 127) && (c < 2048)) {
                        utftext += String.fromCharCode((c >> 6) | 192);
                        utftext += String.fromCharCode((c & 63) | 128);
                    } else {
                        utftext += String.fromCharCode((c >> 12) | 224);
                        utftext += String.fromCharCode(((c >> 6) & 63) | 128);
                        utftext += String.fromCharCode((c & 63) | 128);
                    }

                }

                return utftext;
            },
            getWelcomeMessage: function (activity) {
                if (activity.activityType === 'DETECTED_PERSON') {
                    console.log(activity.person.name)
                    moment.locale('de');
                    let time = moment(activity.timestamp).fromNow();
                    let person = ((activity.person) ? activity.person.name : "Unbekannte Person");
                    return `Schön, dich zu sehen, <b>${person}</b>`
                }
                if (activity.activityType === 'STRAVA_ACTIVITY') {
                    moment.locale('de');
                    let time = moment(activity.timestamp).fromNow();
                    let person = ((activity.person) ? activity.person.name : "Unbekannte Person");
                    return `<b>${person}</b> hat <b>${time}</b> Sport gemacht.`
                }
            },
        }
    };
</script>

<style lang="scss" scoped>
    .responsive {
        height: auto;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 80%;
    }
    .activity-message {
        text-align: center;
        font-size: 0.9rem;
    }
    .whosthere {
        text-align: center;
    }

</style>
