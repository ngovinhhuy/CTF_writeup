function verifyUsername(username) {
    if (username != "cookiehanhoan") {
        return false
    }
    return true
}
function reverseString(str) {
    if (str === "") {
        return ""
    } else {
        return reverseString(str.substr(1)) + str.charAt(0)
    }
}
function verifyPassword(password) {
    if (reverseString(password) != "dr0Wss@p3rucreSr3pus") {
        return false
    }
    return true
}
function verifyRole(role) {
    if (role.charCodeAt(0) != 64) {
    	console.log("0")
        return false;
    }
    //role(0)=64->@
    //role(1)=100->d
    //role(2)=109->m
    if ((role.charCodeAt(1) + role.charCodeAt(2) != 209) && (role.charCodeAt(2) - role.charCodeAt(1) != 9)) {
        return false
    }
    if ((role.charCodeAt(3).toString() + role.charCodeAt(4).toString() != "10578") && (role.charCodeAt(3) - role.charCodeAt(4) != 27)) {
        return false
    }
    //role(3)=105->i
    //role(4)=78->N
    return true
}