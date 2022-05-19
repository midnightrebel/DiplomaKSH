<style scoped>
form {
  display: block;
  height: 400px;
  width: 400px;
  background: #ccc;
  margin: auto;
  margin-top: 40px;
  text-align: center;
  line-height: 400px;
  border-radius: 4px;
}

progress {
  width: 400px;
  margin: auto;
  display: block;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>

<template>
  <div id="file-drag-drop-instant">
    <hr />
    <form id="drop-form-instant" @drop="handleFileDrop($event)">
      <span class="drop-files">Drop the files here!</span>
    </form>
    <progress max="100" :value.prop="uploadPercentage"></progress>
    <span v-show="uploadPercentage > 0"
      >Uploading {{ uploadPercentage }}%...</span
    >
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      dragAndDropCapable: false,
      files: [],
      uploadPercentage: 0,
    };
  },

  mounted() {
    this.dragAndDropCapable = this.determineDragAndDropCapable();
    if (this.dragAndDropCapable) {
      this.bindEvents();
    }
  },

  methods: {
    bindEvents() {
      [
        "drag",
        "dragstart",
        "dragend",
        "dragover",
        "dragenter",
        "dragleave",
        "drop",
      ].forEach(
        function (evt) {
          document.getElementById("drop-form-instant").addEventListener(
            evt,
            function (e) {
              e.preventDefault();
              e.stopPropagation();
            }.bind(this),
            false
          );
        }.bind(this)
      );
    },

    handleFileDrop(event) {
      for (let i = 0; i < event.dataTransfer.files.length; i++) {
        this.files.push(event.dataTransfer.files[i]);
      }

      this.submitFiles();
    },

    determineDragAndDropCapable() {
      var div = document.createElement("div");
      return (
        ("draggable" in div || ("ondragstart" in div && "ondrop" in div)) &&
        "FormData" in window &&
        "FileReader" in window
      );
    },

    submitFiles() {
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("files[" + i + "]", file);
      }
      axios
        .post("/generate/excel", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          onUploadProgress: function (progressEvent) {
            this.uploadPercentage = parseInt(
              Math.round((progressEvent.loaded / progressEvent.total) * 100)
            );
          }.bind(this),
        })
        .then(function () {
          console.log("SUCCESS!!");
        })
        .catch(function () {
          console.log("FAILURE!!");
        });
    },
  },
};
</script>
