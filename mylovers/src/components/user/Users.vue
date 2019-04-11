<template>
  <!--唯一的根元素-->
  <div class="container" id="users">
    <!--添加成功或者失败时显示的提示内容-->
    <alert></alert>
    <!--用户信息页面的主体内容-->
    <div class="users container">
      <h4 class="page-header">动漫人物</h4>
      <table class="table table-striped">
        <thead>
        <tr>
          <td>姓名</td>
          <td>性别</td>
          <td>年龄</td>
          <td>来源</td>
          <td></td>
        </tr>
        </thead>
        <tbody>
        <tr v-for="user in users">
          <td>{{user.cname}}</td>
          <td>{{user.sex}}</td>
          <td>{{user.age}}</td>
          <td>{{user.source}}</td>
          <td></td>
        </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
  import Alert from "../Alert";

  export default {
    name: "users",
    data() {
      return {users: []}
    },
    methods: {
      getUsers: function () {
        this.$http.get('http://localhost:3000/users').then(
          function (response) {
            this.users = response.body;
          }
        )
      }
    },
    components: {'alert': Alert},
    created() {
      this.getUsers()
    }
  }
</script>
