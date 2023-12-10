let editor;

window.onload = function() {
    editor = ace.edit("editor")
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
}


function changeLanguage() {

    let language = $("#languages").val();


    if(language == 'python')editor.session.setMode("ace/mode/python");
    else if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'java')editor.session.setMode("ace/mode/java");
}


function executeCode() {

    $.ajax({

        url: "compiler",

        method: "POST",
        

        data: {
            language: $("#languages").val(),
            code: editor.getSession().getValue()
        },
        

        success: function(response) {
            $(".output").text(response.output)
            $("#executiontime").text(response.result)
            $("#statusexecution").text(response.status)
        }
    })
}

function handleFileUpload() {
    // Mendapatkan elemen input file
    var fileInput = document.getElementById('file_input');
    
    // Membuat objek FormData untuk mengirim file
    var formData = new FormData();

    // Menambahkan file ke FormData
    formData.append('testcase_file', fileInput.files[0]);

    // Melakukan permintaan AJAX untuk mengirim FormData ke backend
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'upload_endpoint', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // Tanggapan dari server
            console.log(xhr.responseText);
        }
    };

    // Mengirim FormData
    xhr.send(formData);
}


