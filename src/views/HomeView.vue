<script>
import CarouselV from "../components/CarouselV.vue";
import axios from "axios";

export default {
  name: "HomeView",

  components: {
    CarouselV,
  },

  data() {
    return {
      url: "http://localhost:1337",
      landscape_images: [],
      square_images: [],
      portrait_images: [],
    };
  },

  methods: {
    FetchImages() {
      let url = this.url + "/tattoos";
      axios
        .get(url)
        .then((response) => {
          let fetched_images = response["data"];

          for (let y = 0; y < 3; y++) {
            let images = fetched_images[y.toString()];
            let dont_stop_while_loop = true;
            let i = "0";
            while (dont_stop_while_loop) {
              if (images.Images[i] != null) {
                if (y == 0) {
                  this.landscape_images[i] = this.url + images.Images[i].url;
                }
                if (y == 1) {
                  this.square_images[i] = this.url + images.Images[i].url;
                } else {
                  this.portrait_images[i] = this.url + images.Images[i].url;
                }
                i++;
              } else {
                dont_stop_while_loop = false;
              }
            }
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.FetchImages();
  },
};
</script>

<template>
  <div class="flex flex-wrap flex-row justify-center items-center w-full">
    <a href="#landscape" class="hidden w-0 h-0"></a>
    <CarouselV mrk="x" class="w-full" :tattoos="landscape_images" />
  </div>
  <div class="flex flex-wrap flex-row justify-center items-center w-full">
    <CarouselV mrk="x" class="w-1/2" :tattoos="square_images" />
    <CarouselV mrk="x" class="w-1/2" :tattoos="square_images" />
  </div>
  <div class="flex flex-wrap flex-row justify-center items-center w-full">
    <CarouselV mrk="x" class="w-1/3" :tattoos="portrait_images" />
    <CarouselV mrk="x" class="w-1/3" :tattoos="portrait_images" />
    <CarouselV mrk="x" class="w-1/3" :tattoos="portrait_images" />
  </div>
</template>

<style scoped></style>
