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
                    required
                />
            </div>
            <div class="form-field col">
                <label for="model">Model</label>
                <input 
                    type="text" 
                    name="model" 
                    id="model" 
                    v-model="model" 
                    required
                />
            </div>
            <div class="col">
              <button type="submit" class="submit-btn">Search</button>
            </div>
          </div>
      </form>
    </div>
    <div class="cards-view">
      <CarCard 
        :id="2"
        :make="'Telsa'"
        :model="'Model S'"
        :photo="'../uploads/car.jpg'"
        :price="'20,000'"
        :year="'2022'"
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
        }
    },
    methods: {
        async searchCars(){
            let res = await CarService.search(make, model)
            console.log(res)
            if(res?.errors){
                this.error = true
            } else {
                console.log(res)
                // this.$router.push("/login")
            }
        }
    }
}
</script>

<style scoped>

.search-bar{
  /* display: flex;
  align-items: center;
  justify-content: center; */
  width: 80%;
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
</style>