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

});

