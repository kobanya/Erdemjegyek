import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtWidgets import QHeaderView


class Diak:
    def __init__(self, nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas):
        self.nev = nev
        self.magyar = magyar
        self.tortenelem = tortenelem
        self.matematika = matematika
        self.idegen_nyelv = idegen_nyelv
        self.igazolt_hianyzas = igazolt_hianyzas
        self.igazolatlan_hianyzas = igazolatlan_hianyzas

    def atlag(self):  # az átlag kiszámítása
        return (self.magyar + self.tortenelem + self.matematika + self.idegen_nyelv) / 4.0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diákok Adatai")  # az ablak fejléce
        self.setGeometry(300, 300, 1550, 400)  # az ablak méretei és elhelyezkedése
        # self.setMinimumWidth(800)
        # self.setMinimumHeight(400)

        self.table_widget = QTableWidget(self)  # az adattábla
        self.table_widget.setGeometry(200, 10, 1300, 380)  # az adattábla méretei
        self.show_data()

    def show_data(self):
        diakok = []  # A diákok lista létrehozása

        # Első diák hozzáadása, megadott fix adatok
        diak1 = Diak("Kázmér", 3, 2, 5, 5, 10, 0)
        diakok.append(diak1)  # hozzáadom a listához Kázmér jegyeit

        self.table_widget.setRowCount(len(diakok))  # Táblázat oszlopainak meghatározása az elemek számából
        self.table_widget.setColumnCount(8)  # a fejléc elemeit fixen definiáltuk
        self.table_widget.setHorizontalHeaderLabels(
            ["A diák neve", "Magyar", "Történelem", "Matematika", "Idegen Nyelv",
             "Igazolt Hiányzás", "Igazolatlan Hiányzás", "Átlag"])  # A fejléc elemei, fixen definiálva

        for row, diak in enumerate(diakok):
            self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
            self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
            self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        self.table_widget.resizeRowsToContents()  # Sorok méretére igazítás
        self.table_widget.resizeColumnsToContents()  # Oszlopok méretének igazítása a tartalomhoz

        # Táblázat fejlécének beállítása
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Oszlopok automatikus nyújtása
        # A TXT beolvasásához létrehozunk egy gombot
        btn_beolvas = QPushButton("Beolvasás", self)
        btn_beolvas.setGeometry(10, 20, 180, 30)  # a gomb elhelyezkedésének és méreteinek  koordinátái
        btn_beolvas.clicked.connect(self.beolvasas)  # funkció hozzáadása a gombhoz, ha azt megnyomja valaki

    def beolvasas(self):
        diakok = []

        try:  # Megpróbáljuk beolvasni a txt fájlt
            with open("/home/bela/PycharmProjects/bizonyítvány/osztaly.txt", "r") as file:
                for sor in file:
                    adatok = sor.strip().split(",")  # feldaraboljuk vesszők mentén
                    nev = adatok[0]
                    magyar = int(adatok[1])
                    tortenelem = int(adatok[2])
                    matematika = int(adatok[3])
                    idegen_nyelv = int(adatok[4])
                    igazolt_hianyzas = int(adatok[5])
                    igazolatlan_hianyzas = int(adatok[6])

                    diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas,
                                igazolatlan_hianyzas)
                    diakok.append(diak)  # hozzáadjuk a listához
                    # Beolvasás gomb letiltása


        except FileNotFoundError:  # hiba esetén  kirjuk, hogy nem található
            print("Az osztaly.txt állomány nem található.")

        for diak in diakok:
            self.table_widget.setRowCount(self.table_widget.rowCount() + 1)
            row = self.table_widget.rowCount() - 1
            self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
            self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
            self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        self.table_widget.resizeRowsToContents()

        self.table_widget.resizeColumnsToContents()  # Oszlopok méretének igazítása a tartalomhoz

        # Táblázat fejlécének beállítása
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Oszlopok automatikus nyújtása


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # MainWindow osztály példányosítása
    window.show()
    sys.exit(app.exec_())
