import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTabWidget, QListWidget, QListWidgetItem, \
    QLabel, QDialog, QFormLayout, QLineEdit, QTextEdit, QErrorMessage, QComboBox, QHBoxLayout

from server_connector import ServerConnector, SecurityError


class AuthorizationDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.id = None
        self.is_accepted = False
        self.setLayout(QVBoxLayout())
        self.id_field = QLineEdit()
        self.id_field.setPlaceholderText("Login ID")
        self.layout().addWidget(self.id_field)
        self.password_field = QLineEdit()
        self.password_field.setPlaceholderText("Password")
        self.password_field.setEchoMode(QLineEdit.Password)
        self.layout().addWidget(self.password_field)
        accept_button = QPushButton("OK")
        accept_button.clicked.connect(self.confirm)
        self.layout().addWidget(accept_button)

    @property
    def user_id(self):
        return self.id

    def confirm(self):
        try:
            self.id = int(self.id_field.text())
            self.is_accepted = True
        except ValueError:
            pass
        self.close()


class FindDeath(QDialog):
    def __init__(self, main_panel):
        super().__init__()
        self.new_key = None
        self.main_panel = main_panel
        self.is_accepted = False
        self.setWindowTitle("Поиск")
        self.resize(250, 150)
        self.setLayout(QVBoxLayout())
        self.combo = QComboBox()
        self.combo.addItems(['ID', "Место", "Дата"])
        self.layout().addWidget(self.combo)
        self.value_field = QLineEdit()
        self.layout().addWidget(self.value_field)
        find_button = QPushButton("Найти")
        find_button.clicked.connect(self.confirm)
        self.layout().addWidget(find_button)

    def confirm(self):
        try:
            self.is_accepted = True
            if self.combo.currentText() == 'Место':
                self.main_panel.update_find('place', self.value_field.text())
                self.new_key = 'place'
            elif self.combo.currentText() == 'Дата':
                self.main_panel.update_find('date', self.value_field.text())
                self.new_key = 'date'
            elif self.combo.currentText() == 'ФИО':
                self.main_panel.update_find('fio', self.value_field.text())
                self.new_key = 'fio'
            elif self.combo.currentText() == 'ID':
                self.main_panel.update_find('id', self.value_field.text())
                self.new_key = 'id'

        except ValueError:
            pass
        self.close()

    @property
    def value(self):
        return self.value_field.text()

    @property
    def key(self):
        return self.new_key


class FindBorn(QDialog):
    def __init__(self, main_panel):
        super().__init__()
        self.new_key = None
        self.main_panel = main_panel
        self.is_accepted = False
        self.setWindowTitle("Поиск")
        self.resize(250, 150)
        self.setLayout(QVBoxLayout())
        self.combo = QComboBox()
        self.combo.addItems(
            ['ID', "ФИО", "Пол", "Дата рождения", "ID родителей", "Дата смерти", "Место смерти"])
        self.layout().addWidget(self.combo)
        self.value_field = QLineEdit()
        self.layout().addWidget(self.value_field)
        find_button = QPushButton("Найти")
        find_button.clicked.connect(self.confirm)
        self.layout().addWidget(find_button)

    def confirm(self):
        try:
            self.is_accepted = True
            if self.combo.currentText() == 'Место смерти':
                self.main_panel.update_find_born('place', self.value_field.text())
                self.new_key = 'place'
            elif self.combo.currentText() == 'Дата рождения':
                self.main_panel.update_find_born('date', self.value_field.text())
                self.new_key = 'date'
            elif self.combo.currentText() == 'ФИО':
                self.main_panel.update_find_born('fio', self.value_field.text())
                self.new_key = 'fio'
            elif self.combo.currentText() == 'ID родителей':
                self.main_panel.update_find_born('id_parents', self.value_field.text())
                self.new_key = 'id_parents'
            elif self.combo.currentText() == 'ID':
                self.main_panel.update_find_born('id', self.value_field.text())
                self.new_key = 'id'
            elif self.combo.currentText() == 'Пол':
                self.main_panel.update_find_born('gender', self.value_field.text())
                self.new_key = 'gender'
            elif self.combo.currentText() == 'Дата смерти':
                self.main_panel.update_find_born('death_date', self.value_field.text())
                self.new_key = 'death_date'
        except ValueError:
            pass
        self.close()

    @property
    def value(self):
        return self.value_field.text()

    @property
    def key(self):
        return self.new_key


