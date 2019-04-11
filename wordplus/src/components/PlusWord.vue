<template>
 <div class="container well">
   <h5 class="page-header">添加单词</h5>
   <form class="container words" v-on:submit="">
     <div class="form-group">
       <label>单词</label>
       <input type="text" class="form-control" placeholder="word">
     </div>
     <div class="form-group">
       <label>词性</label>
       <input type="text" class="form-control" placeholder="type">
     </div>
     <div class="form-group">
       <label>翻译</label>
       <input type="text" class="form-control" placeholder="mean">
     </div>
     <button type="submit" class="btn btn-default">添加</button>
   </form>
 </div>
</template>

<script>
  export default {
    name: "PlusWord"
  }
</script>
