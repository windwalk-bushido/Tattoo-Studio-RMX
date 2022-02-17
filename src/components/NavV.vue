<script>
export default {
  name: "NavV",
};
</script>

<template>
  <div
    class="group flex flex-col justify-between w-16 h-screen rounded-tr-3xl rounded-br-3xl z-10 fixed shadow-lg transition-all duration-200 ease-out hover:w-96 bg-gray-800 text-white"
  >
    <div class="flex flex-col justify-center items-center m-2 group-hover:m-4 text-3xl font-bold">
      <a href="/">
        <img src="../assets/logo.jpg" class="w-full h-full rounded-full shadow-lg" />
      </a>
      <h3 class="mt-4 hidden group-hover:inline">Vanilla Studio</h3>
    </div>

    <FAIcon :icon="['fas', 'quote-right']" class="text-3xl group-hover:hidden text-green-400" />
    <FAIcon :icon="['fas', 'globe']" class="text-3xl group-hover:hidden text-green-400" />
    <FAIcon :icon="['fas', 'laptop-code']" class="text-3xl group-hover:hidden mb-3 text-green-400" />

    <div class="flex flex-col justify-center items-center w-full p-4 text-xl hidden group-hover:flex">
      <p class="text-center">“Show me a man with a tattoo and I'll show you a man with an interesting past”</p>
      <p class="mt-4 text-2xl font-medium">Jack London</p>
    </div>

    <div class="flex flex-row flex-wrap justify-center items-center m-4 text-lg hidden group-hover:flex">
      <div class="flex flex-col justify-center items-center w-full">
        <p>Let's do some cool tattoo!</p>
        <p>Schedule the visit via:</p>
      </div>
      <a href="#" class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200">
        <FAIcon :icon="['fab', 'facebook']" />
      </a>
      <a href="#" class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200">
        <FAIcon :icon="['fab', 'instagram']" />
      </a>
      <a href="#" class="m-4 text-3xl transition-all ease-in duration-150 text-green-500 hover:text-green-200">
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
