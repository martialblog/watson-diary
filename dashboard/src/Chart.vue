<script>
import { Radar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default Radar.extend({
  mixins: [ reactiveProp ],
  props: ['chartData', 'options'],
  mounted () {
    console.log(this.chartData)
    console.log(this.options)
    this.renderChart(this.chartData, this.options)
  }
})
</script>
