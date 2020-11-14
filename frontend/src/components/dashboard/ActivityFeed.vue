<template>
    <div>
        <h3 class="heading">Feed</h3>
        <div class="activity-message alert alert-success" v-for="activity in activityEvents">
            <h4 class="alert-heading">{{getActivityTitle(activity)}}</h4>
            <hr>
            <p>{{getActivityMessage(activity)}}</p>
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
                default: () => ([]),
            },
        },
        methods: {
            getActivityMessage: function (activity) {
                if (activity.activityType === 'DETECTED_PERSON') {
                    moment.locale('de');
                    let time = moment.unix(activity.timestamp).fromNow();
                    let person = ((activity.data.person) ? activity.data.person.name : "Unbekannte Person");
                    return `${person} ist ${time} vorbei gekommen.`
                }
                if (activity.activityType === 'STRAVA_ACTIVITY') {
                    moment.locale('de');
                    let time = moment.unix(activity.timestamp).fromNow();
                    let person = ((activity.data.person) ? activity.data.person.name : "Unbekannte Person");
                    return `${person} hat ${time} Sport gemacht.`
                }
                if (activity.activityType === 'RANDOM_GOOGLE_PHOTO') {
                    moment.locale('de');
                    let time = moment.unix(activity.timestamp).fromNow();
                    let person = ((activity.data.person) ? activity.data.person.name : "Unbekannte Person");
                    return `${person} hat ${time} ein zufälliges Foto auswählen lassen.`
                }
            },
            getActivityTitle: function (activity) {
                if (activity.activityType === 'DETECTED_PERSON') {
                    return "Wer ist denn da?"
                }
                if (activity.activityType === 'STRAVA_ACTIVITY') {
                    return "Sport Frei!"
                }
                if (activity.activityType === 'RANDOM_GOOGLE_PHOTO') {
                    return "Schau an, schau an..."
                }
            }
        }
    };
</script>

<style lang="scss" scoped>
    .activity-message {
        font-size: 0.9rem;
    }

    .heading {
        text-align: center;
    }
</style>
