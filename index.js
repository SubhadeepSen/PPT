$(document).ready(function(){
  $("#upload").on('click', function(){
	$('#errorMessage').empty();
	$('#successMessage').empty();
	let typeOfXml = $('#typeOfXml').val();
	let files = $('#fileuploadForm')[0][1].files;
	if(files.length == 0){
		$('#errorMessage').append('<p class="-error">Please select file(s) to upload</p>');
		return;
	}
    let fileData = new FormData();
    for (let i = 0; i < files.length; i++) {
        fileData.append("files", files[i]);
    }    
    postFiles(fileData, typeOfXml);
  });
  
  $('input[type="file"]').change(function(e){
	  let files = e.target.files;
	  $('#filenames').empty();
	  for (let i = 0; i < files.length; i++) {
		  $('#filenames').append('<p class="-filename">' + files[i].name + '</p>');
	  }
  });
  
});

function postFiles(fileData, typeOfXml){
	$.ajax({
        type: "POST",
        url: "/upload/" + typeOfXml,
        dataType: "json",
        contentType: false, // Not to set any content header
        processData: false, // Not to process data
        data: fileData,
        success: function (result, status, xhr) {
        	handleResponse(xhr);
        },
        error: function (xhr, status, error) {
        	handleResponse(xhr);
        }
    });
}

function handleResponse(xhr){
	if(xhr.status == 200){
		displayMessage(xhr);
		$('#filenames > p').each(function(){
			$(this).removeClass('-filename').addClass('-success');
		});
	}else{
		displayError(xhr);
	}
}

function displayError(xhr){
	$('#errorMessage').append('<p class="-error">' + xhr.status + ': ' + xhr.responseText + '</p>');
}
function displayMessage(xhr){
	$('#successMessage').append('<p class="-success">' + xhr.status + ': ' + xhr.responseText + '</p>');
}