class FindMarriage(QDialog):
    def __init__(self, main_panel):
        super().__init__()
        self.new_key = None
        self.main_panel = main_panel
        self.is_accepted = False
        self.setWindowTitle("Поиск")
        self.resize(250, 150)
        self.setLayout(QVBoxLayout())
        self.combo = QComboBox()
        self.combo.addItems(
            ['ID Брака', "ФИО Мужа", "ФИО Жены", "Дата регистрации брака", "ID Мужа", "ID Жены", 'Дата равода'])
        self.layout().addWidget(self.combo)
        self.value_field = QLineEdit()
        self.layout().addWidget(self.value_field)
        find_button = QPushButton("Найти")
        find_button.clicked.connect(self.confirm)
        self.layout().addWidget(find_button)

    def confirm(self):
        try:
            self.is_accepted = True

            if self.combo.currentText() == 'Дата равода':
                self.main_panel.update_find_marriage('date_divorce', self.value_field.text())
                self.new_key = 'date_divorce'
            elif self.combo.currentText() == 'Дата регистрации брака':
                self.main_panel.update_find_marriage('date', self.value_field.text())
                self.new_key = 'date'
            elif self.combo.currentText() == 'ФИО Мужа':
                self.main_panel.update_find_marriage('fio_husband', self.value_field.text())
                self.new_key = 'fio_husband'
            elif self.combo.currentText() == 'ФИО Жены':
                self.main_panel.update_find_marriage('fio_wife', self.value_field.text())
                self.new_key = 'fio_wife'
            elif self.combo.currentText() == 'ID Брака':
                self.main_panel.update_find_marriage('id', self.value_field.text())
                self.new_key = 'id'

            elif self.combo.currentText() == 'ID Мужа':
                self.main_panel.update_find_marriage('id_husband', self.value_field.text())
                self.new_key = 'id_husband'
            elif self.combo.currentText() == 'ID Жены':
                self.main_panel.update_find_marriage('id_wife', self.value_field.text())
                self.new_key = 'id_wife'

        except ValueError:
            pass
        self.close()

    @property
    def value(self):
        return self.value_field.text()

    @property
    def key(self):
        return self.new_key


class ConfirmDialog(QDialog):
    def __init__(self, id, server: ServerConnector, win):
        super().__init__()
        self.id = id
        self.win = win
        self.server = server
        self.setWindowTitle("Подтверждение действия")
        self.resize(250, 150)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel(f"Вы действительно хотите удалить эту запись?"))
        yes_button = QPushButton('Да')
        no_button = QPushButton('Нет')
        yes_button.clicked.connect(self.delete)
        no_button.clicked.connect(self.close)
        self.layout().addWidget(yes_button)
        self.layout().addWidget(no_button)

    def delete(self):
        self.server.delete_death(self.id)
        self.close()
        self.win.close()


class ConfirmDialogBorn(ConfirmDialog):
    def delete(self):
        self.server.delete_born(self.id)
        self.close()
        self.win.close()


class ConfirmDialogMarriage(ConfirmDialog):
    def delete(self):
        self.server.delete_marriage(self.id)
        self.close()
        self.win.close()


