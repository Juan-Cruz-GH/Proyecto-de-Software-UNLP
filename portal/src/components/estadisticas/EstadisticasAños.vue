<template>
    <Line
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
    />
  </template>
  
  <script>
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale } from 'chart.js'
  
  ChartJS.register(Title, Tooltip, Legend, LineElement, LinearScale, PointElement, CategoryScale)
  
  export default {
    name: 'LineChart',
    components: { Line },
    props: {
      chartId: {
        type: String,
        default: 'line-chart'
      },
      datasetIdKey: {
        type: String,
        default: 'label'
      },
      width: {
        type: Number,
        default: 400
      },
      height: {
        type: Number,
        default: 400
      },
      cssClasses: {
        default: '',
        type: String
      },
      styles: {
        type: Object,
        default: () => {}
      },
      plugins: {
        type: Array,
        default: () => {}
      }
    },
    data() {
      return {
        chartData: {
          labels: [ 'January', 'February', 'March', 'April', 'May', 'June', 'July' ],
          datasets: [ { 
            label: 'Data One',
            data: [40, 39, 10, 40, 39, 80, 40],
            backgroundColor: '#f87979'
          } ]
        },
        chartOptions: {
          responsive: true,
          maintainAspectRatio: false
        }
      }
    }
  }
  </script>
  