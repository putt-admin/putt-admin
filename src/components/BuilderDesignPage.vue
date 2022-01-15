<script>
import DesignComponents from "./DesignComponents.vue";

export default {
  components: {
    DesignComponents,
  },
};
</script>

<template>
  <section class="section">
    <div class="section-header">
      <h1>Design Page: {{ $route.params.pageName }}</h1>
    </div>

    <div class="section-body">
      <DesignComponents></DesignComponents>
    </div>
  </section>
</template>
