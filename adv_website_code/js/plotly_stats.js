function getData() {

    $.ajax({
      url: './stats_plotly.cgi',
      dataType: 'json',
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
       xaxis: {title: 'Chromosome Name',
	      showgride: false,
	},
       yaxis: {title: 'Number of Variants',
	       showgrid: true,
	},
       paper_bgcolor: 'rgba(0,0,0,0)',
       plot_bgcolor: 'rgba(0,0,0,0)',
       showlegend: false,
       height: 500,
       hovermode: 'closest'
   };
 
    // Generate the plots for plate depth:
     return Plotly.newPlot("graph2", data.matches, layout);

    console.log(layout)


};


window.onload=function() {
	getData();
};

