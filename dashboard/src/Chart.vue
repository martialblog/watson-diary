<script>
import { Radar, mixins } from 'vue-chartjs'
const { reactiveProp } = mixins

export default Radar.extend({
  mixins: [ reactiveProp ],
  props: ['chartData', 'options'],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
})
</script>
