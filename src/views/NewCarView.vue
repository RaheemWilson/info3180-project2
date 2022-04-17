<template>
    <div class="new-car-container">
        <div class="new-car-content">
            <h1>Add New Car</h1>
            <NewCarForm />  
        </div>
    </div> 
</template>

<script>
import NewCarForm from '../components/NewCarForm.vue'
export default {
    components: { NewCarForm }
}
</script>

<style scoped>
.new-car-container{
    min-height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.new-car-content{
    width: 40%;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
}

</style>