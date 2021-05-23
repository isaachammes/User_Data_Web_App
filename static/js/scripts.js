function getStatistics(requestOptions) {
    fetch('/get_statistics', requestOptions)
        .then(response => response.json())
        .then(json => console.log(json))
        .catch(error => console.log('Request Failed', error))
}

function handleSubmit() {
  let requestOptions

  if (document.getElementById('fileSubmission').files[0]) {
    let file = document.getElementById("fileSubmission").files[0]
    let formData = new FormData()
    console.log(file)
    formData.append("file", file)
    requestOptions = {method: "POST", body: formData}
  }
  else if (document.getElementById('textSubmission').value !== '') {
    let data = document.getElementById('textSubmission').value
    console.log(data)
    requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: data,
    }
  }

  getStatistics(requestOptions)
}

function isJsonString(str) {
  try {
      JSON.parse(str);
  } catch (e) {
      return false;
  }
  return true;
}