class EditDeathDialog(QDialog):

    def __init__(self, data, server: ServerConnector):
        super().__init__()
        self.is_accepted = False
        self.setWindowTitle("Редактировать запись")
        self.resize(400, 200)
        self.id = data['id']
        self.server = server
        self.setLayout(QFormLayout())
        self.date_field = QLineEdit()
        self.layout().addRow("Дата смерти", self.date_field)
        self.date_field.setText(data['date'])
        self.place_field = QLineEdit()
        self.layout().addRow("Место", self.place_field)
        self.place_field.setText(data['place'])
        self.description_field = QTextEdit()
        self.layout().addRow("Описание", self.description_field)
        self.description_field.setText(data['description'])
        edit_button = QPushButton('Редактировать запись')
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton('Удалить запись')
        delete_button.clicked.connect(self.confirm_dialog)
        self.layout().addRow(delete_button, edit_button)

        if self.server.user_role == 'OPERATOR':
            edit_button.setVisible(False)
            delete_button.setVisible(False)

    def edit(self):
        self.server.edit_death(self.id, self.date_field.text(), self.place_field.text(),
                               self.description_field.toPlainText())
        self.close()

    def confirm_dialog(self):
        window = ConfirmDialog(self.id, self.server, self)
        window.exec()


# class Push_Death(QDialog):
#     def __init__(self, id, server: ServerConnector, data, win):
#         super().__init__()
#         self.id = id
#         self.win = win
#         self.data = data
#         self.server = server
#         self.setWindowTitle("Установка смерти")
#         self.resize(250, 150)
#         self.setLayout(QFormLayout())
#         self.death_field = QLineEdit()
#         self.layout().addRow("Укажите ID смерти из БД", self.death_field)
#         # if data['id_death']!=None:
#         #     self.death_field.setText(str(data['id_death']))
#         yes_button = QPushButton('Установить')
#         yes_button.clicked.connect(self.push_death)
#         self.layout().addWidget(yes_button)
#         no_button = QPushButton('Удалить')
#         no_button.clicked.connect(self.delete_death)
#
#         self.layout().addRow("", yes_button)
#
#         self.layout().addWidget(no_button)
#
#     def push_death(self):
#         self.server.edit_born_push_death(self.id, self.death_field.text())
#         self.close()
#         self.win.close()
#
#     def delete_death(self):
#         self.server.edit_born_push_death(self.id, '0')
#         self.close()
#         self.win.close()

class Push_Divorce(QDialog):
    def __init__(self, id, server: ServerConnector, data, win):
        super().__init__()
        self.id = id
        self.win = win
        self.data = data
        self.server = server
        self.setWindowTitle("Развод")
        self.resize(250, 150)
        self.setLayout(QFormLayout())
        self.divorce_field = QLineEdit()
        self.layout().addRow("Укажите дату развода", self.divorce_field)
        yes_button = QPushButton('Утвердить')
        yes_button.clicked.connect(self.push_divorce)
        self.layout().addWidget(yes_button)
        no_button = QPushButton('Удалить')
        no_button.clicked.connect(self.delete_divorce)
        self.layout().addRow("", yes_button)
        self.layout().addWidget(no_button)

    def push_divorce(self):
        self.server.edit_marriage_push_divorce(self.id, self.divorce_field.text())
        self.close()
        self.win.close()

    def delete_divorce(self):
        self.server.edit_marriage_push_divorce(self.id, '0')
        self.close()
        self.win.close()


class NewDeathDialog(QDialog):
    def __init__(self, id_death):
        super().__init__()
        self.is_accepted = False
        self.id_death = id_death
        self.setLayout(QFormLayout())
        self.setWindowTitle(f"Смерть {self.id}")
        self.date_field = QLineEdit()
        self.layout().addRow("Дата смерти", self.date_field)
        self.place_field = QLineEdit()
        self.layout().addRow("Место", self.place_field)
        self.description_field = QTextEdit()
        self.layout().addRow("Описание", self.description_field)
        accept_button = QPushButton("Добавить")
        accept_button.clicked.connect(self.confirm)
        self.layout().addRow('', accept_button)

    def confirm(self):
        self.is_accepted = True
        self.close()

    @property
    def id(self):
        return self.id_death

    @property
    def date(self):
        return self.date_field.text()

    @property
    def place(self):
        return self.place_field.text()

    @property
    def description(self):
        return self.description_field.toPlainText()


