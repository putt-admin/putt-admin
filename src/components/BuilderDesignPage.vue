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
      <div class="row">
        <div class="col-12 col-md-9 col-lg-9">
          <div class="card">
            <div class="card-body">This is some text within a card body.</div>
            <div class="card-body">This is some text within a card body.</div>
            <div class="card-body">This is some text within a card body.</div>
            <div class="card-body">This is some text within a card body.</div>
            <div class="card-body">This is some text within a card body.</div>
            <div class="card-body">This is some text within a card body.</div>

            <div class="card-footer">Footer Card</div>
          </div>
        </div>
        <div class="col-12 col-md-3 col-lg-3">
          <DesignComponents></DesignComponents>
        </div>
      </div>
    </div>
  </section>
</template>
