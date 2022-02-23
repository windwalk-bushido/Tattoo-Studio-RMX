module.exports = {
  configureWebpack: {
    devServer: {
      headers: { "Access-Control-Allow-Origin": "*" },
      proxy: "http://127.0.0.1:5000/",
    },
  },
};
