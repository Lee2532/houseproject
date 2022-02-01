import createPersistedState from "vuex-persistedstate";
import Vue from 'vue';
import Vuex from 'vuex';

import stores from './modules/stores';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    stores,
  },
  plugins: [createPersistedState()]
});
