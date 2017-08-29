function getData(term) {

    $.urlParam = function(name) {
	var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
	return decodeURIComponent(results[1]) || 0;
    }
    var myTerm = $.urlParam('term');
    var myString = 'term=' + myTerm;
    console.log(myString)

    $.ajax({
      url: './plotly.cgi',
      dataType: 'json',
      data: myString,
      success: function(data, textStatus, jqXHR) {
	processJSON(data);
      },
      error: function(jqXHR, textStatus, errorThrown){
    	alert("Faled to perform gene search! textStatus: (" + textStatus +
	  ") and errorThrown: (" + errorThrown + ")");
      }
    });
}


function processJSON(data) {

    var layout = {
     title: 'Chromosome Map',
       xaxis: {title: 'Base Pairs (bp)',
	       showgrid: false,
	       zeroline: false,
	},
       yaxis: {title: 'G Bands',
	       showgrid: false,
	       zeroline: false,
	       showline: false,
	       autotick: false,
	       showticklabels: false
	},
       barmode: 'stack',
       paper_bgcolor: 'rgba(0,0,0,0)',
       plot_bgcolor: 'rgba(0,0,0,0)',
       showlegend: false,
       height: 250,
       hovermode: 'closest'
   };
 
    // Generate the plots for plate depth:
     return Plotly.newPlot("graph", data.matches, layout);

    console.log(layout)


};



function getMyData(term) {

    $.urlParam = function(name) {
	var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
	return decodeURIComponent(results[1]) || 0;
    }
    var mySearchTerm = $.urlParam('term');
    var myStringTerm = 'term=' + mySearchTerm;

    $.ajax({
      url: './gauge.cgi',
      dataType: 'json',
      data: myStringTerm,
      success: function(data, textStatus, jqXHR) {
	processMyJSON(data);
      },
      error: function(jqXHR, textStatus, errorThrown){
    	alert("Faled to perform gene search! textStatus: (" + textStatus +
	  ") and errorThrown: (" + errorThrown + ")");
      }
    });
}


function processMyJSON(data) {
  // Enter a speed between 0 and 180
  var level = data.matches;

  // // Trig to calc meter point
  var degrees = 180 - level,
    radius = .5;
  var radians = degrees * Math.PI / 180;
  var x = radius * Math.cos(radians);
  var y = radius * Math.sin(radians);
  //
 // Path: may have to change to create a better triangle
  var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
   pathX = String(x),
    space = ' ',
    pathY = String(y),
    pathEnd = ' Z';
 var path = mainPath.concat(pathX,space,pathY,pathEnd);


  var data2 = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 28, color:'850000'},
    showlegend: false,
    name: 'significance',
    text: level,
    hoverinfo: 'text+name'},
  { values: [50/10, 50/10, 50/10, 50/10, 50/10, 50/10, 50/10, 50/10, 50/10, 50/10, 50],
  rotation: 90,
  text: ['PATHOGENIC!', 'Risk Factor', 'Drug Response', 'Association', 'Affects', 'Benign',
            'Protective', 'Uncertain', 'Not Provided', 'Other', ''],
  textinfo: 'text',
  textposition:'inside',
  marker: {colors:['rgb(204, 0, 0)', 'rgb(255, 51, 51)', 'rgb(255, 102, 102)',
                         'rgb(255, 153, 153)', 'rgb(255, 204, 204)', 'rgb(173, 235, 173)',
                         'rgb(51, 204, 51)', 'rgb(230, 230, 230)', 'rgb(191, 191, 191)',
			 'rgb(153, 153, 153)','rgba(255, 255, 255, 0)']},
  labels: ['PATHOGENIC!', 'Risk Factor', 'Drug Response', 'Association', 'Affects', 'Benign',
            'Protective', 'Uncertain', 'Not Provided', 'Other', ''],
  hoverinfo: 'label',
  hole: .5,
  type: 'pie',
  showlegend: false
}];
var layout = {
      shapes:[{
        type: 'path',
        path: path,
        fillcolor: '850000',
        line: {
          color: '850000'
        }
      }],
     title: '<b> Gauge</b> <br> Variant Signifiance',
     height: 500,
     width: 500,
     paper_bgcolor: 'rgba(0,0,0,0)',
     plot_bgcolor: 'rgba(0,0,0,0)',
     xaxis: {zeroline: false, showline: false,  showticklabels: false,
        showgrid: false, range:[-1, 1]},
     yaxis: {zeroline: false, showline: false, showticklabels:false,
        showgrid: false, range:[-1,1]}
   };

    // Generate the plots for plate depth:
  return Plotly.newPlot("graph3", data2, layout);
};


function start() {
	getData();
	getMyData();
}

window.onload = start;


