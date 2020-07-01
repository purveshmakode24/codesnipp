var express = require('express');
const axios = require('axios');

var app = express();

app.get('/', (req, res)=> {
	res.send("Api data available at /api");
});

app.get('/api', function(req, res){

    axios.get(`https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=10`)
	.then(result=>{
	console.log(result.data);
	res.json(result.data)
	})
	.catch(err=> {
	console.log(err);
	})

});

app.listen(3000, ()=> {console.log("running at localhost:3000")});


