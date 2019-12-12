<template>
  <div>
      <h1> Was passiert so? </h1>
		<span v-if="persons.length != 0">
        {{addNewActivity(persons)}}
      	</span>
		<span v-if="persons.length != 0">
	  		{{persons.first_name}} kam Nachhause um {{persons.Timestamp}}
		</span>
		<div class="heading" v-for="activity in allActivities">
        	{{activity.first_name}} kam Nachhause um {{activity.Timestamp}}
      	</div>
  </div>
</template>

<script>
export default {
	name: "acitivity-feed",
	props: ["persons"],
	data() {
        return {
            allActivities: []
        }
  	},
	methods: {
    addNewActivity: function (activity) {
            this.allActivities.unshift(activity)
            this.persons = []
		},
	}
};
</script>

<style lang="scss" scoped>

</style>
