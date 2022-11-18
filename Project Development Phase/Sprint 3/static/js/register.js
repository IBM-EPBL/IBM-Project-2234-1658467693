
function validateform() 
{  
var x=document.myform.email.value;
var num=document.myform.phnum.value; 
var num2=document.myform.phnum2.value;   
var atposition=x.indexOf("@");  
var dotposition=x.lastIndexOf(".");  
if (atposition<1 || dotposition<atposition+2 || dotposition+2>=x.length){  
  alert("Please enter a valid e-mail address \n atpostion:"+atposition+"\n dotposition:"+dotposition);  
  return false;  
  }
if (isNaN(num2)){  
    document.getElementById("phnum2").innerHTML="Enter Numeric value only";  
    return false;  
  }  
if (isNaN(num)){  
  document.getElementById("phnum").innerHTML="Enter Numeric value only";  
  return false;  
}
else{  
  return true;  
  }
}  
  