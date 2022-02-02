<template>
  <section>
    <div v-for="product in products" :key="product.idx" class="products">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <ul>
            <li><strong>제품:</strong> {{ product.title }}</li>
            <li><strong>브랜드:</strong> {{ product.brand }}</li>
            <li><strong>설명:</strong> {{ product.content }}</li>
            <li><strong>가격:</strong> {{ product.price }}</li>
          </ul>
        </div>
      </div>
      <br/>
    </div>
  </section>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'Product',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getProducts');
  },
  computed: {
    ...mapGetters({ products: 'stateProducts'}),
  },
  methods: {
    ...mapActions(['createProduct']),
    async submit() {
      await this.createProduct(this.form);
    },
  },
};
</script>