<template>
  <div>
    
  <section>
    <div v-for="product in products" :key="product.idx" class="products">
      <div class="card" style="width: 18rem;">
        <div class="card-body">
          <ul>
            <li><strong>제품:</strong> {{ product.title }}</li>
            <li><strong>브랜드:</strong> {{ product.brand }}</li>
            <li><strong>설명:</strong> {{ product.content }}</li>
            <li><strong>가격:</strong> {{ product.price }}</li>
            <p><router-link :to="{name: 'productions', params:{id: product.idx}}" class="btn btn-primary">상세 정보</router-link></p>

          </ul>
        </div>
      </div>
      <br/>
    </div>
  </section>
  <hr/><br/>
  <section>
        <h1>상품등록</h1>
        <hr/><br/>

        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="title" class="form-label">상품명:</label>
            <input type="text" name="title" v-model="form.title" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="brand" class="form-label">브랜드명:</label>
            <input type="text" name="brand" v-model="form.brand" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="content" class="form-label">본문:</label>
            <textarea
              name="content"
              v-model="form.content"
              class="form-control"
            ></textarea>
          </div>
          <div class="mb-3">
            <label for="price" class="form-label">가격:</label>
            <input type="text" name="price" v-model="form.price" class="form-control" />
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </section>

  </div>
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