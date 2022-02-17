<script>
import CarouselV from "../components/CarouselV.vue";
import NavV from "../components/NavV.vue";
import axios from "axios";

export default {
  name: "HomeView",

  components: {
    CarouselV,
    NavV,
  },

  data() {
    return {
      url: "http://localhost:1337",
      landscape_images: [],
      square_images: [],
      square_images_odd: [],
      portrait_images_1: [],
      portrait_images_2: [],
      portrait_images_3: [],
    };
  },

  methods: {
    FetchImages() {
      let url = this.url + "/tattoos";
      axios
        .get(url)
        .then((response) => {
          let fetched_images = response["data"];
          let temp_landscape_images = [];
          let temp_square_images = [];
          let temp_portrait_images = [];

          for (let y = 0; y < 3; y++) {
            let images = fetched_images[y.toString()];
            let dont_stop_while_loop = true;
            let i = "0";
            while (dont_stop_while_loop) {
              if (images.Images[i] != null) {
                if (y == 0) {
                  temp_landscape_images[i] = this.url + images.Images[i].url;
                }
                if (y == 1) {
                  temp_square_images[i] = this.url + images.Images[i].url;
                } else {
                  temp_portrait_images[i] = this.url + images.Images[i].url;
                }
                i++;
              } else {
                dont_stop_while_loop = false;
              }
            }
          }
          for (let i = 0; i < temp_landscape_images.length; i++) {
            this.landscape_images[i] = temp_landscape_images[i];
          }
          // All tattoos that have square dimensions should be divided in 2 groups.
          let e = 0;
          let o = 0;
          for (let i = 0; i < temp_square_images.length; i++) {
            if (i % 2 == 0) {
              this.square_images[e] = temp_square_images[i];
              e++;
            } else {
              this.square_images_odd[o] = temp_square_images[i];
              o++;
            }
          }
          // All tattoos in portrait orientation should be divided in 3 groups.
          // First: 1st, 4th, 7th.,.. Second: 2nd, 5th, 8th... Third: 3rd, 6th, 9th...
          for (let i = 0; i < 3; i++) {
            let x = 0;
            for (let y = i; y < temp_portrait_images.length; y += 3) {
              if (i == 0) {
                this.portrait_images_1[x] = temp_portrait_images[y];
              }
              if (i == 1) {
                this.portrait_images_2[x] = temp_portrait_images[y];
              } else {
                this.portrait_images_3[x] = temp_portrait_images[y];
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
  <div class="bg-black">
    <NavV />
    <div class="ml-16 p-4">
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#landscapes" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full" :tattoos="landscape_images" :slide_speed="3300" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#squares" class="hidden w-0 h-0"></a>
        <CarouselV class="w-1/2" :tattoos="square_images" :slide_speed="4500" />
        <CarouselV class="w-1/2" :tattoos="square_images_odd" :slide_speed="6600" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#portraits" class="hidden w-0 h-0"></a>
        <CarouselV class="w-1/3" :tattoos="portrait_images_1" :slide_speed="7100" />
        <CarouselV class="w-1/3" :tattoos="portrait_images_2" :slide_speed="5400" />
        <CarouselV class="w-1/3" :tattoos="portrait_images_3" :slide_speed="2200" />
      </div>
    </div>
  </div>
</template>