class EditBornDialog(QDialog):

    def __init__(self, data, server: ServerConnector):
        super().__init__()
        self.gender_field = None
        self.is_accepted = False
        self.setWindowTitle("Редактировать запись")
        self.resize(400, 200)
        self.data = data
        self.id = data['id']
        self.server = server
        self.setLayout(QFormLayout())
        self.fio_field = QLineEdit()
        self.layout().addRow("Фамилия Имя Отчество", self.fio_field)
        self.fio_field.setText(data['fio'])
        self.date_field = QLineEdit()
        self.layout().addRow("Дата рождения", self.date_field)
        self.date_field.setText(data['date'])
        self.combo = QComboBox()
        self.combo.addItems(
            ['Мужской', 'Женский'])
        self.combo.setCurrentText(data['gender'])
        self.layout().addRow("Пол", self.combo)
        self.id_parents_field = QLineEdit()
        self.layout().addRow("ID родителей", self.id_parents_field)
        self.id_parents_field.setText(str(data['id_parents']))
        edit_button = QPushButton('Редактировать запись')
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton('Удалить запись')
        delete_button.clicked.connect(self.confirm_dialog)
        push_death_button = QPushButton('Заявить о смерти')
        push_death_button.clicked.connect(self.addDeath)
        self.layout().addRow(delete_button, edit_button)
        self.layout().addRow('', push_death_button)
        if self.server.user_role == 'OPERATOR':
            edit_button.setVisible(False)
            delete_button.setVisible(False)

    def edit(self):
        if self.combo.currentText() == 'Мужской':
            self.gender_field = 'Мужской'
        else:
            self.gender_field = 'Женский'
        self.server.edit_born(self.id, self.fio_field.text(), self.date_field.text(), self.gender_field,
                              self.id_parents_field.text())
        self.close()

    def confirm_dialog(self):
        window = ConfirmDialogBorn(self.id, self.server, self)
        window.exec()

    def addDeath(self):
        adding_dialog = NewDeathDialog(self.id)
        adding_dialog.exec()
        if adding_dialog.is_accepted:
            self.server.add_death(adding_dialog.id, adding_dialog.date, adding_dialog.place, adding_dialog.description)


class EditMarriageDialog(QDialog):

    def __init__(self, data, server: ServerConnector):
        super().__init__()
        self.is_accepted = False
        self.setWindowTitle("Редактировать запись")
        self.resize(400, 200)
        self.data = data
        self.id = data['id']
        self.server = server
        self.setLayout(QFormLayout())
        self.id_husband_field = QLineEdit()
        self.layout().addRow("ID Мужа из Рождённых", self.id_husband_field)
        self.id_husband_field.setText(str(data['id_husband']))
        self.id_wife_field = QLineEdit()
        self.layout().addRow("ID Жены из Рождённых", self.id_wife_field)
        self.id_wife_field.setText(str(data['id_wife']))
        self.date_field = QLineEdit()
        self.layout().addRow("Дата регистрации брака", self.date_field)
        self.date_field.setText(data['date'])
        edit_button = QPushButton('Редактировать запись')
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton('Удалить запись')
        delete_button.clicked.connect(self.confirm_dialog)
        push_divorce_button = QPushButton('Заявить о расторжении брака')
        push_divorce_button.clicked.connect(self.push_divorce)
        self.layout().addRow(delete_button, edit_button)
        self.layout().addRow('', push_divorce_button)
        if self.server.user_role == 'OPERATOR':
            edit_button.setVisible(False)
            delete_button.setVisible(False)

    def edit(self):
        self.server.edit_marriage(self.id, int(self.id_husband_field.text()), int(self.id_wife_field.text()),
                                  self.date_field.text())
        self.close()

    def confirm_dialog(self):
        window = ConfirmDialogMarriage(self.id, self.server, self)
        window.exec()

    def push_divorce(self):
        window = Push_Divorce(self.id, self.server, self.data, self)
        window.exec()


