<template>
    <div class="car-form">
        <div v-if="error" class="error">Invalid information</div>
        <div class="alert alert-success" role="alert" v-if="message">{{ message }}</div>
        <form 
            @submit.prevent="addNewCar" 
            method="post" 
            enctype="multipart/form-data"
            id="carForm"
            ref="carForm"
        >
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
            </div>
            <div class="row">
                <div class="form-field col">
                    <label for="colour">Colour</label>
                    <input 
                        type="text" 
                        name="colour" 
                        id="colour" 
                        v-model="colour"
                        required
                    />
                </div>
                <div class="form-field col">
                    <label for="year">Year</label>
                    <input type="text" name="year" id="year" v-model="year" required/>
                </div>
            </div>
            <div class="row">
                <div class="form-field col">
                    <label for="price">Price</label>
                    <input 
                        type="number" 
                        min="1" 
                        step="any" 
                        name="price" 
                        id="price" 
                        v-model="price"
                        required
                    />
                </div>
                <div class="form-field col">
                    <label for="car_type">Car Type</label>
                    <select  name="cartype" id="cartype" v-model="cartype" required>
                        <option value="SUV">SUV</option>
                    </select>
                </div>
            </div>
            <div class="row">
                <div class="form-field col">
                    <label for="transmission">Transmission</label>
                    <select name="transmission" id="transmission" v-model="transmission" required>
                        <option value="Manual">Manual</option>
                        <option value="Automatic">Automatic</option>
                    </select>
                </div>
                <div class="col"></div>
            </div>
            <div class="form-field">
                <label for="description">Description</label>
                <textarea 
                    name="description" 
                    id="description" 
                    v-model="description" 
                    cols="30" 
                    rows="10"
                    required
                ></textarea>
            </div>
            <div class="form-field">
                <label for="photo">Upload photo</label>
                <input 
                    type="file" 
                    name="photo" 
                    id="photo" 
                    ref="photo" 
                    accept="image/png, image/jpg, image/jpeg"
                    @change="handleFileUpload"
                    required
                />
            </div>

            <button type="submit" class="submit-btn">Add New Car</button>
        </form>
    </div>
</template>

<script>
import CarService from '@/services/cars.service.js'
import AuthService from '@/services/auth.service.js'
import TokenService from '@/services/token.service.js'
import store from '@/store/store.js'
export default {
    data(){
        return {
            make: '',
            model: '',
            colour: '',
            year: '',
            price: null,
            cartype: '',
            transmission: '',
            description: '',
            photo: '',
            error: false,
            message: '',
            csrf: ''
        }
    },
    async created(){
        let res = await TokenService.getCrsfToken()
        this.csrf = res.csrf_token
    },
    methods: {
        handleFileUpload(){
            this.photo = this.$refs.photo.files[0]
        },
        async addNewCar(){
            let form = document.getElementById("carForm")
            let carInfo = new FormData(form)
            carInfo.append('user_id', store.getters.getUser || localStorage.getItem('id'))

            let res = await CarService.add(carInfo, this.csrf)
            console.log(res)
            if(res?.errors){
                this.error = true
                AuthService.handleLogout()
            } else {
                this.message = "Car was successfully added!"
                this.$refs.carForm.reset()
                // console.log(res)
                // this.$router.push("/login")
            }
        }
    }
}
</script>

<style scoped>
.car-form{
    padding: 0 2rem;
    width: 100%;
}

.car-form, input, textarea, select{
    border: 1px solid rgba(19, 19, 19, 0.1);
    border-radius: 5px;
}

input[type="file"]{
    border: none;
}

.form-field, .submit-btn{
    margin: 1rem 0;
}

input, textarea, select{
    display: block;
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