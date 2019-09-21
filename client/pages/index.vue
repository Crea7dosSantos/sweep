<template>
  <div class="contant">
    <v-app>
      <div class="holder">
        <div class="first" />
        <div class="second" />
        <div class="third" />
        <div class="txt">
          <div class="display-4">
            Sweep
          </div>
          <br>
          <div class="textcontainer">
            <button
              class="btn6"
              to
              @click="displaySigninView"
            >
              Let's start!!!
            </button>
          </div>
        </div>
      </div>
      <template>
        <AllModal />
      </template>
    </v-app>
  </div>
</template>

<script>
import AllModal from '~/components/AllModal'
import { mapActions } from 'vuex'

export default {
  components: {
    AllModal
  },
  methods: {
    ...mapActions('modal', ['setSigninView']),
    displaySigninView: function() {
      this.setSigninView()
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Bitter');

body {
  margin: 0;
  font-family: 'Bitter', serif;
  text-align: center;
}

.holder,
.first,
.second,
.third {
  height: 100vh;
  width: 100vw;
}

.first,
.second,
.third {
  position: absolute;
}

.second,
.third {
  opacity: 0;
}

.holder {
  height: 100vh;
  position: relative;
  z-index: 1;
}

.first {
  animation: first 10s infinite;
  background: linear-gradient(#5ff8ca, #60e08c);
  z-index: 10;
}

@keyframes first {
  0% {
    opacity: 1;
  }

  10% {
    opacity: 0.8;
  }

  20% {
    opacity: 0.6;
  }

  30% {
    opacity: 0.4;
  }

  40% {
    opacity: 0.2;
  }

  50% {
    opacity: 0.1;
  }

  60% {
    opacity: 0.2;
  }

  70% {
    opacity: 0.4;
  }

  80% {
    opacity: 0.6;
  }

  90% {
    opacity: 0.8;
  }

  100% {
    opacity: 1;
  }
}

.second {
  animation: second 10s infinite;
  animation-delay: 2s;
  background: linear-gradient(#19eaa6, #00a1f0);
  z-index: 20;
}

@keyframes second {
  0% {
    opacity: 0;
  }

  10% {
    opacity: 0.2;
  }

  20% {
    opacity: 0.4;
  }

  30% {
    opacity: 0.6;
  }

  40% {
    opacity: 0.8;
  }

  50% {
    opacity: 1;
  }

  60% {
    opacity: 0.8;
  }

  70% {
    opacity: 0.6;
  }

  80% {
    opacity: 0.4;
  }

  90% {
    opacity: 0.2;
  }

  100% {
    opacity: 0;
  }
}

.third {
  animation: third 10s infinite;
  animation-delay: 8s;
  background: linear-gradient(#aab7f8, #ff75c6);
  z-index: 30;
}

@keyframes third {
  0% {
    opacity: 0;
  }

  10% {
    opacity: 0.2;
  }

  20% {
    opacity: 0.4;
  }

  30% {
    opacity: 0.6;
  }

  40% {
    opacity: 0.8;
  }

  50% {
    opacity: 1;
  }

  60% {
    opacity: 0.8;
  }

  70% {
    opacity: 0.6;
  }

  80% {
    opacity: 0.4;
  }

  90% {
    opacity: 0.2;
  }

  100% {
    opacity: 0;
  }
}

.txt {
  margin-top: calc(50vh - 43px);
  position: absolute;
  width: 100%;
  z-index: 1000;
}

.display-4 {
  color: burlywood;
}

.btn6 {
  padding: 15px 100px;
  margin: 10px 4px;
  color: navajowhite;
  font-family: sans-serif;
  text-transform: uppercase;
  text-align: center;
  position: relative;
  text-decoration: none;
  display: inline-block;
}
.btn6 {
  border: 1px solid transparent;
  -webkit-transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
  transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
}

.btn6::before {
  content: '';
  position: absolute;
  left: 0px;
  bottom: 0px;
  z-index: -1;
  width: 0%;
  height: 1px;
  background: #fff;
  box-shadow: inset 0px 0px 0px #fff;
  display: block;
  -webkit-transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
  transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
}

.btn6:hover::before {
  width: 100%;
}

.btn6::after {
  content: '';
  position: absolute;
  right: 0px;
  top: 0px;
  z-index: -1;
  width: 0%;
  height: 1px;
  background: #fff;
  -webkit-transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
  transition: all 0.4s cubic-bezier(0.5, 0.24, 0, 1);
}
.btn6:hover::after {
  width: 100%;
}
.btn6:hover {
  border-left: 1px solid #fff;
  border-right: 1px solid #fff;
}
</style>
