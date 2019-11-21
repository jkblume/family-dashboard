const path = require("path");

module.exports = {
  chainWebpack: (config) => {
    config.resolve.alias
      .set("$vue", "ue/dist/vue.esm.js")
  },
  devServer: {
    port: 1024,
    open: true,
    host: "localhost",
    contentBase: path.resolve(__dirname, "dist"),
    publicPath: "/",
  },
  css: {
    loaderOptions: {
      sass: {
        data: `
          @import "@/scss/_variables.scss";
        `,
      },
    },
  },
};
