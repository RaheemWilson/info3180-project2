<template>
<div class="card-container">
        <div class="card">
            <div class="row">
                <div class="col">
                    <img :src="`../../uploads/${car.photo}`" class="img-fluid rounded-start" alt="Car image">
                </div>
                <div class="col">
                    <div class="card-body d-flex flex-column h-100">
                        <h5 class="card-title">{{`${car.year} ${car.make}`}}</h5>
                        <h6 class="card-text text-muted">{{ car.model }}</h6>
                        <p class="card-text">{{ car.description }}</p>
                        <div>
                            <div class="row">
                                <p class="col">Color {{ car.colour }}</p>
                                <p class="col">Body Type {{ car.car_type }}</p>
                            </div>
                            <div class="row">
                                <p class="col">Price {{ car.price }}</p>
                                <p class="col">Transmission {{ car.transmission }}</p>
                            </div>
                        </div>
                        <div class="row mt-auto">
                            <div class="col">
                                <span class="email-btn"  role="button">Email Owner</span>
                            </div>
                            <div class="col d-flex" role="button" @click="handleAddFav(car.id)">
                                <span class="material-icons-outlined ms-auto favourite">favorite_border</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</div>
</template>

<script>
import CarService from '@/services/cars.service.js'
import TokenService from '@/services/token.service.js'
export default {

    data(){
        return {
            car: null,
            error: false,
            message: '',
            csrf: ''
        }
    },
    async beforeMount(){
        let res = await CarService.getCar(this.$route.params.id)

      if(res){
        this.car = {...res}
      } else {
        this.error = true
      }
    },
    methods: {
        async handleAddFav(id){
            let response = await TokenService.getCrsfToken()

            let res = await CarService.addFav(id, response.csrf_token)
             if(res){
                console.log(res)
            } else {
                this.error = true
            }
        }
    }
}
</script>

<style scoped>
.card-container{
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;

}
.card{
    max-width: 60%;
}

.email-btn{
    height: 44px;
    background: #0eb881;
    color: #fff;
    border-radius: 5px;
    padding: 10px 1rem;
    width: auto;
}

.favourite{
    color: #b80e0e;
    border: 1px solid #b80e0e;
    border-radius: 50%;
    padding: 10px;
}

</style>