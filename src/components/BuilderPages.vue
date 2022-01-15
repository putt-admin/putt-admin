<script>
import PagesList from "./PagesList.vue";

export default {
  components: {
    PagesList,
  },
};
</script>

<template>
  <section class="section">
    <div class="section-header">
      <h1>Pages</h1>
    </div>

    <div class="section-body">
      <PagesList></PagesList>
    </div>
  </section>
</template>
