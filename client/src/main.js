import 'babel-polyfill';
import axios from 'axios';
import Vue from 'vue';
import 'bulma';

import TasksListComponent from './components/TasksListComponent.vue'

window.axios = require('axios');

new Vue({
  el: '#app',

  components: {
    'app': TasksListComponent
  }
})
