
export function getData(endpoint, callback) {
    const request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState === 4 && request.status === 200) {
        callback(request.responseText);
      }
    };
    request.open("GET", endpoint);
    request.send();
  }