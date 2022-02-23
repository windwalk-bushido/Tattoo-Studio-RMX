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
      url: "http://127.0.0.1:5000",
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
      let url = this.url;
      axios
        .get(url)
        .then((response) => {
          let fetched_images = response["data"];
          let temp_landscape_images = [];
          let temp_square_images = [];
          let temp_portrait_images = [];

          for (let image_type = 0; image_type < 3; image_type++) {
            let images = fetched_images["square"];
            if (image_type == 1) {
              images = fetched_images["landscape"];
            }
            if (image_type == 2) {
              images = fetched_images["portrait"];
            }
            let dont_stop_while_loop = true;
            let i = "0";
            let t = 0;
            while (dont_stop_while_loop) {
              if (images[i] != null) {
                if (image_type == 0) {
                  temp_landscape_images[t] = this.url + images[i].url;
                }
                if (image_type == 1) {
                  temp_square_images[t] = this.url + images[i].url;
                } else {
                  temp_portrait_images[t] = this.url + images[i].url;
                }
                i++;
                t++;
              } else {
                dont_stop_while_loop = false;
              }
            }
          }
          for (let j = 0; j < temp_landscape_images.length; j++) {
            this.landscape_images[j] = temp_landscape_images[j];
          }
          // All tattoos that have square dimensions should be divided in 2 groups.
          let e = 0;
          let o = 0;
          for (let y = 0; y < temp_square_images.length; y++) {
            if (y % 2 == 0) {
              this.square_images[e] = temp_square_images[y];
              e++;
            } else {
              this.square_images_odd[o] = temp_square_images[y];
              o++;
            }
          }
          // All tattoos in portrait orientation should be divided in 3 groups.
          // First: 1st, 4th, 7th.,.. Second: 2nd, 5th, 8th... Third: 3rd, 6th, 9th...
          for (let l = 0; l < 3; l++) {
            let x = 0;
            for (let k = l; k < temp_portrait_images.length; k += 3) {
              if (l == 0) {
                this.portrait_images_1[x] = temp_portrait_images[k];
              }
              if (l == 1) {
                this.portrait_images_2[x] = temp_portrait_images[k];
              } else {
                this.portrait_images_3[x] = temp_portrait_images[k];
              }
              x++;
            }
          }
          console.log(temp_landscape_images);
          console.log(temp_square_images);
          console.log(temp_portrait_images);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },

  mounted() {
    this.FetchImages();
    console.log("L ->  ", this.landscape_images);
    console.log("S ->  ", this.square_images);
    console.log("SO -> ", this.square_images_odd);
    console.log("P1 -> ", this.portrait_images_1);
    console.log("P2 -> ", this.portrait_images_2);
    console.log("P3 -> ", this.portrait_images_3);
  },
};
</script>

<template>
  <div class="">
    <NavV />
    <div class="pb-14 p-2 lg:ml-16 lg:p-4">
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#landscapes" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full" :tattoos="landscape_images" :slide_speed="3300" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#squares" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full lg:w-1/2" :tattoos="square_images" :slide_speed="4500" />
        <CarouselV class="w-full lg:w-1/2" :tattoos="square_images_odd" :slide_speed="6600" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#portraits" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_1" :slide_speed="7100" />
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_2" :slide_speed="5400" />
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_3" :slide_speed="2200" />
      </div>
    </div>
  </div>
</template>
