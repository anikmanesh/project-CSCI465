var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

// var app4 = new Vue({
//   el: '#app-4',
//   data: {
//     todos: [
//       { text: 'Learn JavaScript' },
//       { text: 'Learn Vue' },
//       { text: 'Build something awesome' }
//     ]
//   }
// })

var app4 = new Vue({
  el: '#app-4',
  data: {
    suggestions: []
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchSuggestionList();
        this.timer = setInterval(this.fetchSuggestionList, 10000);
  },
  methods: {
    fetchSuggestionList: function() {
        axios
          .get('/suggestions/')
          .then(response => (this.suggestions = response.data.suggestions))
        console.log(this.suggestions)

    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
