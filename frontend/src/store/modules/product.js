import axios from 'axios';

const state = {
  products: null,
  product: null
};

const getters = {
  stateProducts: state => state.products,
  stateProduct: state => state.product,
};

const actions = {
  async createProduct({dispatch}, product) {
    await axios.post('product/', product);
    await dispatch('getProducts');
  },
  async getProducts({commit}) {
    let {data} = await axios.get('product/');
    commit('setProducts', data);
  },
  async viewProduct({commit}, id) {
    let {data} = await axios.get(`product/${id}`);
    commit('getProduct', data);
  },
};

const mutations = {
  setProducts(state, products){
    state.products = products;
  },
  setProduct(state, product){
    state.product = product;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
