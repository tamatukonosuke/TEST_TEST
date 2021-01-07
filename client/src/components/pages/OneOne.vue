<template>
    <div>
        HedgeHog Page
        <div id="app">
            {{ info }}
        </div>
    </div>
</template>

<script>
import router from "../../router";
import axios from 'axios';
export default {
    name: "OneOne",
    data () {
    return {
      info: null
      }
    },
    mounted() {
        this.checkLoggedIn();
        this.get_ones();
    },
    methods: {
        checkLoggedIn() {
            this.$session.start();
            if (!this.$session.has("token")){
                router.push("/auth")
            }
        },
        get_ones() {
            //this.loading = true;
            //ここDjango側のポート番号を使う
            //ここでapi通信をしている
            //401だから認証されてないことが原因か？？
            axios.get('http://localhost:9000/api/ones/').then(response => (this.info = response)
            // eslint-disable-next-line
            ).catch(e => {
                 console.log(e)
            })
        }
    }
}
</script>