<template>
    <div>
        <div v-if="lastEvent && lastEvent.activityType === 'DETECTED_PERSON'">
            <div class="activity-message" v-html="getWelcomeMessage(lastEvent)"></div>
            <img class="responsive" :src="'data:image/png;base64,' + toImage(lastEvent.data.image)"/>
        </div>
        <div v-if="lastEvent && lastEvent.activityType === 'RANDOM_GOOGLE_PHOTO'">
            <div class="activity-message" v-html="getWelcomeMessage(lastEvent)"></div>
            <img class="responsive" :src="lastEvent.data.publicUrl"/>
        </div>
    </div>
</template>

<script>
    import moment from "moment"

    export default {
        name: "dashboard-center",
        props: {
            lastEvent: {
                type: Object,
                default: () => ({}),
            },
        },
        data() {
            return {}
        },
        computed: {},
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
                    moment.locale('de');
                    let time = moment.unix(activity.timestamp).fromNow();
                    let person = ((activity.data.person) ? activity.data.person.name : "Unbekannte Person");
                    return `Schön, dich zu sehen, <b>${person}</b>`
                }
                if (activity.activityType === 'RANDOM_GOOGLE_PHOTO') {
                    moment.locale('de');
                    let time = moment.unix(activity.timestamp).fromNow();
                    let person = ((activity.data.person) ? activity.data.person.name : "Unbekannte Person");
                    return `Danke für das Foto <b>${person}</b>`
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

</style>
