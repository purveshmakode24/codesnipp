	// Your html file will be like this

	// <body>
	// <input id="num1" type="number" name="num1" placeholder="Enter number 1">
	// 	<select id="select">
 //  			<option value="add">Add</option>
 //  			<option value="sub">Sub</option>
 //  			<option value="div">Divide</option>
 //  			<option value="mul">Multiply</option>
	// 	</select>
	// <input id="num2" type="number" name="num2" placeholder="Enter number 2">
	
	// <button onclick="equalTo()">=</button>
	// <input id="ans" type="number" name="ans" readonly>
	// <body>



// Script for above markup

		function equalTo() {

			if(select.value==="add"){
				add();
			}else if(select.value==="sub"){
				sub();
			}else if (select.value==="mul"){
				mul();
			} else {
				div();
			}
		}


		function add() {
			var num1, num2, ans;
			num1 = Number(document.getElementById("num1").value);
			num2 = Number(document.getElementById("num2").value);
			ans= num1+num2;
			document.getElementById("ans").value=ans;
		}

		function sub() {
			var num1, num2, ans;
			num1 = Number(document.getElementById("num1").value);
			num2 = Number(document.getElementById("num2").value);
			ans= num1-num2;
			document.getElementById("ans").value=ans;
		}

		function mul() {
			var num1, num2, ans;
			num1 = Number(document.getElementById("num1").value);
			num2 = Number(document.getElementById("num2").value);
			ans= (num1*num2);
			document.getElementById("ans").value=ans;
		}

		function div() {
			var num1, num2, ans;
			num1 = Number(document.getElementById("num1").value);
			num2 = Number(document.getElementById("num2").value);
			ans= num1/num2;
			document.getElementById("ans").value=ans;
		}
		
