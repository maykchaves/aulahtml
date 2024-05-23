function decimal_binario(numero){
    if(numero == 0){
       return "0";
    }
      binario =  "";
}



function teste_decimal_binario(){
    console.log("iniciando teste");
    resultado = decimal_binario(25);
    if(resultado == "11001"){
        console.log("passou no teste no decimal 25 e binario 11001");
    } else {
        console.log("falhou no teste no decimal 25 e binario 11001");
    }
}

resultado = decimal_binario (0);
  if(resultado == "0"){
  console.log ("passou o teste no deimal 0 e binario 0");

  }else{
     console.log ("falhou o teste no decimal 0 e binario 0");


  }






teste_decimal_binario();