class DeathListItem(QListWidgetItem):
    def __init__(self, death_dick):
        super().__init__()
        self.id = death_dick['id']
        self.data = death_dick
        self.setText(
            f"{death_dick['id']}".ljust(10) + f"{death_dick['fio']}".ljust(38) + f"{death_dick['date']}".ljust(
                30) + f"{death_dick['place']}".ljust(25) + f"{death_dick['description']}")


class BornListItem(QListWidgetItem):
    def __init__(self, born_dick):
        super().__init__()
        self.id = born_dick['id']
        self.data = born_dick

        text = f"{born_dick['id']}".strip().ljust(10 - len(str(born_dick['id']))) + f"{born_dick['fio']}".strip().ljust(
            82 - len(str(born_dick['fio']))) + f"{born_dick['date']}".strip().ljust(
            38 - len(str(born_dick['date']))) + f"{born_dick['gender']}".strip().ljust(
            30 - len(str(born_dick['gender']))) + f"{born_dick['id_parents']}".strip().ljust(
            35 - len(str(born_dick['id_parents']))) + f"{born_dick['death_date']}"

        self.setText(text)


class MarriageListItem(QListWidgetItem):
    def __init__(self, marriage_dick):
        super().__init__()
        self.id = marriage_dick['id']
        self.data = marriage_dick
        self.setText(
            f"{marriage_dick['id']}".ljust(10) + f"{marriage_dick['fio_husband']}".ljust(
                42) + f"{marriage_dick['fio_wife']}".ljust(42) + f"{marriage_dick['date']}".ljust(
                50) + f"{marriage_dick['date_divorce']}")


