<template>
  <div class="container">
    <h5 class="page-header">单词</h5>
    <table class="table table-striped">
      <thead>
      <tr>
        <td>单词</td>
        <td>词性</td>
        <td>翻译</td>
        <td></td>
      </tr>
      </thead>
      <tbody>
      <tr v-for="word in words">
        <td>{{word.word}}</td>
        <td>{{word.type}}</td>
        <td>{{word.mean}}</td>
        <td></td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
  export default {
    data() {
      return {words: []}
    },
    methods: {
      getWords() {
        this.$http.get('http://localhost:3000/words').then(
          function (response) {
            this.words = response.body
          }
        )
      }
    },
    created() {
      this.getWords()
    }
  }
</script>
