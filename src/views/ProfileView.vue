<template>
  <div class="profile container">
    <div>
        <div class="card">
            <div class="row">
                <div class="col">
                    <img :src="`../../uploads/${user.photo}`" class="img-fluid rounded-start" alt="Car image">
                </div>
                <div class="col">
                    <div class="card-body d-flex flex-column h-100">
                        <h5 class="card-title">{{ user.name }}</h5>
                        <h6 class="card-text text-muted">@{{ user.username }}</h6>
                        <p class="card-text">{{ user.biography }}</p>
                        <div>
                            <div class="row">
                                <p class="col">Email</p>
                                <p class="col">{{ user.email }}</p>
                            </div>
                            <div class="row">
                                <p class="col">Location</p>
                                <p class="col">{{ user.location }}</p>
                            </div>
                            <div class="row">
                                <p class="col">Joined</p>
                                <p class="col">{{ new Date(user.date_joined).toLocaleString('en-US', {}) }}</p>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
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
    console.log(user)
    if(user){
      this.error = false
      this.user = {...user}
      let favourites = await ProfileService.getFav(id)
      if(favourites){
        this.error = false
        this.favourites = [...favourites]
      }else{
        this.error = true
      }
    }else{
      this.error = true
    }

  }
}
</script>

<style>
.cards-view{
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 2rem;
  margin: 4rem 0;
}
</style>
