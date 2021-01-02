<template>
    <div class="layout-wrapper">
        <div class="main">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-12">
                        <button style="width: 100%; height: 80px; margin: 10px" class="btn btn-primary" @click="letFlow(400)">Let 400ml water flow</button>
                        <button style="width: 100%; height: 80px; margin: 10px" class="btn btn-primary" @click="letFlow(800)">Let 800ml water flow</button>
                        <button style="width: 100%; height: 80px; margin: 10px" class="btn btn-primary" @click="letFlow(1200)">Let 1200ml water flow</button>
                        <button style="width: 100%; height: 80px; margin: 10px" class="btn btn-primary" @click="letFlow(1600)">Let 1600ml water flow</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import { services } from "@/main";

    export default {
        name: "home",
        components: {},
        data() {
            return {
            }
        },
        watch: {},
        computed: {},
        mounted() {},
        methods: {
            letFlow: function (waterVolume) {
                let oneMilliliterDuration = 5000 / 440
                let duration = oneMilliliterDuration * waterVolume
                if (duration > 20000) {
                    duration = 20000;
                }
                console.log("Will order flow of " + duration + " ms");
                services.waterControlService.letWaterFlow(duration);
            },
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
