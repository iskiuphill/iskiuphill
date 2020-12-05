<template>
  <div id="app">
	<h1 class="title is-1">ISkiUphill</h1>
    <div id="nav">
      <router-link to="/">Resorts</router-link> |
      <router-link to="/about">About</router-link> |
      <!-- <router-link to="/faq">FAQ</router-link> | -->
      <a href='https://forms.gle/V4RQ1PuPnpe3EG5G6'>Submit New Resort</a>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
