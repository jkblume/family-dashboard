<template>
  <div id="app">
    <base-layout>
      <router-view :key="this.$route.fullPath" />
    </base-layout>
  </div>
</template>

<script>
import BaseLayout from "@/components/base/BaseLayout";

export default {
  components: {
    BaseLayout,
  },
};
</script>

<style lang="scss">
body {
  overflow: hidden;
}
</style>
