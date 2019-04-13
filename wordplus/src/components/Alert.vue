<template>
  <div v-if="message" class="alert alert-warning alert-dismissible fade show" role="alert">
    <strong>{{message}}</strong>
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</template>

<script>
  export default {
    name: "Alert",
    props: ["message"]
  }
</script>
