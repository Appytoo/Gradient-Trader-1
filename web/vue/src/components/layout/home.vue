<template lang='pug'>
  section.contain.grd-row
    .grd-row-col-2-8(v-html='left')
    .grd-row-col-2-8.txt--center
      img(src='https://cryptocurrencykb.com/wp-content/uploads/2019/05/Cryptocurrency-Wallpaper-1-1024x713.jpg')
      p
        em The most valuable commodity I know of is information.
</template>

<script>
import marked from '../../tools/marked';

const left = marked(`

## Gradient Trader

It is a Bitcoin trading bot and backtesting platform that
connects to popular Bitcoin exchanges. It is written in javascript
and runs on nodejs.

`);

export default {
  data: () => {
    return {
      left
    }
  }
}
</script>
