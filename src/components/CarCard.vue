<template>
    <div class="card">
        <img :src="photo" alt="Image of car" class="card-img-top">
        <div class="card-body d-flex flex-column">
            <div class="card-info">
                <p>{{`${year} ${make}`}}</p>
                <span class="price">
                    <span class="material-icons-outlined">local_offer</span>
                    {{`$${price}`}}
                </span>
            </div>
            <p>{{ model }}</p>
            <button class="btn btn-primary mt-auto" @click="viewDetails(id)">View more details</button>
        </div>
    </div>
</template>

<script>
export default {
    props: ['photo', 'year', 'make', 'model', 'id', 'price'],
    methods: {
        viewDetails(id){
            this.$router.push(`/cars/${id}`)
        }
    }
}
</script>

<style scoped>
.card{
    width: 300px;
    height: 400px;
}

.card-info{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
}

.price{
    display: flex;
    column-gap: 5px;
    background: #0eb881;
    color: #fff;
    padding: 3px;
    border-radius: 5px;
}



.btn{
    width: 100%;
    bottom: 0;
}

</style>