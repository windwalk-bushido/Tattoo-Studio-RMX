<script>
import "vue3-carousel/dist/carousel.css";
import { Carousel, Slide } from "vue3-carousel";

export default {
  name: "CarouselV",

  components: {
    Carousel,
    Slide,
  },

  props: {
    tattoos: [],
    number_of_tattoos: Number,
    slide_speed: Number,
  },
};
</script>

<template>
  <div class="rounded-3xl p-4">
    <Carousel :autoplay="slide_speed" :transition="1500" :wrapAround="true" :mouseDrag="false" :snapAlign="'center'">
      <Slide v-for="tattoo in tattoos" :key="tattoo">
        <img :src="tattoo" alt="Image of the tattoo." class="w-full image-height rounded-3xl" />
      </Slide>
    </Carousel>
  </div>
</template>

<style scoped>
.image-height {
  height: 800px;
}
</style>
