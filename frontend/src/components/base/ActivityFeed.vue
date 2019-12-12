<template>
  <div>
      <h1> Was passiert so? </h1>
	  <span v-if="persons.length != 0">
	  		{{persons.first_name}} kam Nachhause um {{persons.Timestamp}}
		</span>
	   </div>
  </div>
</template>

<script>
export default {
	name: "acitivity-feed",
	props: ["persons"],
};
</script>

<style lang="scss" scoped>

</style>
