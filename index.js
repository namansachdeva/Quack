// Require modules
const express = require("express");
var ejs = require('ejs')
var bodyParser = require('body-parser')
var ps = require('python-shell')
const app = express();
app.set('port', 5000)

app.use(require('body-parser').urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.get('/', function(req, res){
	//res.render('form', {answer: "", paragraph: "", question: ""});
	res.render('form');
})

app.post('/predict',function(req, res){
	var mPara = req.body.para;
	var mQues = req.body.ques;
	
	// Run Python Script here

	let options = {
	  mode: 'text',
	  pythonPath: '/usr/bin/python3',
	  pythonOptions: ['-u'], // get print results in real-time
	  scriptPath: '.',
	  args: [mPara, mQues]
	};

	ps.PythonShell.run('script.py', options, function (err, results) {
		if (err) throw err;
	  	// results is an array consisting of messages collected during execution
	  	console.log('results: %j', results);
	  	//res.render('form', {answer: results[0], paragraph: mPara, question: mQues})
	  	res.send(results[0])
	});
})


//Start server
app.listen(app.get('port'), function() {
	console.log('server started.')
})