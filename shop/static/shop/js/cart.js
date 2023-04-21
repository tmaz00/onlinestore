var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        // extract data from html by searching for data-{name_of_param} attributes
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        console.log('USER:', user)
        if (user === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else {
            updateUserOrder(productId, action)
        }
    })
}

function updateUserOrder(productId, action){
    console.log('User is logged in, sending data..')

    // url to send response
    var url = '/update_item'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action': action})
    })

    // return a promise (response after sending data to view)
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        // reload page to get new data passed in (and see it immediately)
        location.reload()
    })
}