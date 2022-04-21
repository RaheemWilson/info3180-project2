<template>
  <div class="about container">
    <h2>Explore</h2>
    <div class="search-bar">
      <form method="post" @submit.prevent="searchCars">
         <div class="row">
            <div class="form-field col">
                <label for="make">Make</label>
                <input 
                    type="text" 
                    name="make" 
                    id="make" 
                    v-model="make"
                />
            </div>
            <div class="form-field col">
                <label for="model">Model</label>
                <input 
                    type="text" 
                    name="model" 
                    id="model" 
                    v-model="model" 
                />
            </div>
            <div class="col">
              <button type="submit" class="submit-btn" @click="searchCars">Search</button>
            </div>
          </div>
      </form>
    </div>
    <div class="cards-view">
      <CarCard 
        v-for="car in cars"
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
</template>
<script>
import CarService from '@/services/cars.service.js'
import CarCard from '../components/CarCard.vue'
export default {
    components: { CarCard },
    data(){
        return {
            make: '',
            model: '',
            error: false,
            message: '',
            cars: []
        }
    },
    async beforeMount(){
      let res = await CarService.getAll()

      if(res){
        this.cars = [...res.data.slice(-3)]
      } else {
        this.error = true
        AuthService.handleLogout()
      }
    },
    methods: {
        async searchCars(){
            let res = await CarService.querySearch(this.make, this.model)
            if(res){
              this.error = false
              this.cars = [...res]
              console.log(res)
            } else {
              this.error = true
              AuthService.handleLogout()
            }
        }
    }
}
</script>

<style scoped>

.search-bar{
  margin: 0 auto;
  padding: 1rem 0;
  box-shadow: 10px 0 40px rgba(19, 19, 19, 0.1);
}

form{
  padding: 1rem;
}

input{
  display: block;
  border: 1px solid rgba(19, 19, 19, 0.1);
  border-radius: 5px;
}

.col{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
}

.submit-btn, input, textarea, select{
    width: 100%;
    height: 44px;
}

.submit-btn{
    border: none;
    border-radius: 5px;
    background: #0eb881;
    color: #ffffff;
}

.cards-view{
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: row;
  flex-wrap: wrap;
  gap: 2rem;
  margin: 4rem 0;
}
</style>