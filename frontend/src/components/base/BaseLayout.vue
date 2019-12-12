<template>
  <div class="layout-wrapper">
    <div class="main">
        <div class="container-fluid">
            <div class="row">
                <div class="col-3">
                   <activity-feed :persons="persons"/>
                </div>
                <div class="col-6">
                    <slot></slot>
                     <cam-feed v-on:pass-on="testIt"/>
                </div>
                <div class="col-3">
                  <whos-home :persons="persons"/>
                </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
import CamFeed from "./CamFeed";
import ActivityFeed from "./ActivityFeed";
import WhosHome from "./WhosHome";

export default {
  name: "base-layout",
  components: {
    CamFeed,
    ActivityFeed,
    WhosHome,
  },
  data() {
    return {
      persons: []
    }
  },
  methods: {
		testIt (person) {
        this.persons = person
        console.log(123)
    }
  }
};
</script>

<style lang="scss" scoped>
.layout-wrapper {
  display: flex;
  width: 100vw;
  height: 100vh;

  .main {
    padding: 2rem 2rem;
    overflow-y: scroll;
    width: 100%;
    background-color: #f5f4f7;
  }
}
</style>
