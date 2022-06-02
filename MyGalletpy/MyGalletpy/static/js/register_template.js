function cambioPassword(){
    pwdInput = document.getElementById('f_password')
    rePwdInput = document.getElementById('f_rep_password')
    button = document.getElementById('btn_submit')

    if (pwdInput.value != rePwdInput.value){
       button.setAttribute('disabled','true')
    }else{
        button.removeAttribute('disabled')
    }
}