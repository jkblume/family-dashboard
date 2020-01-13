<template>
    <div>
        <h1> Was passiert so? </h1>
        <div v-for="activity in activityEvents">
            <div class="activity-message" v-html="getActivityMessage(activity)"></div>
        </div>
    </div>
</template>

<script>
    import moment from "moment"

    export default {
        name: "acitivity-feed",
        props: {
            activityEvents: {
                type: Array,
                default: [],
            },
        },
        methods: {
            getActivityMessage: function (activity) {
                if (activity.activityType === 'DETECTED_PERSON') {
                    moment.locale('de');
                    let time = moment(activity.timestamp).fromNow();
                    let person = ((activity.person) ? activity.person.name : "Unbekannte Person");
                    return `<b>${person}</b> ist <b>${time}</b> vorbei gekommen.`
                }
                if (activity.activityType === 'STRAVA_ACTIVITY') {
                    moment.locale('de');
                    let time = moment(activity.timestamp).fromNow();
                    let person = ((activity.person) ? activity.person.name : "Unbekannte Person");
                    return `<b>${person}</b> hat <b>${time}</b> Sport gemacht.`
                }
            }
        }
    };
</script>

<style lang="scss" scoped>
    .activity-message {
        font-size: 0.9rem;
    }
</style>
