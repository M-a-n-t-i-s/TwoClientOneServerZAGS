import React from 'react';
import './App.css'


const App = () => {
    window.addEventListener("load",async ()=>{
        document.forms["bornForm"].style.display="none";
        document.forms["deathForm"].style.display="none";
        document.forms["marriageForm"].style.display="none";
        document.forms["divorceForm"].style.display="none";
        get("http://127.0.0.1:5000/death",death_row,".death")
        get("http://127.0.0.1:5000/born",born_row,".born")
        get("http://127.0.0.1:5000/marriage",marriage_row,".marriage")
        console.log('HEY')
        if ('serviceWorker' in navigator){
            try{
                 const reg = await navigator.serviceWorker.register('/sw.js')
                console.log("Service worker register success",reg)
            } catch (e) {
                console.log("Service worker register fail")
            }
        }
    })



    async function get (url, drow, class_table)  {
        // отправляет запрос и получаем ответ

        const response = await fetch(url, {
            method: "GET",

            headers: { 'Content-Type': 'application/json' }
        });

        // если запрос прошел нормально
        if (response.ok === true) {
            // получаем данные
            const data = await response.json();
            let rows = document.querySelector(class_table);
            data.forEach(line => {
                // добавляем полученные элементы в таблицу
                rows.append(drow(line));

            });
        }
        else {
            console.log("ERROR")
        }
    };
    async function getBorn(key,id) {

        const response = await fetch("http://127.0.0.1:5000/born/"+key+"/"+id+"/get", {
            method: "GET",
            headers: { 'Content-Type': 'application/json'  }
        });
        if (response.ok === true) {
            const born = await response.json();
            const form = document.forms["bornForm"];
            born.forEach(line => {
                // добавляем полученные элементы в таблицу
                form.elements["id"].value = line.id;
                form.elements["fio"].value = line.fio;
                form.elements["date"].value = line.date;
                form.elements["gender"].value = line.gender;
                form.elements["id_parents"].value = line.id_parents;

            });

        }
    }
    async function getDeath(key,id) {

        const response = await fetch("http://127.0.0.1:5000/death/"+key+"/"+id+"/get", {
            method: "GET",
            headers: { 'Content-Type': 'application/json'  }
        });
        if (response.ok === true) {
            const death = await response.json();
            const form = document.forms["deathForm"];
            death.forEach(line => {
                // добавляем полученные элементы в таблицу
                form.elements["id"].value = line.id;
              //  form.elements["fio"].value = line.fio;
                form.elements["date"].value = line.date;
                form.elements["place"].value = line.place;
                form.elements["description"].value = line.description;

            });

        }
    }
    async function getMarriage(key,id) {

        const response = await fetch("http://127.0.0.1:5000/marriage/"+key+"/"+id+"/get", {
            method: "GET",
            headers: { 'Content-Type': 'application/json'  }
        });
        if (response.ok === true) {
            const marriage = await response.json();
            const form = document.forms["marriageForm"];

            marriage.forEach(line => {
                // добавляем полученные элементы в таблицу
                console.log(line)
                form.elements["id"].value = line.id;
                form.elements["date"].value = line.date;
               // form.elements["date_divorce"].value = line.date_divorce;

            });

        }
    }
    function death_row(death) {
        console.log(death)
        const tr = document.createElement("tr");
        tr.setAttribute("death-rowid", death.id);

        const idTd = document.createElement("td");
        idTd.append(death.id);
        tr.append(idTd);

        const fioTd = document.createElement("td");
        fioTd.append(death.fio);
        tr.append(fioTd);

        const dateTd = document.createElement("td");
        dateTd.append(death.date);
        tr.append(dateTd);

        const placeTd = document.createElement("td");
        placeTd.append(death.place);
        tr.append(placeTd);

        const descriptionTd = document.createElement("td");
        descriptionTd.append(death.description);
        tr.append(descriptionTd);

        const linksTd = document.createElement("td");

        const editLink = document.createElement("a");
        editLink.setAttribute("data-id", death.id);
        editLink.setAttribute("style", "cursor:pointer;padding:15px;");
        editLink.append("Изменить");
        editLink.addEventListener("click", e => {

            e.preventDefault();
            getDeath('id',death.id);
            document.forms["deathForm"].style.display="block";
            document.forms["deathForm"].elements["flag"].value = 0;
        });
        linksTd.append(editLink);

        const removeLink = document.createElement("a");
        removeLink.setAttribute("data-id", death.id);
        removeLink.setAttribute("style", "cursor:pointer;padding:15px;");
        removeLink.append("Удалить");
        removeLink.addEventListener("click", e => {

            e.preventDefault();
            delete_method("death",death.id);
        });

        linksTd.append(removeLink);
        tr.appendChild(linksTd);

        return tr;
    }

    function born_row(born) {

        const tr = document.createElement("tr");
        tr.setAttribute("born-rowid", born.id);

        const idTd = document.createElement("td");
        idTd.append(born.id);
        tr.append(idTd);

        const fioTd = document.createElement("td");
        fioTd.append(born.fio);
        tr.append(fioTd);

        const dateTd = document.createElement("td");
        dateTd.append(born.date);
        tr.append(dateTd);

        const genderTd = document.createElement("td");
        genderTd.append(born.gender);
        tr.append(genderTd);

        const idParentsTd = document.createElement("td");
        idParentsTd.append(born.id_parents);
        tr.append(idParentsTd);

        const deathDTd = document.createElement("td");
        deathDTd.append(born.death_date);
        tr.append(deathDTd);

        const linksTd = document.createElement("td");

        const editLink = document.createElement("a");
        editLink.setAttribute("data-id", born.id);
        editLink.setAttribute("style", "cursor:pointer;padding:15px;");
        editLink.append("Изменить");
        editLink.addEventListener("click", e => {
            setVisibleForm('bornForm')
            e.preventDefault();
            getBorn('id',born.id);


        });
        linksTd.append(editLink);

        const removeLink = document.createElement("a");
        removeLink.setAttribute("data-id", born.id);
        removeLink.setAttribute("style", "cursor:pointer;padding:15px;");
        removeLink.append("Удалить");
        removeLink.addEventListener("click", e => {

            e.preventDefault();
            delete_method("born",born.id);
        });
        linksTd.append(removeLink);

        const deathLink = document.createElement("a");
        deathLink.setAttribute("data-id", born.id);
        deathLink.setAttribute("style", "cursor:pointer;padding:15px;");
        deathLink.append("Зарегистрировать смерть");
        deathLink.addEventListener("click", e => {
            setVisibleForm('deathForm')
            e.preventDefault();
           // submit_deathForm()
            document.forms["deathForm"].elements["id"].value=born.id;
            document.forms["deathForm"].elements["flag"].value = 1;

        });
        linksTd.append(deathLink);
        tr.appendChild(linksTd);

        return tr;
    }

    function marriage_row(marriage) {

        const tr = document.createElement("tr");
        tr.setAttribute("marriage-rowid", marriage.id);

        const idTd = document.createElement("td");
        idTd.append(marriage.id);
        tr.append(idTd);

        const fioHTd = document.createElement("td");
        fioHTd.append(marriage.fio_husband);
        tr.append(fioHTd);

        const fioWTd = document.createElement("td");
        fioWTd.append(marriage.fio_wife);
        tr.append(fioWTd);

        const dateTd = document.createElement("td");
        dateTd.append(marriage.date);
        tr.append(dateTd);

        const dateDTd = document.createElement("td");
        dateDTd.append(marriage.date_divorce);
        tr.append(dateDTd);

        const linksTd = document.createElement("td");

        const editLink = document.createElement("a");
        editLink.setAttribute("data-id", marriage.id);
        editLink.setAttribute("style", "cursor:pointer;padding:15px;");
        editLink.append("Изменить");
        editLink.addEventListener("click", e => {

            e.preventDefault();
            getMarriage('id',marriage.id);
            document.forms["marriageForm"].style.display="block";
        });
        linksTd.append(editLink);

        const removeLink = document.createElement("a");
        removeLink.setAttribute("data-id", marriage.id);
        removeLink.setAttribute("style", "cursor:pointer;padding:15px;");
        removeLink.append("Удалить");
        removeLink.addEventListener("click", e => {

            e.preventDefault();
            delete_method("marriage",marriage.id);
        });

        linksTd.append(removeLink);




        const divorceLink = document.createElement("a");
        divorceLink.setAttribute("data-id", marriage.id);
        divorceLink.setAttribute("style", "cursor:pointer;padding:15px;");
        divorceLink.append("Установить развод");
        divorceLink.addEventListener("click", e => {

            e.preventDefault();
            document.forms["divorceForm"].elements["id"].value=marriage.id;
            document.forms["divorceForm"].style.display="block";
        });

        const delDivorceLink = document.createElement("a");
        delDivorceLink.setAttribute("data-id", marriage.id);
        delDivorceLink.setAttribute("style", "cursor:pointer;padding:15px;");
        delDivorceLink.append("Удалить развод");
        delDivorceLink.addEventListener("click", e => {

            e.preventDefault();
            pushDivorce(marriage.id, 0);
            window.location.reload();
        });

        if (marriage.date_divorce==0 || marriage.date_divorce=='0' ||  marriage.date_divorce==null)
        {
            linksTd.append(divorceLink);
        }
        else {
            linksTd.append(delDivorceLink);
        }

        tr.appendChild(linksTd);




        return tr;
    }

    async function pushDivorce( marriage_id, date_divorce) {
        const response = await fetch("http://127.0.0.1:5000/marriage/" + marriage_id + "/edit/divorce", {
            method: "POST",
            headers: {"Accept": "application/json", "Content-Type": "application/json"},
            body: JSON.stringify({
                date_divorce: date_divorce
            })
        });

        if (response.ok === true) {
            const marriage = await response.json();
            reset("divorceForm");
            window.location.reload();
           // document.querySelector("tr[marriage-rowid='" + marriage.id + "']")
        }
    }
    async function delete_method(str,id) {
        const response = await fetch("http://127.0.0.1:5000/"+str+"/"+id+"/delete", {
            method: "DELETE",
            headers: { 'Content-Type': "application/json" }
        });
        if (response.ok === true) {

            const table = await response.json();
            //document.querySelector("tr["+str+"-rowid='" + id + "']").remove();;
            window.location.reload();

        }
    }

    async function createBorn(fio, date, gender, id_parents) {

        const response = await fetch("http://127.0.0.1:5000/born", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({
                fio: fio,
                date: date,
                gender: gender,
                id_parents: id_parents
            })
        });
        if (response.ok === true) {
            const born = await response.json();
            reset("bornForm");
            //document.querySelector(".born").append(born_row(born));
            window.location.reload();
        }
    }
    async function createDeath(id, date, place, description) {

        const response = await fetch("http://127.0.0.1:5000/death", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({
                id: id,
                date: date,
                place: place,
                description: description
            })
        });
        if (response.ok === true) {
            const death = await response.json();
            reset("deathForm");
            //document.querySelector(".death").append(death_row(death));
            window.location.reload();
        }
    }

    async function createMarriage(id_husband, id_wife, date) {

        const response = await fetch("http://127.0.0.1:5000/marriage", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({
                'id_husband': id_husband,
                "id_wife": id_wife,
                'date': date
            })
        });
        if (response.ok === true) {
            const marriage = await response.json();
            reset("marriageForm");
           // document.querySelector(".marriage").append(marriage_row(marriage));
            window.location.reload();
        }
    }

    async function editMarriage( marriage_id, id_husband, id_wife, date) {
        const response = await fetch("http://127.0.0.1:5000/marriage/" + marriage_id + "/edit", {
            method: "POST",
            headers: {"Accept": "application/json", "Content-Type": "application/json"},
            body: JSON.stringify({
                id_husband: id_husband,
                id_wife: id_wife,
                date: date
            })
        });
        if (response.ok === true) {
            const marriage = await response.json();
            reset("marriageForm");
           // document.querySelector("tr[marriage-rowid='" + marriage.id + "']").replaceWith(marriage_row(marriage));
            window.location.reload();
        }
    }


    async function editBorn(id, new_fio, new_date, new_gender, new_id_parents) {
        const response = await fetch("http://127.0.0.1:5000/born/"+id+"/edit", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({

                fio: new_fio,
                date: new_date,
                gender: new_gender,
                id_parents: new_id_parents
            })
        });
        if (response.ok === true) {
            const born = await response.json();
            reset("bornForm");
            //document.querySelector("tr[born-rowid='" + born.id + "']").replaceWith(born_row(born));
            window.location.reload();
        }
    }


    async function editDeath(death_id, new_date, new_place, new_description) {
        const response = await fetch("http://127.0.0.1:5000/death/"+death_id+"/edit", {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify({

                date: new_date,
                place: new_place,
                description: new_description
            })
        });

        if (response.ok === true) {
            const death = await response.json();
            reset("deathForm");

            window.location.reload();
        }
    }
    function reset(select_form) {
        const form = document.forms[select_form];
        form.reset();
        form.elements["id"].value = 0;
    }


    function submit_bornForm() {

    const form = document.forms["bornForm"];
    const id = form.elements["id"].value;
    const fio = form.elements["fio"].value;
    const date = form.elements["date"].value;
    const gender = form.elements["gender"].value;
    const id_parents = form.elements["id_parents"].value;
    if (id == 0)
        createBorn(fio,date,gender,id_parents);
    else
        editBorn(id,fio,date,gender,id_parents);
    };

    function submit_deathForm() {

        const form = document.forms["deathForm"];
        const id = form.elements["id"].value;
        const flag = form.elements["flag"].value;
        const date = form.elements["date"].value;
        const place = form.elements["place"].value;
        const description = form.elements["description"].value;
        console.log("fdfdfdf", flag)
        if (flag == 1)
            createDeath(id, date, place, description);
        if (flag == 0)
           editDeath(id, date, place, description);
    };

    function submit_marriageForm() {

        const form = document.forms["marriageForm"];
        const id = form.elements["id"].value;
        const date = form.elements["date"].value;
        const id_husband = form.elements["id_husband"].value;
        const id_wife = form.elements["id_wife"].value;
        if (id == 0)
            createMarriage(id_husband, id_wife, date);
        else
            editMarriage(id, id_husband, id_wife, date);
    };
    function submit_divorceForm() {

        const form = document.forms["divorceForm"];
        const id = form.elements["id"].value;
        const date_divorce = form.elements["date_divorce"].value;

        pushDivorce(id, date_divorce);

    };

    function setVisibleForm(f){
        const form = document.forms[f];
        form.style.display="block";
    }
    function setNotVisibleForm(f){
        const form = document.forms[f];
        form.style.display="none";
    }
    return (
        <div>
            <h1>Информационная система ЗАГСа (ZAGS)</h1>
                <form name="bornForm">
                    <input type="hidden" name="id" value="0"/>
                    <div className="form-group">
                        <label htmlFor="fio">Фамилия Имя Отчество:</label>
                        <input className="form-control" name="fio"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="date">Дата Рождения:</label>
                        <input className="form-control" name="date"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="gender">Пол:</label>
                        <input className="form-control" name="gender"/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="id_parents">ID родителей:</label>
                        <input className="form-control" name="id_parents"/>
                    </div>
                    <div className="panel-body">
                        <button type="submit" className="btn btn-sm btn-primary" onClick={(e) => submit_bornForm(e)}>Сохранить </button>
                        <button type="reset" className="btn btn-sm btn-primary" onClick={(e) => reset("bornForm")}>Сбросить</button>
                        <button className="btn btn-sm btn-primary" onClick={(e) =>  setNotVisibleForm("bornForm")}>Закрыть</button>
                    </div>
                </form>
            <form name="deathForm">
                <input type="hidden" name="id" />
                <input type="hidden" name="flag" />
                <div className="form-group">
                    <label htmlFor="date">Дата смерти:</label>
                    <input className="form-control" name="date"/>
                </div>
                <div className="form-group">
                    <label htmlFor="place">Место смерти:</label>
                    <input className="form-control" name="place"/>
                </div>
                <div className="form-group">
                    <label htmlFor="description">Описание:</label>
                    <input className="form-control" name="description"/>
                </div>
                <div className="panel-body">
                    <button type="submit" className="btn btn-sm btn-primary" onClick={(e) => submit_deathForm(e)}>Сохранить </button>
                    <button type="reset" className="btn btn-sm btn-primary" onClick={(e) => reset("deathForm")}>Сбросить</button>
                    <button className="btn btn-sm btn-primary" onClick={(e) =>  setNotVisibleForm("deathForm")}>Закрыть</button>
                </div>
            </form>

            <form name="marriageForm">
                <input type="hidden" name="id" value="0"/>
                <div className="form-group">
                    <label htmlFor="id_husband">ID мужа:</label>
                    <input className="form-control" name="id_husband"/>
                </div>
                <div className="form-group">
                    <label htmlFor="id_wife">ID жены:</label>
                    <input className="form-control" name="id_wife"/>
                </div>
                <div className="form-group">
                    <label htmlFor="date">Дата регистрации:</label>
                    <input className="form-control" name="date"/>
                </div>
                <div className="panel-body">
                    <button type="submit" className="btn btn-sm btn-primary" onClick={(e) => submit_marriageForm(e)}>Сохранить </button>
                    <button type="reset" className="btn btn-sm btn-primary" onClick={(e) => reset("marriageForm")}>Сбросить</button>
                    <button className="btn btn-sm btn-primary" onClick={(e) =>  setNotVisibleForm("marriageForm")}>Закрыть</button>
                </div>
            </form>
            <form name="divorceForm">
                <input type="hidden" name="id" value="0"/>
                <div className="form-group">
                    <label htmlFor="date_divorce">Дата развода:</label>
                    <input className="form-control" name="date_divorce"/>
                </div>
                <div className="panel-body">
                    <button type="submit" className="btn btn-sm btn-primary" onClick={(e) => submit_divorceForm(e)}>Установить </button>
                    <button type="reset" className="btn btn-sm btn-primary" onClick={(e) => reset("divorceForm")}>Сбросить</button>
                    <button className="btn btn-sm btn-primary" onClick={(e) =>  setNotVisibleForm("divorceForm")}>Закрыть</button>
                </div>
            </form>
            <br></br>
            <br></br>
                <div className="btns">
                    <button onClick={(e) => setVisibleForm('bornForm')}>Зарегистрировать рождение</button>
                    <button onClick={(e) => setVisibleForm('marriageForm')}>Зарегистрировать брак</button>
                </div>

                <h3> Рожденные </h3>
                <table className="table table-condensed table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Фамилия Имя Отчество</th>
                        <th>Дата рождения</th>
                        <th>Пол</th>
                        <th>ID родителей</th>
                        <th>Дата смерти (Если есть)</th>
                        <th></th>

                    </tr>
                    </thead>
                    <tbody className="born">
                    </tbody>
                </table>
                <h3> Умершие </h3>
                <table className="table table-condensed table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>Фамилия Имя Отчество</th>
                        <th>Дата смерти</th>
                        <th>Место смерти</th>
                        <th>Описание</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody className="death">
                    </tbody>
                </table>
                <h3> Браки </h3>
                <table className="table table-condensed table-striped table-bordered">
                    <thead>
                    <tr>
                        <th>ID</th>
                        <th>ФИО Мужа</th>
                        <th>ФИО Жены</th>
                        <th>Дата регистрации</th>
                        <th>Дата развода (Если есть)</th>
                        <th></th>

                    </tr>
                    </thead>
                    <tbody className="marriage">
                    </tbody>
                </table>
        </div>
    );
};

export default App;
