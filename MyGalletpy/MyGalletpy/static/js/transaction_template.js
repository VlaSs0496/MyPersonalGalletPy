function validacionPocket(){
    transactionType = document.getElementById('tr_type')
    selectionPocket = document.getElementById('tr_pocket')
    console.log(transactionType.value)

    if(transactionType.value == 'False'){
        selectionPocket.removeAttribute('disabled')
    }else{
        selectionPocket.setAttribute('disabled', 'true')
    }
}

function activador(){
    transactionType = document.getElementById('tr_type')
    selectionPocket = document.getElementById('tr_pocket')

    if(transactionType.value != 'Pocket') selectionPocket.removeAttribute('disabled')
}