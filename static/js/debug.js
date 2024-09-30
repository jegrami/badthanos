
import { getData } from "./request.js";

export class DebugForm {
    constructor() {
      this.debugCard = document.querySelector(".debug-card");
      this.form = this.debugCard.querySelector(".debug-form");
      this.clearButton = this.form.querySelector("button[data-action='clear']");
      this.clearButton.addEventListener("click", this.handleClearClick.bind(this));
      this.sendButton = this.form.querySelector("button[data-action='read']");
      this.sendButton.addEventListener("click", this.handleSendClick.bind(this));
  
      // Base API URL for random quotes
      this.baseApiUrl = "/api/quotes/random";
    }
  
    handleClearClick(event) {
      event.preventDefault();
      let code = this.debugCard.querySelector("code");
      code.innerText = "";
    }
  
    handleSendClick(event) {
      event.preventDefault();
      const input = document.querySelector(".debug-card input");
      const limit = input.value.trim()
  
      // Validate user input
      if (limit < 1 || limit > 3) {
        alert("Please enter a number between 1 and 3.");
        return;
      }
      const endpoint = `${this.baseApiUrl}/${limit}`;
      getData(endpoint, this.showResponse);
    }
  
    showResponse(responseText) {
      const debugCard = document.querySelector(".debug-card");
      let code = debugCard.querySelector("code");
  
      // Parse json data to extract only relevant fields
      const data = JSON.parse(responseText);
      let formattedResponse = ""
      data.forEach(item => {
          formattedResponse += `<div id='quote-block'>
              <p id='quote-text'>"${item.quote}"</p>
              <p id='quote-movie'>—"${item.movie}"</p>
              </div>`;
      });
  
      code.innerHTML = formattedResponse;
    }
  }
  

