<template>
    <div>
        <h1> Wer ist Zuhause? </h1>
        <span class="heading" v-for="activityEvent in detectedPersonActivityEvents">
            <img class="responsive" :src="'data:image/png;base64,' + toImage(activityEvent.data.image)"/>
        </span>
    </div>
</template>

<script>
    export default {
        name: "who-is-home",
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
            }
        }
    };
</script>

<style lang="scss" scoped>
    .responsive {
        width: 30%;
        height: auto;
    }

</style>
