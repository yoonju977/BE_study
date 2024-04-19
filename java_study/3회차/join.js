//제출 이벤트를 받는다
//제출되 입력 값들을 참조한다
//입력값에 문제가 있는 경우 이를 감지한다.
//가입 환영 인사를 제공한다

const form = document.getElementById("form")

form.addEventListener("submit", function (event) {

    event.preventDefault() //기존기능 차단, submit의 경우 리셋

    let userId = event.target.id.value //확인할 경우 console.log(값)
    let userPw1 = event.target.pw1.value
    let userPw2 = event.target.pw2.value
    let userName = event.target.name.value
    let userPhone = event.target.phone.value
    let userPosition = event.target.position.value
    let userGender = event.target.gender.value
    let userEmail = event.target.email.value
    let userIntro = event.target.intro.value

    console.log(userId, userPw1, userPw2, userName,
        userPhone, userPosition, userGender, userEmail, userIntro)


    if (userId.length < 6) {
        alert("아이디가 너무 짧습니다. 6자 이상 입력해주세요.")
        return; //submit 이벤트 강제 종료

    }

    if (userPw1 !== userPw2) {
        alert("비밀번호가 일치하지 않습니다")
        return;
    }

    document.body.innerHTML = ""
    document.write(`<p>${userId}님 환영합니다
    <br>
    회원 가입 시 입력하신 내역은 다음과 같습니다.<br>
    아이디 : ${userId}<br>
    이름 : ${userName}<br>
    전화번호 : ${userPhone}<br>
    원하는 직무 : ${userPosition}<\p>`)   //3회차 과제
})
