<script>
export default {
  name: "NavV",

  data() {
    return {
      menu_opened: false,
    };
  },

  methods: {
    ChangeMenuState() {
      this.menu_opened = !this.menu_opened;
    },
  },
};
</script>

<template>
  <div
    class="w-full rounded-tl-3xl rounded-tr-3xl group flex flex-col justify-between lg:w-16 lg:h-screen lg:rounded-tr-3xl lg:rounded-br-3xl z-10 fixed transition-all duration-150 ease-out lg:hover:w-96 bg-gray-800 text-white"
    :class="menu_opened ? 'w-screen h-screen' : 'h-12 bottom-0'"
  >
    <button class="w-full mt-2 opacity-60 text-2xl text-green-300 lg:hidden" @click="ChangeMenuState()">
      <FAIcon :icon="['fas', 'angles-up']" v-if="menu_opened == false" />
      <FAIcon :icon="['fas', 'angles-down']" v-else />
    </button>

    <div
      class="lg:flex flex flex-col justify-center items-center lg:group-hover:m-4 text-3xl font-bold"
      :class="menu_opened ? 'flex w-full p-4' : 'hidden'"
    >
      <a href="/">
        <img src="../assets/logo.jpg" class="w-full h-full rounded-full shadow-lg lg:p-2" />
      </a>
      <h3 class="mt-4 hidden group-hover:inline">Tattoo Studio Miloš</h3>
    </div>

    <FAIcon :icon="['fas', 'quote-right']" class="hidden lg:inline text-3xl group-hover:hidden text-green-400" />
    <FAIcon :icon="['fas', 'globe']" class="hidden lg:inline text-3xl group-hover:hidden text-green-400" />
    <FAIcon :icon="['fas', 'laptop-code']" class="hidden lg:inline text-3xl group-hover:hidden mb-3 text-green-400" />

    <div class="flex flex-col justify-center items-center w-full p-4 text-xl hidden group-hover:flex">
      <p class="text-center">“Show me a man with a tattoo and I'll show you a man with an interesting past”</p>
      <p class="mt-4 text-2xl font-medium">Jack London</p>
    </div>

    <div class="flex flex-row flex-wrap justify-center items-center m-4 text-lg hidden group-hover:flex">
      <div class="flex flex-col justify-center items-center w-full">
        <p>Let's do some cool tattoo!</p>
        <p>Schedule the visit via:</p>
      </div>
      <a
        href="https://www.facebook.com/milos.cvetkovic.12935"
        class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200"
      >
        <FAIcon :icon="['fab', 'facebook']" />
      </a>
      <a
        href="https://www.instagram.com/milos__tattoo/"
        class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200"
      >
        <FAIcon :icon="['fab', 'instagram']" />
      </a>
      <a
        href="mailto:melkior0103@gmail.com"
        class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200"
      >
        <FAIcon :icon="['fas', 'envelope']" />
      </a>
    </div>

    <div class="m-4 flex flex-wrap flex-col justify-center items-center hidden group-hover:flex">
      <p>2022.</p>
      <div class="flex flex-wrap flex-row justify-center items-center mt-2 text-sm">
        <p>Website by</p>
        <a
          href="https://milijan-mosic.surge.sh"
          class="ml-1 transition-all ease-in duration-150 text-green-500 hover:text-green-200"
          >Windwalk</a
        >
      </div>
    </div>
  </div>
</template>

<style scoped>
.show_menu {
  width: 100vh;
  height: 100vh;
}
</style>
