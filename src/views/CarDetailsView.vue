<template>
<div class="card-container">
        <div class="card">
            <div class="row">
                <div class="col">
                    <img src="../../uploads/car.jpg" class="img-fluid rounded-start" alt="Car image">
                </div>
                <div class="col">
                    <div class="card-body d-flex flex-column h-100">
                        <h5 class="card-title">{{`${year} ${make}`}}</h5>
                        <h6 class="card-text text-muted">{{ model }}</h6>
                        <p class="card-text">{{ description }}</p>
                        <div>
                            <div class="row">
                                <p class="col">Color {{ colour }}</p>
                                <p class="col">Body Type {{ type }}</p>
                            </div>
                            <div class="row">
                                <p class="col">Price {{ price }}</p>
                                <p class="col">Transmission {{ transmission }}</p>
                            </div>
                        </div>
                        <div class="row mt-auto">
                            <div class="col">
                                <span class="email-btn"  role="button">Email Owner</span>
                            </div>
                            <div class="col d-flex" role="button">
                                <span class="material-icons-outlined ms-auto favourite">favorite_border</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
</div>
</template>

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
}

</style>