function login() {
    event.preventDefault()
    var username = document.getElementById(username)
    var password = document.getElementById(password)
    if(username == undefined || password == undefined) {
        alert('Please try again!!!')
    }
}