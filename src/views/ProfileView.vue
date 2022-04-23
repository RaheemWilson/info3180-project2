<template>
  <div class="profile container">
    <!-- <div> -->
        <div class="card" v-if="user">
            <div class="row">
                <div class="col-5 d-flex justify-content-center">
                    <img 
                      :src="`../../uploads/${user.photo}`" 
                      class="img-fluid profile-img" 
                      alt="User's profile"
                    >
                </div>
                <div class="col-7">
                    <div class="card-body">
                        <h5 class="card-title">{{ user.name }}</h5>
                        <h6 class="card-text text-muted">@{{ user.username }}</h6>
                        <p class="card-text text-muted">{{ user.biography }}</p>
                        <div>
                            <div class="row">
                                <p class="col-2">Email</p>
                                <p class="col">{{ user.email }}</p>
                            </div>
                            <div class="row">
                                <p class="col-2">Location</p>
                                <p class="col">{{ user.location }}</p>
                            </div>
                            <div class="row">
                                <p class="col-2">Joined</p>
                                <p class="col">{{ new Date(user.date_joined).toLocaleString('en-US', {}) }}</p>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    <!-- </div> -->
    <div class="favourite-container">
      <h1>Cars Favourited</h1>
        <div class="cards-view">
        <CarCard 
          v-for="car in favourites"
          :key="car.id"
          :id="car.id"
          :make="car.make"
          :model="car.model"
          :photo="`../uploads/${car.photo}`"
          :price="car.price"
          :year="car.year"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ProfileService from '@/services/profile.service.js'
import AuthService from '@/services/auth.service.js'
import store from '@/store/store'
import CarCard from '../components/CarCard.vue'
export default {
  components: { CarCard },
  data(){
    return {
      user: null,
      favourites: [],
      error: false,
      message: '',
    }
  },
  async beforeMount(){
    let id = store.getters.getUser || localStorage.getItem('id')
    let user = await ProfileService.getUser(id)
    if(user){
      this.user = {...user}
      console.log(user.photo)
      let favourites = await ProfileService.getFav(id)
      if(favourites){
        this.error = false
        this.favourites = [...favourites]
      }else{
        AuthService.handleLogout()
      }
    }else{
      AuthService.handleLogout()
    }

  }
}
</script>

<style scoped>
.profile{
  width: 70%;
  height: 100%;
}

@media screen and (max-width: 840px) {
  .profile{
    width: 100%;
  }
}
.favourite-container{
  margin: 2rem 0;
}

.favourite-container h1{
  margin: 1rem 0;
}
.cards-view{
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 2rem;
}


.card > .row{
  height: 100%;
  padding-top: 1rem;
}

.profile-img{
  width: 15rem;
  height: 15rem;
  border-radius: 50%;
}

</style>
