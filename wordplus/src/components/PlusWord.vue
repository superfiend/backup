<template>
  <div class="container well">
    <h5 class="page-header">添加单词</h5>
    <form class="container words" v-on:submit="plusWord">
      <div class="form-group">
        <label>单词</label>
        <input type="text" class="form-control" placeholder="word" v-model="word.word">
      </div>
      <div class="form-group">
        <label>词性</label>
        <input type="text" class="form-control" placeholder="type" v-model="word.type">
      </div>
      <div class="form-group">
        <label>翻译</label>
        <input type="text" class="form-control" placeholder="mean" v-model="word.mean">
      </div>
      <button type="submit" class="btn btn-default">添加</button>
    </form>
  </div>
</template>

<script>
  export default {
    name: "PlusWord",
    data() {
      return {
        word: {}
      }
    },
    methods: {
      plusWord(e) {
        this.$http.get('http://localhost:5000/word/plus/'
          + '?word=' + this.word.word
          + '&type=' + this.word.type
          + '&mean=' + this.word.mean
        ).then(
          function (response) {
            this.$router.push({path: '/', query: {'message': response.body}});
          }
        );
        e.preventDefault();
      }
    }
  }
</script>
