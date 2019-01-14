<template>
<div class="pure-g">
  <div class="text-box pure-u-1 pure-u-md-1 pure-u-lg-1 pure-u-xl-1">
    <div class="l-box">
      <h1 class="text-box-head">Gallery</h1>
      <p class="text-box-subhead">subhead</p>
    </div>
  </div>

  <div v-for="image in images" :key="image.photo_id"
    class="photo pure-u-1-3 pure-u-md-1-3 pure-u-lg-1-3 pure-u-xl-1-3">
    <img v-bind:src="image_url_base + image.photo_id + '.' + image.type.split('/')[1]">
  </div>

  <div class="pure-u-1 form-box" id="upload-image">
    <div class="l-box">
      <h2>Upload a Photo</h2>
      <input v-on:change="onFileChange" type="file" name="file"
        placeholder="your photo" accept="image/*" required>
      <button v-on:click="uploadImage" class="pure-button pure-button-primary">Upload</button>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios';
import appConfig from '../config';

const API_BASE_URL = appConfig.ApiBaseUrl;
const IMAGE_BASE_URL = appConfig.ImageBaseUrl;

const imageData = {
  image_url_base: IMAGE_BASE_URL,
  uploadFile: null,
  images: [],
};

const uploadImage = async () => {
  const file = this.uploadFile;
  const router = this.$router;
  const data = { size: file.size, type: file.type };

  let json = null;

  await axios.post(`${API_BASE_URL}/images`, JSON.stringify(data)).then((res) => {
    json = JSON.parse(JSON.stringify(res.data));
  }).catch((error) => {
    // eslint-disable-next-line
    alert(error);
    // eslint-disable-next-line
    console.log(error);
  });

  await axios.put(json.signed_url, file, { headers: { 'Content-Type': file.type } }).then(() => {
    json.status = 'Uploaded';
  }).catch((error) => {
    // eslint-disable-next-line
    alert(error);
    // eslint-disable-next-line
    console.log(error);
  });

  await axios.put(`${API_BASE_URL}/images`, json).then(() => {
    // eslint-disable-next-line
    alert('Successfully uploaded photo.');
    router.go(router.currentRoute);
  }).catch((error) => {
    // eslint-disable-next-line
    alert(error);
    // eslint-disable-next-line
    console.log(error);
  });
};

export default {
  data: imageData,

  created: () => this.listImages(),

  methods: {
    listImages: () => { axios.get(`${API_BASE_URL}/images`).then((res) => { this.$data.images = res.Data; }); },
    onFileChange: (event) => { this.uploadFile = event.target.files[0]; },
    uploadImage,
  },
};
</script>

<style>
.header .pure-menu {
  border-bottom-color: black;
  border-radius: 0;
}

.pure-menu-link {
  padding: 1em 0.8em;
}

.text-box-head {
  color: #fff;
  padding-bottom: 0.2em;
  font-weight: 400;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 24px;
}

.text-box-subhead {
  font-weight: normal;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}

h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

.l-box {
  padding: 2em;
}

.text-box {
  text-align: left;
  overflow: hidden;
  position: relative;
  height: 180px;
  background: rgb(49, 49, 49);
  color: rgb(255, 190, 94);
}

.photo {
  height: 250px;
  overflow: hidden;
}

.photo img {
  max-width: 100%;
  min-height: 250px;
  height: auto;
}
</style>
