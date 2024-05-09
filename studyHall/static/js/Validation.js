function validateMobileNumber() {
              var a =document.getElementById("mobile").value;
              if (a==""){
                document.getElementById("message").innerHTML="**Please fill mobile number";
                return false;
              }
              if (isNaN(a)){
                 document.getElementById("message").innerHTML="** Enter only numeric value";
                 return false;
              }
              if (a.length<10){
                 document.getElementById("message").innerHTML="** Mobile number must be 10 digit";
                 return false;
              }
              if (a.length>10){
                 document.getElementById("message").innerHTML="** Mobile number must be 10 digit";
                 return false;
              }
              if ((a.charAt(0)!=9) && (a.charAt(0)!=8) && (a.charAt(0)!=7)){
                 document.getElementById("message").innerHTML="** Invalid mobile number";
                 return false;
              }
    }