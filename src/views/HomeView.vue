<script>
import { RouterLink } from "vue-router";
</script>

<template>
    <div class="home-container">
      <div class="row">
        <div class="col info">
          <div class="hero-content">
            <h1>
              Buy and Sell Cars Online
            </h1>
            <p>
              United Auto Sales provides the fastest, easiest, and most user friendly way 
              to buy or sell cars online. Find a great price on the Vehicle You Want.
            </p>
            <div>
              <RouterLink to="/register" class="register link">Register</RouterLink>
              <RouterLink to="/login" class="login link">Login</RouterLink>
            </div>
          </div>
        </div>
        <div class="col">
          <img src="@/assets/home.jpg" alt="Car on display">
        </div>
      </div>
    </div>
</template>

<style scoped>
.home-container{
  max-width: 100vw;
  margin: 0;
  padding: 0;
  margin-top: -1.2rem;
}

.row{
  max-width: 100%;
  margin: 0;
}

img{
  width: 100%;
  height: 100%;
}

.col{
  margin: 0;
  padding: 0;
}

.info{
  display: flex;
  align-items: center;
  justify-content: center;
}
.info h1{
  width: 80%;
}

.info p{
  padding-bottom: 24px;
}


.hero-content{
  width: 70%;
}

.link{
  height: 44px;
  padding: 16px 32px;
  border: 1px solid #0eb881;
  border-radius: 6px;
  text-decoration: none;
  margin-right: 12px;
}

.login{
  color: #0eb881;
}

.register{
  background: #0eb881;
  color: #fff;
}
</style>