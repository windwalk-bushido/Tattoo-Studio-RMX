import { createApp } from "vue";
import router from "./router";

import axios from "axios";
import VueAxios from "vue-axios";

import App from "./App.vue";

import "./assets/tailwind.css";
import "./assets/index.css";

import { library } from "@fortawesome/fontawesome-svg-core";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { fas } from "@fortawesome/free-solid-svg-icons";
import { fab } from "@fortawesome/free-brands-svg-icons";
import { far } from "@fortawesome/free-regular-svg-icons";
library.add(fas, fab, far); // <FAIcon :icon="['fab', 'font-awesome']"/>

const app = createApp(App);
app.use(router);
app.use(VueAxios, axios);
app.component("FAIcon", FontAwesomeIcon);
app.mount("#app");
