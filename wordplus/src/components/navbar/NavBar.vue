<template>
  <header class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <h5 class="nav-brand">后台单词管理系统</h5>
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link">单词主页</router-link>
          </li>
          <li class="nav-item">
            <router-link to="#" class="nav-link">关于我们</router-link>
          </li>
        </ul>
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/word/plus" class="nav-link">添加单词</router-link>
        </li>
      </ul>
    </nav>
  </header>
</template>
