<template>
      <nav class="navbar navbar-default">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">动漫人物管理系统</a>
          </div>
          <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
              <li><router-link to="/">动漫人物</router-link></li>
              <li><router-link to="/about">关于我们</router-link></li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
              <li><router-link to="/user/add">添加用户</router-link></li>
            </ul>
          </div>
        </div>
      </nav>
</template>
