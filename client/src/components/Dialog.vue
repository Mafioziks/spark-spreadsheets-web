<template>
<div class="modal" :id="id" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <slot name="header">
          <h5 class="modal-title">
            <slot name="title">Modal Title</slot>
          </h5>
        </slot>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <slot></slot>
      </div>
      <div class="modal-footer">
        <slot name="footer"></slot>
        <Button buttonType="secondary" data-dismiss="modal">Cancel</Button>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import Button from '@/components/Button'

export default {
  name: 'Dialog',
  components: { Button },
  props: {
    id: {
      type: String,
      default: 'modal'
    }
  },
  setup () {
  }
}
</script>

<style scoped>

</style>
