<template>
  <h1 v-if="responseCode">{{ errorStatement }}</h1>
  <div class="hello">
    <p>
    Temperature in Paris Ontario: {{temperature}} C<br>
    Pressure in Paris Ontario: {{pressure}} hpa<br>
    Humidity in Paris Ontario: {{humidity}}%<br>
    Wind Speed in Paris Ontario: {{windSpeed}} kn<br>
    </p>
  </div>
</template>

<script>
import axios from "axios";
let url = "https://api.openweathermap.org";
export default {
  name: "WeatherView",
  data: function() {
    return {
      responseCode: "",
      temperature: "",
      pressure: "",
      humidity: "",
      windSpeed: "",
      errorStatement: ""
    };
  },
  beforeMount(){
    this.getWeather("Paris, Ontario")
  },
  methods: {
    getWeather: function(inputTitle) {
      axios
        .get(
          url +
            "/data/2.5/weather?q=" +
            inputTitle +
            "&appid=24c9457a83864f3937717df4cbfca187&units=metric"
        )
        .then(response => {
          this.responseCode = response.cod
          if (this.responseCode === 404) {
            this.errorStatement = "Not Found";
          }
          this.temperature = response.data.main.temp;
          this.pressure = response.data.main.pressure;
          this.humidity = response.data.main.humidity;
          this.windSpeed = response.data.wind.speed;
        })
        .catch(error => {
          if (error) {
            this.errorStatement = "Error in finding this city!";
          }
        });
    }
  }
};
</script>