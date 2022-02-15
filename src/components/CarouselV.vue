<script>
export default {
  name: "CarouselV",
  props: {
    tattoos: [],
  },
};
</script>

<template>
  <div class="relative overflow-hidden transition duration-150 ease-out border-2 border-gray-800">
    <div class="flex flex-wrap justify-between items-center w-full h-screen text-2xl z-10">
      <button
        class="flex justify-center items-center w-16 h-16 p-4 m-4 rounded-full shadow-lg opacity-25 hover:opacity-100 transition duration-150 ease-out border-2 border-gray-800 bg-black text-white hover:bg-white hover:text-black"
      >
        <FAIcon :icon="['fas', 'arrow-left']" />
      </button>
      <button
        class="flex justify-center items-center w-16 h-16 p-4 m-4 rounded-full shadow-lg opacity-25 hover:opacity-100 transition duration-150 ease-out border-2 border-gray-800 bg-black text-white hover:bg-white hover:text-black"
      >
        <FAIcon :icon="['fas', 'arrow-right']" />
      </button>
    </div>

    <div class="absolute" v-for="tattoo in tattoos" v-bind:key="tattoo">
      <img :src="tattoo" alt="Image of the tattoo." class="w-full h-full" />
    </div>
  </div>
</template>
