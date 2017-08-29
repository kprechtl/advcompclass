Window.onload=function () {
   console.log("onload started");
   $("#stats_results").complete({
     source: "./statistics.cgi"
 });
};


$( function() {
  $("#accordion" ).accordion ({
      collapsible:true,
      width: 600,
  });
});


$( function() {
  $("#accordion2" ).accordion ({
      collapsible:true,
      width: 600,
  });
});


$( function() {
  $("#accordion3" ).accordion ({
      collapsible:true,
      width: 600,
  });
});

$( function() {
  $("#accordion4" ).accordion ({
      collapsible:true,
      width: 600,
  });
});



