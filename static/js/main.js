let addButton = document.querySelector('#add-contact')
let addForm = document.querySelector('#add-contact-form')


addButton.addEventListener('click', function(event){
  if (addForm.style.display === 'none'){
    addForm.style.display = 'block'
    event.target.innerText = "Cancel"
  }
  else {
    addForm.style.display = 'none'
    event.target.innerText = "Add New Contact"
  }
})

let verifyButtons = document.querySelectorAll('.verify-button')

const csrftoken = Cookies.get('csrftoken');

for (let button of verifyButtons){
  document.addEventListener('click', function(event){
    let contactDiv = event.target.parentNode.parentNode
    let contactId = contactDiv.dataset.contactId
    fetch(`/contacts/${contactId}/verify`, {
      method:'POST',
      headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRFToken": csrftoken
  },
    credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {if (data.verified === 'true') {
      event.target.remove();
      icon = document.createElement('i')
      icon.classList.add("fa", "fa-check")
      contactDiv.firstElementChild.append(icon)
      }
    })
    
  })
}

