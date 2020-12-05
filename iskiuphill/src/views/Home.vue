<template>
  <div class="home">
    <Resorts/>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>ISkiUphill</strong> by Reedster LLC © 2020
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
// @ is an alias to /src
import Resorts from '@/components/Resorts.vue'

export default {
  name: 'home',
  components: {
    Resorts 
  }
}
</script>
