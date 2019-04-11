<template>
  <div id="app">
    <!--导航栏-->
    <mynavbar></mynavbar>
    <router-view/>
  </div>
</template>

<script>
  import NavBar from "./components/navbar/NavBar";

  export default {
    name: 'App',
    components: {'mynavbar': NavBar}
  }
</script>
