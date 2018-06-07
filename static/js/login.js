var log = console.log.bind(console)

var e = function(sel) {
    return document.querySelector(sel)
}

var bindTab = function() {
    var tab = e('.lg-tab')
    // log('tab1', tab)
    tab.addEventListener('click', function(event) {
        // log('dianji tab')
        var blue = e('.blue')
        var self = event.target
        var login = e('#id-div-login')
        var signup = e('#id-div-signup')
        if (self.id == 'id-tab-signup') {
            blue.classList.remove('blue')
            self.classList.add('blue')
            signup.classList.remove('none')
            login.classList.add('none')
        }else if (self.id == 'id-tab-login') {
            blue.classList.remove('blue')
            self.classList.add('blue')
            login.classList.remove('none')
            signup.classList.add('none')
        }
    })
}

// var loadTodos = function() {
//     var s = localStorage.savedTodos
//     // log('ll', s)
//     if (s == undefined) {
//         var s = []
//         return s
//     }else {
//         var ts = JSON.parse(s)
//         return ts
//     }
// }
//
// var saveTodo = function(todo) {
//     var todos = loadTodos()
//     todos.push(todo)
//     var s = JSON.stringify(todos)
//     localStorage.savedTodos = s
// }
// // 登录已有帐号
// var todoCheck = function(username, password) {
//         var todos = loadTodos()
//         for (var i = 0; i < todos.length; i++) {
//             var t = todos[i]
//             if (username == t.username && password == t.password) {
//                 alert('登陆成功')
//                 return true
//             }
//         }
//         alert('用户名或密码错误')
//         return false
// }
//
// // 检查是否有数字
// var numCheck = function(s) {
//     var num = '0123456789'
//     for (var i = 0; i < s.length; i++) {
//         ts = s[i]
//         if (num.includes(ts)) {
//             return true
//         }
//     }
//     return false
// }
// // 检查是否存在字母
// var letterCheck = function(s) {
//     var letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     for (var i = 0; i < s.length; i++) {
//         ts = s[i]
//         if (letter.includes(ts)) {
//             return true
//         }
//     }
//     return false
// }
//
// var usernameCheck = function(input) {
//     var s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     var letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
//     // var username = e('#id-input-signup-username')
//     if (input.length < 6) {
//         alert('用户名长度不足')
//         return false
//     }
//     // value = username.value
//     for (var i = 0; i < input.length; i++) {
//         // log('*****loop')
//         var index = s.includes(input[i])
//         var star = letter.includes(input[0])
//         if (index == false || star == false) {
//             alert('用户名不合法')
//             return false
//         }
//     }
//     // log('用户名格式正确')
//     return true
// }
//
// // 用户名注册检测
// var signupCheck = function(username) {
//     var todos = loadTodos()
//     for (var i = 0; i < todos.length; i++) {
//         var t = todos[i]
//         if (username == t.username) {
//             alert('用户名已存在')
//             return false
//         }
//     }
//     usernameCheck(username)
//     return true
// }
//
// var passwordCheck = function(input) {
//     if (input.length < 6) {
//         alert('密码长度不足')
//         return false
//     }
//     var s1 = numCheck(input)
//     var s2 = letterCheck(input)
//     if (s1 == true && s2 == true) {
//         log('密码格式合格')
//         return true
//     }
//     alert('密码格式错误')
//     return false
// }
//
// var passwordConfirm = function(input) {
//     var password1 = e('#id-input-signup-password')
//     var p1 = password1.value
//     if (p1 == input) {
//         return true
//     }
//     alert('两次输入不一致')
//     return false
// }
//
// var nicknameCheck = function(input) {
//     var space = ' '
//     if (input.length == 0) {
//         alert('用户名不合法')
//         return false
//     }
//     var todos = loadTodos()
//     for (var i = 0; i < todos.length; i++) {
//         var t = todos[i]
//         if (input == t.nickname) {
//             alert('昵称已存在')
//             return false
//         }
//     }
//     for (var i = 0; i < input.length; i++) {
//         var s = input[i]
//         if (space.includes(s)) {
//             alert('昵称不合法')
//             return false
//         }
//     }
//     // log('昵称可用')
//     return true
// }
//
//
//
// var bindSignup = function() {
//     var signupButton = e('#id-button-signup')
//     signupButton.addEventListener('click', function() {
//         // log('s')
//         var username = e('#id-input-signup-username')
//         u = username.value
//         var uc = signupCheck(u)
//         var nickname = e('#id-input-signup-nickname')
//         var n = nickname.value
//         var nc = nicknameCheck(n)
//         var password = e('#id-input-signup-password')
//         var p = password.value
//         var pc = passwordCheck(p)
//         var password2 = e('#id-input-signup-password2')
//         var p2 = password2.value
//         var confirm = passwordConfirm(p2)
//         if (uc && nc && pc && confirm) {
//             var todo = {
//                 username: u,
//                 nickname: n,
//                 password: p
//             }
//             saveTodo(todo)
//             alert('注册成功')
//         }
//     })
// }
//
// var bindLogin = function() {
//     var loginButton = e('#id-button-login')
//     loginButton.addEventListener('click', function() {
//         // log('l')
//         var username = e('#id-input-login-username')
//         u = username.value
//         var uc = usernameCheck(u)
//         var password = e('#id-input-login-password')
//         var p = password.value
//         if (uc) {
//             todoCheck(u, p)
//         }
//     })
// }


var __main = function() {
    bindTab()
    // bindSignup()
    // bindLogin()
}

$(document).ready(function(){
    __main()
})
