<template>
  <div>
    <h1> Wer ist Zuhause? </h1>
	<span v-if="persons.length != 0">
	   <img class="responsive" v-bind:src="'data:image/png;base64,' + toImage(persons.image)" />
	</span>
  </div>
</template>

<script>
export default {
	name: "whos-home",
	props: ["persons"],
  data() {
        return {
            whoIsHome: []
        }
  }
	methods: {
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
.responsive {
  width: 30%;
  height: auto;
}

</style>
