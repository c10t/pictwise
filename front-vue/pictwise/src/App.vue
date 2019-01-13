<template>
  <div id="app">
    <div class="header">
      <div class="pure-menu pure-menu-horizontal">
        <a class="pure-menu-heading" href="">Gallery</a>
        <ul class="pure-menu-list">
          <li class="pure-menu-item pure-menu-selected">
            <a class="pure-menu-link" href="#">Home</a>
          </li>
          <li class="pure-menu-item">
            <a class="pure-menu-link" href="#upload-image">Upload</a>
          </li>
          <li class="pure-menu-item">
            <a class="pure-menu-link" href="#">Settings</a>
          </li>
          <li class="pure-menu-item">
            <a class="pure-menu-link" href="#">Login</a>
          </li>
        </ul>
      </div>
    </div>
    <router-view/>
    <div class="footer">piyo</div>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.footer {
  color: #FFFFFF;
  font-size: 87.5%;
  border-top: 1px solid #eee;
  margin-top: 1em;
  padding: 1em;
  background: rgb(49, 49, 49);
}
</style>
