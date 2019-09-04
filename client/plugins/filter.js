import Vue from 'vue'
import moment from 'moment'

Vue.filter('dateFormat', function(dateValue) {
  if (!dateValue) return ''
  return moment(dateValue).format('YYYY年MM月DD日 HH時mm分ss秒')
})
