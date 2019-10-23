/* ***REFER THE FOLLOWING HTML***
<body>
	<form name="myForm" action="/action_page.php"
	onsubmit="return validateForm()" method="post">
	Name: <input type="text" name="fname">
	<input type="submit" value="Submit">
	</form>
</body>
*/
function validateForm() {
    var x = document.forms["myForm"]["fname"].value;
    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
}
