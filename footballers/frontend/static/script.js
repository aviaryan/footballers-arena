// parse
$(document).ready(function(){

	// load initial data
	$.ajax({
		type: 'GET',
		url: '/api/players',
		dataType: 'json',
		success: function (data) {
			var list = data['footballers'];
			$.each(list, function(index, element) {
				// console.log(element);
				var fields = element.fields;
				$('tbody').append($('<tr>')
					.append($('<td>').append(element.pk))
					.append($('<td>').append(fields.name))
					.append($('<td>').append(fields.nationality))
					.append($('<td>').append(fields.club))
					.click(function(){
						window.location.href = '/profiles/' + element.pk;
					})
					);
			});
		}
	});

	// search handler
	$("#search_btn").click(function(){
		var term = $("#search")[0].value.toLowerCase();
		updateRows(term);
	});

	$("form").submit(function(e) { // needed as form submit causes reload
		e.preventDefault();
	});
});



function updateRows(term){
	var count = 0;
	$('tbody tr').each(function(i, row) {
		var row = $(row);
		var name = row.find('td')[1].innerHTML;
		// console.log(name);
		if (name.toLowerCase().search(term) > -1) {
			row.show();
			count += 1;
		} else {
			row.hide();
		}
	});
	$('#count')[0].innerHTML = count;
}
