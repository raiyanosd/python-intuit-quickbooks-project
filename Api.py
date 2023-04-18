const axios = require("axios");

const options = {
  method: 'GET',
  url: 'https://voicerss-text-to-speech.p.rapidapi.com/',
  params: {
    key: 'undefined',
    src: 'Hello, world!',
    hl: 'en-us',
    r: '0',
    c: 'mp3',
    f: '8khz_8bit_mono'
  },
  headers: {
    'X-RapidAPI-Key': '484b0338e3msh49f1e230c88eb7cp10ad9fjsne635de0176c1',
    'X-RapidAPI-Host': 'voicerss-text-to-speech.p.rapidapi.com'
  }
};

axios.request(options).then(function (response) {
	console.log(response.data);
}).catch(function (error) {
	console.error(error);
});
