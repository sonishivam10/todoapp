
<style>
.task {
  border-radius: 0px;
}
</style>
<template>

  <div class="columns ">
    <div class="column">

      <ul class="column is-6">
        <li class="field has-addons  " style="border-radius:0px">
          <div class="control is-expanded">
            <input v-model="newTask.name" placeholder="Add new task" class="input is-info is-large" />
          </div>
          <div class="control">
            <button class="button is-info is-large" @click.stop="save">
              <i class="fa fa-plus" />
            </button>
          </div>
        </li>
        <li v-for="task in tasks" v-bind:key="task.id" @click="select(task)" :class="['box','task','is-marginless',selectedClass(task),completedTaskClass(task)]">

          <div class="field is-grouped columns">
            <div class="field is-grouped column">
              <div class="control column is-1">
                <button class="button " @click="toggleCompletion(task)">
                  <i class="fa" :class="taskCompletionButtonClass(task)" />
                </button>
              </div>
              <div class="control column is-8">
                <input type="text" v-model="task.name" class="input  is-expanded" @click.stop="" v-if="modes.edit && isSelected(task)">
                <span class="is-size-4" v-else> {{task.name}}</span>
              </div>
              <!-- </div> -->
              <!--controls -->
              <div class="control is-pulled-right column is-3">
                <div class="buttons has-addons " v-if="isSelected(task)">
                  <!-- edit buttons -->
                  <div v-if="!modes.delete" class="control">
                    <button class="button " @click.stop="modes.edit=true" v-if="!modes.edit">
                      <i class="fa fa-edit" />
                    </button>
                    <!-- buttons -->
                    <div class="buttons has-addons " v-if="modes.edit">
                      <button class="button " @click.stop="cancelEdit">
                        <i class="fa fa-ban" />
                      </button>
                      <button class="button  is-primary" @click.stop="edit">
                        <i class="fa fa-save" />
                      </button>
                    </div>
                  </div>
                  <!-- delete button -->
                  <div v-if="!modes.edit" class="control">
                    <button class="button " v-if="!modes.delete">
                      <i class="fa fa-times" @click.stop="modes.delete=true" />
                    </button>
                    <!-- buttons -->
                    <div class="buttons has-addons " v-else>
                      <button class="button " @click.stop="modes.delete=false">
                        <i class="fa fa-ban" />
                      </button>
                      <button class="button  is-danger">
                        <i class="fa fa-trash" @click.stop="remove" />
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /controls -->
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  async mounted() {
    console.log("Component mounted.");
    await this.populateTasks();
    console.log("Running in ", process.env.NODE_ENV);
  },
  data() {
    return {
      API_ENDPOINT:
        window.location.hostname === "todovu.herokuapp.com"
          ? "https://todovu.herokuapp.com/api/tasks"
          : "/api/tasks",
      modes: {
        edit: false,
        delete: false
      },
      tasks: [],
      newTask: {
        name: null
      },
      selectedTask: {}
    };
  },
  computed: {},
  methods: {
    taskCompletionButtonClass(t) {
      return {
        "fa-check": t.completionDate,
        "fa-square": !t.completionDate
      };
    },
    isSelected: function(t) {
      return t.id === this.selectedTask.id;
    },
    cancelAllModes() {
      this.modes.delete = false;
      this.modes.edit = false;
    },
    completedTaskClass: function(t) {
      if (t) return { "has-text-success": t.completionDate };
    },
    selectedClass: function(t) {
      if (t) return { "has-background-light	": t.id === this.selectedTask.id };
    },
    async populateTasks() {
      this.tasks = await this.readAll();
    },
    select: function(t) {
      this.cancelAllModes();
      this.selectedTask = t;
      console.log("Selected task: ", this.selectedTask);
    },
    async remove(e) {
      e.stopPropagation();
      const response = await axios.delete(
        this.API_ENDPOINT + "/" + this.selectedTask.id + "/"
      );
      if (response) await this.populateTasks();
      this.modes.delete = false;
    },
    async readAll() {
      var response = await axios.get(this.API_ENDPOINT + "/");
      return response.data;
    },
    async toggleCompletion(task) {
      var uri =
        this.API_ENDPOINT +
        "/" +
        task.id +
        (task.completionDate ? "/undone" : "/done");

      const response = await axios.put(uri);
      if (response) await this.populateTasks();
    },
    async save() {
      console.log(this.API_ENDPOINT, this.newTask);
      const response = await axios.post(this.API_ENDPOINT + "/", this.newTask);
      if (response) {
        await this.populateTasks();
        this.newTask.name = null;
      }
    },
    async edit() {
      const response = await axios.put(
        this.API_ENDPOINT + "/" + this.selectedTask.id + "/",
        this.selectedTask
      );
      if (response) {
        await this.populateTasks();
        this.modes.edit = false;
      }
    },
    async cancelEdit() {
      this.modes.edit = false;
      await this.populateTasks();
    }
  }
};
</script>
