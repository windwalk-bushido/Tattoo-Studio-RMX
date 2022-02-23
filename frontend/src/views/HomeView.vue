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
      url: "https://cutura-ink-serving.herokuapp.com/",
      landscape_images: [],
      square_images: [],
      square_images_odd: [],
      portrait_images_1: [],
      portrait_images_2: [],
      portrait_images_3: [],
      is_api_online: false,
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
          this.is_api_online = true;
        })
        .catch((error) => {
          this.is_api_online = false;
        });
    },
  },

  mounted() {
    this.FetchImages();
  },
};
</script>

<template>
  <div class="">
    <div class="body flex justify-center items-center w-screen h-screen z-10 absolute" v-if="is_api_online == false">
      <div
        class="flex flex-col justify-center items-center w-80 p-4 rounded-3xl shadow-lg border-4 border-green-700 bg-gray-800"
      >
        <div class="w-full text-center">
          <FAIcon :icon="['fas', 'bed']" class="text-8xl pb-8 text-green-300" id="loading_icon" />
        </div>
        <div class="w-full text-center text-white">
          <p>Uh oh.</p>
          <p>The API that fetches images has fallen asleep. Wake him up by clicking a button every couple of seconds.</p>
          <p>It should be awake in about 30 seconds from loading the website.</p>
          <button
            class="mt-8 mb-8 p-4 rounded-3xl shadow-lg font-semibold transition-all duration-150 ease-in bg-green-300 text-black hover:bg-white hover:text-green-700"
            @click="FetchImages()"
          >
            Wake API
          </button>
          <p>Thank you for your patience!</p>
        </div>
      </div>
    </div>
    <div class="hidden" v-else></div>

    <NavV />
    <div class="pb-14 p-2 lg:ml-16 lg:p-4">
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#landscapes" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full" :tattoos="landscape_images" :slide_speed="3500" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#squares" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full lg:w-1/2" :tattoos="square_images" :slide_speed="5000" />
        <CarouselV class="w-full lg:w-1/2" :tattoos="square_images_odd" :slide_speed="6500" />
      </div>
      <div class="flex flex-wrap flex-row justify-center items-center w-full rounded-3xl">
        <a href="#portraits" class="hidden w-0 h-0"></a>
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_1" :slide_speed="3500" />
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_2" :slide_speed="5000" />
        <CarouselV class="w-full lg:w-1/3" :tattoos="portrait_images_3" :slide_speed="6500" />
      </div>
    </div>
  </div>
</template>
