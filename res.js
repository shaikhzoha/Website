
function Validate()
{

	var s = new String();
	f = document.f1.fname.value; 
	e = document.f1.email.value; 
	p = document.f1.pword.value; 
	ph = document.f1.mno.value;

	if((f == "")||(f ==" "))

	{

		alert("Please enter Full Name!");

	}

	else if((e == "")||(e ==" ")||(!ValidateEmail(e)))

	{

		alert("Please enter a valid email!");
		ValidateEmail(e)


	}
	
	else if((p == "")||(p==" "))

	{

		alert("Please enter a valid password!");

	}

	else if((ph == "")||(ph ==" ")||(!ValidatePhone(ph)))

	{

		alert("Please enter a valid phone number!");
		ValidatePhone(ph)


	}


}

function ValidateEmail(e)

{

	if(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(f1.email.value))

	{

		return true;

	}

	else{

		return false;

	}

}

function ValidatePhone(ph)

{

	if(/^\d{10}$/.test(f1.Pno.value))

	{

		return true;

	}

	else

	{

		return false;

	}

}
function func2(){
	alert("reservation is completed...");
	
}