class Title_Born(QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.setText(
            "ID".ljust(10) + "ФИО".ljust(65) + "Дата рождения".ljust(30) + "Пол".ljust(25) + "ID родителей".ljust(
                20) + "Дата смерти (если умер)")


class Title_Death(QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.setText("ID".ljust(10) + "ФИО".ljust(65) + "Дата смерти".ljust(27) + "Место".ljust(25) + "Описание")


class Title_Marriage(QListWidgetItem):
    def __init__(self):
        super().__init__()
        self.setText("ID".ljust(10) + "ФИО Мужа".ljust(60) + "ФИО Жены".ljust(55) + "Дата регистрации брака".ljust(
            35) + "Дата Развода(если есть)")


class MainPanel(QTabWidget):
    def __init__(self, get_death, get_death_key, get_born, get_born_key, get_marriage, get_marriage_key, server):
        super().__init__()
        self.server = server
        self.get_death = get_death
        self.get_death_key = get_death_key
        self.get_born = get_born
        self.get_born_key = get_born_key
        self.get_marriage = get_marriage
        self.get_marriage_key = get_marriage_key
        self.death_table_widget = QListWidget()
        self.death_table_widget.itemDoubleClicked.connect(self.openDeathWindow)
        self.born_table_widget = QListWidget()
        self.born_table_widget.itemDoubleClicked.connect(self.openBornWindow)
        self.addTab(self.born_table_widget, "Рождённые")
        self.addTab(self.death_table_widget, "Умершие")
        self.marriage_table_widget = QListWidget()
        self.marriage_table_widget.itemDoubleClicked.connect(self.openMarriageWindow)
        self.addTab(self.marriage_table_widget, "Браки")
        self.find_table_widget = QListWidget()
        self.find_table_widget.itemDoubleClicked.connect(self.openDeathWindow)
        self.find_born_table_widget = QListWidget()
        self.find_born_table_widget.itemDoubleClicked.connect(self.openBornWindow)
        self.addTab(self.find_born_table_widget, "Результат поиска Рождённые")
        self.addTab(self.find_table_widget, "Результат поиска Умершие")
        self.find_marriage_table_widget = QListWidget()
        self.find_marriage_table_widget.itemDoubleClicked.connect(self.openMarriageWindow)
        self.addTab(self.find_marriage_table_widget, "Результат поиска Браки")

        self.update_data()

    def update_data(self):
        self.death_table_widget.clear()
        self.death_table_widget.addItem(Title_Death())
        for death in self.get_death():
            self.death_table_widget.addItem(DeathListItem(death))

        self.born_table_widget.clear()
        self.born_table_widget.addItem(Title_Born())
        for born in self.get_born():
            self.born_table_widget.addItem(BornListItem(born))

        self.marriage_table_widget.clear()
        self.marriage_table_widget.addItem(Title_Marriage())
        for marriage in self.get_marriage():
            self.marriage_table_widget.addItem(MarriageListItem(marriage))

    def update_find(self, key, value):
        self.find_table_widget.clear()
        self.find_table_widget.addItem(Title_Death())
        for death in self.get_death_key(key, value):
            self.find_table_widget.addItem(DeathListItem(death))

    def update_find_born(self, key, value):
        self.find_born_table_widget.clear()
        self.find_born_table_widget.addItem(Title_Born())
        for born in self.get_born_key(key, value):
            self.find_born_table_widget.addItem(BornListItem(born))

    def update_find_marriage(self, key, value):
        self.find_marriage_table_widget.clear()
        self.find_marriage_table_widget.addItem(Title_Marriage())
        for marriage in self.get_marriage_key(key, value):
            self.find_marriage_table_widget.addItem(MarriageListItem(marriage))

    def openDeathWindow(self):
        edit_dialog = EditDeathDialog(self.sender().selectedItems()[0].data, self.server)
        edit_dialog.exec()

    def openBornWindow(self):
        edit_dialog = EditBornDialog(self.sender().selectedItems()[0].data, self.server)
        edit_dialog.exec()

    def openMarriageWindow(self):
        edit_dialog = EditMarriageDialog(self.sender().selectedItems()[0].data, self.server)
        edit_dialog.exec()


class NewBornDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.is_accepted = False
        self.setLayout(QFormLayout())
        self.fio_field = QLineEdit()
        self.setWindowTitle("Новая запись")
        self.layout().addRow("Фамилия Имя Отчество", self.fio_field)
        self.date_field = QLineEdit()
        self.layout().addRow("Дата рождения", self.date_field)
        self.gender_field = QLineEdit()
        self.combo = QComboBox()
        self.combo.addItems(
            ['Мужской', 'Женский'])
        self.layout().addRow("Пол", self.combo)
        self.id_parents_field = QLineEdit()
        self.layout().addRow("ID родителей", self.id_parents_field)
        accept_button = QPushButton("Добавить")
        accept_button.clicked.connect(self.confirm)
        self.layout().addRow('', accept_button)

    def confirm(self):
        self.is_accepted = True
        if self.combo.currentText() == 'Мужской':
            self.gender_field = 'Мужской'
        else:
            self.gender_field = 'Женский'
        self.close()

    @property
    def fio(self):
        return self.fio_field.text()

    @property
    def date(self):
        return self.date_field.text()

    @property
    def gender(self):
        return self.gender_field

    @property
    def id_parents(self):
        return self.id_parents_field.text()


class NewMarriageDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.is_accepted = False
        self.setLayout(QFormLayout())
        self.id_husband_field = QLineEdit()
        self.setWindowTitle("Новая запись")
        self.layout().addRow("ID Мужа из Рождённых", self.id_husband_field)
        self.id_wife_field = QLineEdit()
        self.layout().addRow("ID Жены из Рождённых", self.id_wife_field)
        self.date_field = QLineEdit()
        self.layout().addRow("Дата регистрации брака", self.date_field)
        accept_button = QPushButton("Добавить")
        accept_button.clicked.connect(self.confirm)
        self.layout().addRow('', accept_button)

    def confirm(self):
        self.is_accepted = True

        self.close()

    @property
    def id_husband(self):
        return self.id_husband_field.text()

    @property
    def date(self):
        return self.date_field.text()

    @property
    def id_wife(self):
        return self.id_wife_field.text()


class MainWindow(QWidget):

    def __init__(self, server: ServerConnector):
        super().__init__()
        self.server = server
        self.server.add_view(self)
        self.setWindowTitle("Информационная система ЗАГС")
        self.setGeometry(700, 200, 950, 500)
        upper_box = QHBoxLayout()
        under_box = QHBoxLayout()
        central_box = QHBoxLayout()
        main_box = QVBoxLayout()
        self.add_born_button = QPushButton("Зарегистрировать рождение", self)
        self.add_born_button.clicked.connect(self.addBorn)
        upper_box.addWidget(self.add_born_button)
        self.add_marriage_button = QPushButton("Зарегистрировать брак", self)
        self.add_marriage_button.clicked.connect(self.addMarriage)
        upper_box.addWidget(self.add_marriage_button)

        self.find_born_button = QPushButton("Найти рождённого", self)
        self.find_born_button.clicked.connect(self.findBorn)
        central_box.addWidget(self.find_born_button)
        self.find_death_button = QPushButton("Найти умершего", self)
        self.find_death_button.clicked.connect(self.findDeath)
        central_box.addWidget(self.find_death_button)
        self.find_marriage_button = QPushButton("Найти Брак", self)
        self.find_marriage_button.clicked.connect(self.findMarriage)
        central_box.addWidget(self.find_marriage_button)
        self.main_panel = MainPanel(self.server.get_death, self.server.get_death_key, self.server.get_born,
                                    self.server.get_born_key, self.server.get_marriage, self.server.get_marriage_key,
                                    self.server)
        self.server.add_view(self.main_panel)
        under_box.addWidget(self.main_panel)
        main_box.addLayout(upper_box)
        main_box.addLayout(central_box)
        main_box.addLayout(under_box)
        self.setLayout(main_box)
        self.setLayout(under_box)
        self.update_data()

    def setEngineerMode(self):
        self.add_born_button.setVisible(True)
        self.add_marriage_button.setVisible(False)

    def setOperatorMode(self):
        self.add_born_button.setVisible(False)
        self.add_marriage_button.setVisible(False)

    def setAdministratorMode(self):
        self.add_born_button.setVisible(True)
        self.add_marriage_button.setVisible(True)

    def addBorn(self):
        adding_dialog = NewBornDialog()
        adding_dialog.exec()
        if adding_dialog.is_accepted:
            self.server.add_born(adding_dialog.fio, adding_dialog.date, adding_dialog.gender, adding_dialog.id_parents)

    def addMarriage(self):
        adding_dialog = NewMarriageDialog()
        adding_dialog.exec()
        if adding_dialog.is_accepted:
            self.server.add_marriage(adding_dialog.id_husband, adding_dialog.id_wife, adding_dialog.date)

    def findDeath(self):
        find_dialog = FindDeath(self.main_panel)
        find_dialog.exec()
        if find_dialog.is_accepted:
            self.server.get_death_key(find_dialog.key, find_dialog.value)

    def findBorn(self):
        find_dialog = FindBorn(self.main_panel)
        find_dialog.exec()
        if find_dialog.is_accepted:
            self.server.get_born_key(find_dialog.key, find_dialog.value)

    def findMarriage(self):
        find_dialog = FindMarriage(self.main_panel)
        find_dialog.exec()
        if find_dialog.is_accepted:
            self.server.get_marriage_key(find_dialog.key, find_dialog.value)

    def update_data(self):
        if self.server.user_role == 'ADMIN':
            self.setAdministratorMode()
        elif self.server.user_role == 'ENGINEER':
            self.setEngineerMode()
        elif self.server.user_role == 'OPERATOR':
            self.setOperatorMode()

    def showTable(self):
        self.main_panel.update_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    connector = ServerConnector("http://localhost", 5000)
    auth_dialog = AuthorizationDialog()
    auth_dialog.exec()
    if auth_dialog.is_accepted:
        try:
            connector.set_user(auth_dialog.user_id,
                               # sha256(auth_dialog.password_field.text().encode('utf-8')).hexdigest())
                               auth_dialog.password_field.text())
        except SecurityError:
            error_box = QErrorMessage()
            error_box.showMessage("Check your credentials and try again!")
            error_box.setWindowTitle("Security error")
            error_box.exec()
            sys.exit(1)
        window = MainWindow(connector)
        window.show()
    sys.exit(app.exec())
