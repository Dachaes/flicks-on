<template>
  <div class="container" v-if="movieStore.detailMovie.poster_path">
    <div class="movie">
      <img class="movie-poster" :src="movieStore.detailMovie.poster_path" alt="poster">
      <div class="movie-rating">
        <img class="movie-heart" src="@/assets/likes/heart2.png" alt="likes">
        <p class="movie-rate" >{{ movieStore.detailMovie.vote_average }} </p>
      </div>
    </div>

    <div class="movie-info">
      <div class="movie-title" v-if="movieStore.detailMovie.production_countries">
        <p class="title">{{ movieStore.detailMovie.title }}</p>
        <div class="original-title">
          <p>{{ movieStore.detailMovie.original_title }}, <span data-start="0" data-end="5">{{ movieStore.detailMovie.release_date }}</span></p>
        </div>
        <p class="runtime">{{ movieStore.detailMovie.runtime }}분 / {{ movieStore.detailMovie.production_countries[0].name }}</p>
        <span v-for="genre in movieStore.detailMovie.genres" :key="genre.id">
          <span class="genre">{{ genre.name }}</span>
        </span>
      </div>
      <div class="movie-detail">
        <p>{{ movieStore.detailMovie.overview }}</p>
      </div>
    </div>
  </div>

  <div v-else>
    <p>로딩중</p>
  </div>
</template>

<script setup>
  import { ref, onMounted } from 'vue'
  import { onBeforeRouteUpdate, useRouter } from 'vue-router'
  import { useMovieStore } from '@/stores/movies'
  
  const props = defineProps({
    tmdbId: String
  })

  const movieStore = useMovieStore()
  const router = useRouter()
  onMounted(() => {
    movieStore.getDetailMovie(props.tmdbId)
  })

  onBeforeRouteUpdate((to, from) => {
    movieStore.getDetailMovie(to.params.title)
  })

</script>

<style scoped>

  .container {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin: 20px auto;

  padding: 20px;
  background-color: rgb(20, 20, 20);
  border-radius: 10px;
  text-align: right;
  background-image: linear-gradient(0deg, rgb(20, 20, 20) 0%, #2d2d2d 50%, rgb(20, 20, 20) 100%);
}

.movie {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 0 20px;
}

.movie-poster {
  width: 300px;
  height: 450px;
  object-fit: contain;
  margin-right: 20px;
  margin-bottom: 20px; 
}

.movie-rating {  
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }

.movie-heart {
    width: 25px;
    height: 25px;
    margin: 6px 6px 17px;
  }

.movie-rate {
  font-size: 16px;
}

.movie-info {
  display: flex;
  flex-direction: column;
  width: 70%;
  padding: 0 20px 0 0;
}

@media (max-width: 768px) {
  .movie-info {
  display: none;
}
}

.movie-title {
  font-size: 40px;
  font-weight: bold;
  margin-bottom: 20px;
}

.title {
  margin-bottom: 5px;
}

.original-title {
  font-size: 20px;
  font-weight: normal;
  margin-bottom: 5px;
}

.runtime {
  font-size: 15px;
  font-weight: normal;
  margin-bottom: 5px;
}

.genre {
  font-size: 14px;
  font-weight: normal;

  margin-left: 10px;
  margin-bottom: 5px;
}

.movie-detail {
  font-size: 15px;
  font-weight: normal;
}
</style>