<script>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import store from '@/store/store';

export default {
  components: { AppHeader, AppFooter },
  beforeMount(){
    let auth = localStorage.getItem('authToken')
    let user = localStorage.getItem('id')

    if(auth){
      store.commit('setAuth', { auth: auth })
      store.commit('setUser', { user: user })
      window.history.pushState({}, "/explore")
      // this.$router.push("/explore")]
      console.log("Helllooooo")
    }
  }
}


</script>

<template>
  <AppHeader />

  <main>
    <RouterView />
  </main>
  
  <!-- <AppFooter /> -->
</template>

<style>
body {
  /* padding-top: 75px; */
  height: 100vh;
}

#app{
  /* position: relative; */
  height: 100%;
  min-height: 100%;
}

main{
  height: 100%;
  padding-top: 75px;
}

</style>