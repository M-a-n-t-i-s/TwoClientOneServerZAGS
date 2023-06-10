import React from 'react';
import './App.css'
import App from "./App";




const Auth = () => {
    async function getAuth(id,password) {
        const response = await fetch("https://127.0.0.1:5000/auth", {
            method: "POST",
            headers: {"Accept": "application/json", "Content-Type": "application/json"},
            body: JSON.stringify({
                user_id: id,
                password: password

            })
        });
        if (response.ok === true) {
            const auth = await response.json();
            if (auth.status == "ok") {
                sessionStorage.setItem("session", "true");
            } else {

                console.error("Wrong password or login")

            }

        }
    }
    window.addEventListener("load", async () => {
        //sessionStorage.setItem("session", "true");
        if (sessionStorage.getItem("session") === "true") {
            document.forms["authForm"].style.display = "none";
            document.forms["prog"].style.display = "block";


        } else {
            document.forms["authForm"].style.display = "block";
            document.forms["prog"].style.display = "none";
        }

    })


      function check(e) {
          //e.preventDefault();


          console.log('ff')


          let id;
          id = parseInt(document.forms["authForm"].elements["login"].value);
          let password = document.forms["authForm"].elements["password"].value;

          if (id===1 && password==="qwerty") {
              sessionStorage.setItem("session", "true");
              document.forms["authForm"].style.display = "none";
              document.forms["prog"].style.display = "block";
           }

          //location.reload();

           // getAuth(id, password).catch(console.log("NO")).then(()=> {
           //     sessionStorage.setItem("session", "true");
           //     document.forms["authForm"].style.display = "none";
           //     document.forms["prog"].style.display = "block";
           // })

      }


    return (
        <div>
            <form name="authForm">
                <h1>Авторизация</h1>
                <div className="form-group">
                    <label htmlFor="login">Логин</label>
                    <input type="number" className="form-control" name="login"/>
                    <label htmlFor="password">Пароль</label>
                    <input type="password" className="form-control" name="password"/>
                </div>
                <div className="btns">
                    <button onClick={(e) => {
                        check(e)
                    }}>Войти
                    </button>
                </div>
            </form>
            <form name="prog">
                <App/>
            </form>
        </div>
    )

}


export default Auth