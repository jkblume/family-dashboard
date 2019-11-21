<template>
  <div class="layout-wrapper">
    <div class="main">
        <div class="container-fluid">
            <div class="row">
                <div class="col-8">
                    <slot></slot>
                </div>
                <div class="col-4">
                    <base-activity-feed />
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import BaseActivityFeed from "./BaseActivityFeed";


export default {
  components: {
    BaseActivityFeed,
  },
};
</script>

<style lang="scss" scoped>
.layout-wrapper {
  display: flex;
  width: 100vw;
  height: 100vh;

  .main {
    padding: 3rem 2rem;
    overflow-y: scroll;
    width: 100%;
    background-color: #f5f4f7;
  }
}
</style>
