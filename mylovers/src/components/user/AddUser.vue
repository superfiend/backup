<template>
  <form action="#" class="container" @submit.stop="addUser">
    <div class="well">
      <h4 class="page-header">添加用户</h4>
      <div>
        <label>中文名</label>
        <input type="text" class="form-control" placeholder="cname" v-model="user.cname">
      </div>
      <div>
        <label>英文名</label>
        <input type="text" class="form-control" placeholder="ename" v-model="user.ename">
      </div>
      <div>
        <label>性别</label>
        <input type="text" class="form-control" placeholder="sex" v-model="user.sex">
      </div>
      <div>
        <label>年龄</label>
        <input type="text" class="form-control" placeholder="age" v-model="user.age">
      </div>
      <div>
        <label>来源</label>
        <input type="text" class="form-control" placeholder="source" v-model="user.source">
      </div>
      <!--提交按钮-->
      <div><input type="submit" value="添加" class="btn btn-default"></div>
    </div>
  </form>
</template>

<script>
  export default {
    data() {
      return {user: {}}
    },
    methods: {
      // 获取当前user的总数
      getCurrentUserSize() {
        this.$http.get('http://localhost:3000/uid').then(
          function (response) {
            this.user.id = response.body.userId;
          }
        )
      },
      // 设置当前user的总数
      setCurrentUserSize(size) {
        // noinspection JSIgnoredPromiseFromCall
        this.$http.post('http://localhost:3000/uid', {'userId': size});
      },
      // 向本地json-server接口添加数据
      addUser() {
        this.getCurrentUserSize();
        this.$http.post('http://localhost:3000/users', this.user).then(
          function (response) {
            this.$router.push('/');
            this.setCurrentUserSize(this.user.id + 1);
          }
        )
      }
    }
  }
</script>
