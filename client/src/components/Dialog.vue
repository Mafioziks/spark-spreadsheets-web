<template>
  <Button type="button"
          :button-type="buttonType"
          data-toggle="modal"
          :data-target="targetModal"
          v-bind:class="className"
  >
    <slot name="button">
      <Icon icon="bi-folder" /> Open File
    </slot>
  </Button>

  <teleport to="body">
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
  </teleport>
</template>

<script>
import Button from '@/components/Button'
import { computed } from 'vue'

export default {
  name: 'Dialog',
  components: { Button },
  props: {
    id: {
      type: String,
      default: 'modal'
    },
    buttonType: {
      type: String,
      default: 'primary'
    },
    className: {
      type: String
    }
  },
  setup (props) {
    const targetModal = computed(() => '#' + props.id)

    return { targetModal }
  }
}
</script>

<style scoped>

</style>
