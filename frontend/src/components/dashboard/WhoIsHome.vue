<template>
    <div>
        <h3 class="heading">Wer ist @home?</h3>
        <span class="heading" v-for="person in whoIsHome">
            <img class="responsive" :src="'data:image/png;base64,' + toImage(person.data.image)"/>
        </span>
    </div>
</template>

<script>
    export default {
        name: "who-is-home",
        props: {
            activityEvents: {
                type: Array,
                default: () => ([]),
            },
        },
        data() {
            return {
                whoIsHome: []
            }
        },
        watch: {
          "activityEvents": function () {
              for (let activityEvent of this.activityEvents) {
                  if (activityEvent.activityType !== "DETECTED_PERSON") {
                      continue;
                  }
                  let found = false;
                  for(let i = 0; i < this.whoIsHome.length; i++) {
                      if (this.whoIsHome[i].person.name === activityEvent.person.name) {
                          found = true;
                          break;
                      }
                  }
                  if (!found) {this.whoIsHome.push(activityEvent)}
              }
          },
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

    .heading {
        text-align: center;
    }

</style>
