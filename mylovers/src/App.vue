<template>
  <div id="app">
    <!--导航条-->
    <mynavbar></mynavbar>
    <!--路由页面-->
    <router-view/>
  </div>
</template>

<script>
  import MyNavBar from "./components/nav/MyNavBar";

  export default {
    name: 'App',
    components: {"mynavbar": MyNavBar}
  }
</script>
