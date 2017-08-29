// this function executes our search via an AJAX call
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();

    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#gene_search').serialize();


    $.ajax({
        url: './final_search.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    // this will be used to keep track of row identifiers
    var next_row_num = 1;

    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
	var omim_link = 'https://www.omim.org/entry/' + item.omim_id;	
        var variation_link = '/kprecht2/final/snp_info.cgi?term=' + item.variation_name;

        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');

        // add the variation name column
        $('<a/>', { "text" : item.variation_name, "id": "var_name", "href": variation_link } ).appendTo('#' + this_row_id);

        // add the variant type column
        $('<td/>', { "text" : item.variant_type } ).appendTo('#' + this_row_id);
        
	// add the phenotype column
        $('<td/>', { "text" : item.phenotype } ).appendTo('#' + this_row_id);

        //add gene symbol column
        $('<td/>', { "text" : item.gene_symbol } ).appendTo('#' + this_row_id);

        //add clinical significance column
        $('<td/>', { "text" : item.significance } ).appendTo('#' + this_row_id);

        //add omim_id column
        $('<a/>', { "text" : item.omim_id, "href": omim_link  } ).appendTo('#' + this_row_id);

    });

    // now show the result section that was previously hidden
    $('#results').show();
}


// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });
});


// this function runs the autocomplete search

window.onload=function () {
   console.log("onload started");
   $("#tags").autocomplete({
     source: "./find_disease_names.cgi",
     minLength: 2,
    //make sure it puts the value in the search box
     select: function(event, ui) {
        event.preventDefault();
 },
    //look at the value when you hover over choices
    focus: function(event, ui) {
        event.preventDefault();
        $("#tags").val(ui.item.label)
},
     html: true
  });
};

