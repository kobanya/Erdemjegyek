import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, \
    QVBoxLayout, QWidget, QLabel, QFileDialog
import magyar


class Diak:
    def __init__(self, nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas):
        self.nev = nev
        self.magyar = magyar
        self.tortenelem = tortenelem
        self.matematika = matematika
        self.idegen_nyelv = idegen_nyelv
        self.igazolt_hianyzas = igazolt_hianyzas
        self.igazolatlan_hianyzas = igazolatlan_hianyzas

    # Az átlag kiszámítása
    def atlag(self):
        return (self.magyar + self.tortenelem + self.matematika + self.idegen_nyelv) / 4.0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Diákok Adatai")
        self.setGeometry(320, 400, 2200, 600)

        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(365, 20, 1800, 400)
        self.table_widget.setSortingEnabled(True)

        self.input_layout = QVBoxLayout()
        self.input_widget = QWidget()
        self.input_widget.setLayout(self.input_layout)
        self.layout.addWidget(self.input_widget)

        label1 = QLabel("Név: ", self)
        label1.setGeometry(15, 70, 100, 40)
        self.input_nev = QLineEdit(self)
        self.input_nev.setGeometry(150, 70, 150, 40)

        label1 = QLabel("Magyar nyelv:", self)
        label1.setGeometry(15, 120, 180, 40)
        self.input_magyar = QLineEdit(self)
        self.input_magyar.setGeometry(200, 120, 100, 40)

        label1 = QLabel("Történelem: ", self)
        label1.setGeometry(15, 170, 160, 40)
        self.input_tortenelem = QLineEdit(self)
        self.input_tortenelem.setGeometry(200, 170, 100, 40)

        label1 = QLabel("Matematika: ", self)
        label1.setGeometry(15, 220, 170, 40)
        self.input_matematika = QLineEdit(self)
        self.input_matematika.setGeometry(200, 220, 100, 40)

        label1 = QLabel("Idegen nyelv: ", self)
        label1.setGeometry(15, 270, 170, 40)
        self.input_idegen_nyelv = QLineEdit(self)
        self.input_idegen_nyelv.setGeometry(200, 270, 100, 40)

        label1 = QLabel("Igazolt : ", self)
        label1.setGeometry(15, 320, 170, 40)
        self.input_igazolt_hianyzas = QLineEdit(self)
        self.input_igazolt_hianyzas.setGeometry(200, 320, 100, 40)

        label1 = QLabel("Igazolatlan : ", self)
        label1.setGeometry(15, 370, 170, 40)
        self.input_igazolatlan_hianyzas = QLineEdit(self)
        self.input_igazolatlan_hianyzas.setGeometry(200, 370, 100, 40)

        self.btn_hozzaadas = QPushButton("Hozzáadás", self)
        self.btn_hozzaadas.setGeometry(15, 490, 200, 50)
        self.btn_hozzaadas.clicked.connect(self.hozzaadas)

        #self.input_layout.addWidget(self.btn_hozzaadas)

        self.btn_beolvas = QPushButton("Beolvasás", self)
        self.btn_beolvas.setGeometry(15, 20, 150, 40)
        self.btn_beolvas.clicked.connect(self.beolvasas)

        # A gomb hozzáadása és az eseménykezelő beállítása
        self.btn_mentes = QPushButton("Mentés új fájlba", self)
        self.btn_mentes.setGeometry(250, 490, 300, 50)
        self.btn_mentes.clicked.connect(self.mentes)

        self.btn_bizonyitvany = QPushButton("Bizonyítvány nyomtatása", self)
        self.btn_bizonyitvany.setGeometry(1650, 490, 400, 50)
        self.btn_bizonyitvany.clicked.connect(self.nyomtat)
        #self.input_layout.addWidget(self.btn_bizonyitvany)

        self.label_mentes = QLabel(" ", self)
        self.label_mentes.setGeometry(650, 490, 950, 30)

        # self.input_layout.addWidget(self.btn_beolvas)
       # self.btn_beolvas = btn_beolvas


        self.diakok = []
        self.show_data()


    def show_data(self):
        diakok = self.diakok

        self.table_widget.setRowCount(len(diakok)) # Sorok száma
        self.table_widget.setColumnCount(8)         # Fix oszlopok száma
        self.table_widget.setHorizontalHeaderLabels(
            ["A diák neve", "Magyar", "Történelem", "Matematika", "Idegen Nyelv",
             "Igazolt Hiányzás", "Igazolatlan Hiányzás", "Átlag"]) # Fix fejléc

        for row, diak in enumerate(diakok):
            self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
            self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
            self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
            self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
            self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
            self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        self.table_widget.resizeRowsToContents()      # Átméretezés
        self.table_widget.resizeColumnsToContents()

    def hozzaadas(self):                    # a beolvasott adatok egyeztetése az objektumokkal
        nev = self.input_nev.text()
        magyar = int(self.input_magyar.text())
        tortenelem = int(self.input_tortenelem.text())
        matematika = int(self.input_matematika.text())
        idegen_nyelv = int(self.input_idegen_nyelv.text())
        igazolt_hianyzas = int(self.input_igazolt_hianyzas.text())
        igazolatlan_hianyzas = int(self.input_igazolatlan_hianyzas.text())

        diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas)
        self.diakok.append(diak)   #  Listához adás

        row = self.table_widget.rowCount()
        self.table_widget.setRowCount(row + 1)   # az Utolsó sor után adjuk hozzá

        self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
        self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
        self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
        self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
        self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
        self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
        self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
        self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        self.clear_input_fields()  # mentés után a beviteli mezőket töröljük

    def clear_input_fields(self):      # a beviteli mezők frissítése
        self.input_nev.clear()
        self.input_magyar.clear()
        self.input_tortenelem.clear()
        self.input_matematika.clear()
        self.input_idegen_nyelv.clear()
        self.input_igazolt_hianyzas.clear()
        self.input_igazolatlan_hianyzas.clear()

    def beolvasas(self):           # a TXT beolvasása
        file_path = "osztaly.txt"  # A fájl elérési útvonalát itt kell megadnod

        try: # ha tudod, olvasd be
            with open(file_path, "r") as file:
                for sor in file:
                    adatok = sor.strip().split(",")   # az adatok darabolása vessző mentén
                    nev = adatok[0]
                    magyar = int(adatok[1])
                    tortenelem = int(adatok[2])
                    matematika = int(adatok[3])
                    idegen_nyelv = int(adatok[4])
                    igazolt_hianyzas = int(adatok[5])
                    igazolatlan_hianyzas = int(adatok[6])

                    diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas)
                    self.diakok.append(diak)   # hozzáadjuk a listához

                    row = self.table_widget.rowCount()
                    self.table_widget.setRowCount(row + 1)

                    self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
                    self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
                    self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
                    self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
                    self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
                    self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
                    self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
                    self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        except FileNotFoundError:
            print("A fájl nem található.")  # ha nem találja a fájlt

        self.table_widget.resizeRowsToContents()     # automatikus átméretezés
        self.table_widget.resizeColumnsToContents()

        # Beolvasás gomb letiltása
        self.btn_beolvas.setEnabled(False)  # ne tudjam többször beolvasni a listát csak egyszer
    def hozzaadas(self):
        # Beviteli mezők értékeinek lekérése
        nev = self.input_nev.text()
        magyar = int(self.input_magyar.text())
        tortenelem = int(self.input_tortenelem.text())
        matematika = int(self.input_matematika.text())
        idegen_nyelv = int(self.input_idegen_nyelv.text())
        igazolt_hianyzas = int(self.input_igazolt_hianyzas.text())
        igazolatlan_hianyzas = int(self.input_igazolatlan_hianyzas.text())

        # Új diák létrehozása
        diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas)

        # Diák hozzáadása a listához
        self.diakok.append(diak)    # az új diák hozzáadaása a meglévő listához

        # Új sor hozzáadása a táblázathoz
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)

        # Diák adatainak beállítása a táblázatban
        self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
        self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
        self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
        self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
        self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
        self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
        self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
        self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        # Beviteli mezők tartalmának törlése
        self.clear_input_fields()

        # Sorok és oszlopok méretének igazítása
        self.table_widget.resizeRowsToContents()
        self.table_widget.resizeColumnsToContents()
    def clear_input_fields(self):
        # Beviteli mezők tartalmának törlése
        self.input_nev.clear()
        self.input_magyar.clear()
        self.input_tortenelem.clear()
        self.input_matematika.clear()
        self.input_idegen_nyelv.clear()
        self.input_igazolt_hianyzas.clear()
        self.input_igazolatlan_hianyzas.clear()

    def hozzaadas(self):
        # Új diák hozzáadása az adatokhoz
        nev = self.input_nev.text()
        magyar = int(self.input_magyar.text())
        tortenelem = int(self.input_tortenelem.text())
        matematika = int(self.input_matematika.text())
        idegen_nyelv = int(self.input_idegen_nyelv.text())
        igazolt_hianyzas = int(self.input_igazolt_hianyzas.text())
        igazolatlan_hianyzas = int(self.input_igazolatlan_hianyzas.text())

        diak = Diak(nev, magyar, tortenelem, matematika, idegen_nyelv, igazolt_hianyzas, igazolatlan_hianyzas)
        self.diakok.append(diak)

        # Új diák hozzáadása a táblázathoz
        row = self.table_widget.rowCount()
        self.table_widget.insertRow(row)
        self.table_widget.setItem(row, 0, QTableWidgetItem(diak.nev))
        self.table_widget.setItem(row, 1, QTableWidgetItem(str(diak.magyar)))
        self.table_widget.setItem(row, 2, QTableWidgetItem(str(diak.tortenelem)))
        self.table_widget.setItem(row, 3, QTableWidgetItem(str(diak.matematika)))
        self.table_widget.setItem(row, 4, QTableWidgetItem(str(diak.idegen_nyelv)))
        self.table_widget.setItem(row, 5, QTableWidgetItem(str(diak.igazolt_hianyzas)))
        self.table_widget.setItem(row, 6, QTableWidgetItem(str(diak.igazolatlan_hianyzas)))
        self.table_widget.setItem(row, 7, QTableWidgetItem(str(diak.atlag())))

        # Beviteli mezők tartalmának törlése
        self.clear_input_fields()

    def mentes(self):
        file_path = "uj.txt"  # Fájl elérési útvonala, ahol el szeretnéd menteni az adatokat

        try:
            with open(file_path, "w") as file:
                for diak in self.diakok:
                    # Adatok kiírása a fájlba, vesszővel elválasztva
                    file.write(
                        f"{diak.nev},{diak.magyar},{diak.tortenelem},{diak.matematika},{diak.idegen_nyelv},{diak.igazolt_hianyzas},{diak.igazolatlan_hianyzas}\n")

            print("Az adatok sikeresen mentve.")
            self.label_mentes.setText("Sikeres mentés! Nyissa meg az uj.txt fájlt ")


        except IOError:
            print("Hiba a fájl mentésekor.")

    def nyomtat(self):
        selected_row = self.table_widget.currentRow()  # Kiválasztott sor lekérése
        if selected_row >= 0:
            diak = self.diakok[selected_row]  # Diák adatainak lekérése
            file_path, _ = QFileDialog.getSaveFileName(self, "Bizonyítvány mentése", "",
                                                       "Text Files (*.txt)")  # Fájl mentési helyének és nevének kiválasztása
            if file_path:
                try:
                    with open(file_path, "w") as file:
                        file.write(f'\n{">" * 25} Kőrösi Csoma Sándor Gimnázium {"<" * 25}\n\n')
                        file.write(f'{" " * 20} 1102 Budapest, Kőrösi Csoma Sándor út 76{" " * 25}\n\n\n')
                        file.write(f"Név:                 {random.choice(magyar.vezeteknev)} {diak.nev}\n")
                        file.write(f'Születés helye:      {random.choice(list(magyar.megye_szekhely.values()))}\n')

                        file.write(f"Anyja neve:          {random.choice(magyar.vezeteknev)} {random.choice(magyar.keresztnev_n)}\n")
                        file.write(f"Állampolgársága:     Magyarország \n\n")
                        file.write(f'{"__" * 40}\n\n\n')
                        file.write(f"Magyar nyelv: {diak.magyar}\n")
                        file.write(f"Történelem:   {diak.tortenelem}\n")
                        file.write(f"Matematika:   {diak.matematika}\n")
                        file.write(f"Idegen nyelv: {diak.idegen_nyelv}\n\n\n")
                        file.write(f"Igazolt hiányzás: {diak.igazolt_hianyzas}\n")
                        file.write(f"Igazolatlan hiányzás: {diak.igazolatlan_hianyzas}\n")
                        file.write(f"Átlag: {diak.atlag()}\n")
                    self.label_mentes.setText(f"A(z) '{file_path}' fájl sikeresen mentve.")
                except IOError:
                    print("Hiba a fájl mentésekor.")
            else:
                print("Nem választottál mentési helyet.")
        else:
            print("Nincs kijelölt sor.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()  # MainWindow osztály példányosítása
    window.show()
    sys.exit(app.exec_())
