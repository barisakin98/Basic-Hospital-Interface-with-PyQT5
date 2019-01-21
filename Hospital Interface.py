import sys
from PyQt5 import QtWidgets
import datetime
import sqlite3
import os
class giris_penceresi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.asil()
    def asil(self):
        self.main_giris()
        self.database()
    def main_giris(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.kurum=QtWidgets.QLabel("              HACETTEPE ÜNİVERSİTESİ HASTANELERİ")
        self.ilk_metin=QtWidgets.QLabel("Sisteme Hoşgeldiniz.Sistemi kullanabilmek için lütfen giriş yapınız.")
        self.giris_yap=QtWidgets.QPushButton("GİRİŞ YAP")
        self.sifremi_unuttum=QtWidgets.QPushButton("ŞİFREMİ UNUTTUM")
        self.uyari_alani=QtWidgets.QLabel("")
        self.v_box=QtWidgets.QVBoxLayout()
        self.h_box=QtWidgets.QHBoxLayout()
        self.v_box.addStretch()
        self.v_box.addWidget(self.kurum)
        self.v_box.addStretch()
        self.v_box.addWidget(self.ilk_metin)
        self.v_box.addWidget(self.kullanici_adi)
        self.v_box.addWidget(self.parola)
        self.v_box.addWidget(self.uyari_alani)
        self.v_box.addWidget(self.giris_yap)
        self.v_box.addWidget(self.sifremi_unuttum)
        self.v_box.addStretch()
        self.h_box.addStretch()
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch()
        self.setLayout(self.h_box)
        self.setWindowTitle("HACETTEPE ÜNİVERSİTESİ HASTANELERİ ")
        self.setGeometry(400,100,600,600)
        self.giris_yap.clicked.connect(self.giris)
        self.show()
    def database(self):
        kanal=sqlite3.connect("Doktor Kullanıcı adı-Şifre")
        self.cursor=kanal.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS doktor(ıd TEXT,sifre TEXT)")
        kanal.commit()

    def giris(self):
        x=self.kullanici_adi.text()
        y=self.parola.text()
        self.cursor.execute("Select * from doktor where ıd = ? and sifre = ?",(x,y))
        kontrol=self.cursor.fetchall()
        if len(kontrol)==0:
            self.uyari_alani.setText("Kullanıcı bulunamadı.Lütfen tekrar deneyin.")
        else:
            self.uyari_alani.setText("Giriş başarılı.Sisteme giriş yapılıyor.")
            print("yazı4")
            #os.startfile("C:/Users/User/Desktop/deneme/denem")
            print("okk")
            self.ikincil()
            self.close()

    def ikincil(self):
        print("ne var mq")
        self.ikincipencere=QtWidgets.QWidget()
        self.hasta_sorgula = QtWidgets.QPushButton("HASTA BİLGİLERİ")
        self.istatistiklerim = QtWidgets.QPushButton("İSTATİSTİKLERİM")
        self.notlarim=QtWidgets.QPushButton("NOTLARIM")

        self.v_box = QtWidgets.QVBoxLayout()
        #self.v_box.addStretch()
        self.v_box.addWidget(self.hasta_sorgula)
        self.v_box.addStretch()
        self.v_box.addWidget(self.istatistiklerim)
        self.v_box.addStretch()
        self.v_box.addWidget(self.notlarim)
        self.h_box = QtWidgets.QHBoxLayout()
        #self.h_box.addStretch()
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch()
        #self.setLayout(self.h_box)
        self.ikincipencere.setLayout(self.h_box)
        self.hasta_sorgula.clicked.connect(self.hasta_sorgulama)
        self.ikincipencere.setGeometry(400,100,600,600)
        self.ikincipencere.setWindowTitle("HACETTEPE ÜNİVERSİTESİ HASTANELERİ")
        self.ikincipencere.show()

        #self.istatistiklerim.clicked.connect(self.istatistiklerim)
        #self.notlarim.clicked.connect(self.notlarim)

    def hasta_sorgulama(self):
        print("sds")
        self.hasta_bilgileri = QtWidgets.QWidget()
        self.metin = QtWidgets.QLabel("LÜTFEN HASTAYA AİT TC KİMLİK NO'YU GİRİNİZ.")
        self.tc_no = QtWidgets.QLineEdit()
        self.incele = QtWidgets.QPushButton("İNCELE")
        self.metin2=QtWidgets.QLabel("")
        self.v1_box = QtWidgets.QVBoxLayout()
        self.v1_box.addStretch()
        self.v1_box.addWidget(self.metin)
        self.v1_box.addWidget(self.tc_no)
        self.v1_box.addWidget(self.metin2)
        self.v1_box.addWidget(self.incele)
        self.v1_box.addStretch()
        self.hasta_bilgileri.setLayout(self.v1_box)
        self.hasta_bilgileri.setGeometry(400,100,350,350)
        self.hasta_bilgileri.setWindowTitle("HACETTEPE ÜNİVERSİTESİ HASTANELERİ")
        self.incele.clicked.connect(self.kayit_kontrol)
        self.hasta_bilgileri.show()

    def kayit_kontrol(self):
        liste = os.listdir("C:/Users/User/Desktop/hastalar")
        if self.tc_no.text() in liste:
            self.metin2.setText("Hasta bulundu.\nHasta bilgileri gösteriliyor..")
            print("111")
            self.hasta_incelemesi()

        else:
            self.metin2.setText("Hasta bulunamadı.Lütfen tekrar deneyiniz..")
    def hasta_incelemesi(self):
        with open("C:/Users/User/Desktop/hastalar/"+self.tc_no.text()+"/bilgiler.txt","r") as dosya:
            bilgiler=dosya.readline()
        bilgiler2=bilgiler.split(",")
        ad=bilgiler2[0]
        soyad=bilgiler2[1]
        dogum=bilgiler2[2]
        yas=2018-int(dogum.split(".")[2])
        tc=self.tc_no.text()
        print(tc)
        self.hasta_bilgileri2=QtWidgets.QWidget()
        self.baslik=QtWidgets.QLabel("HASTA BİLGİLERİ")
        self.adi=QtWidgets.QLabel("ADI: {}".format(ad))
        self.soyadi=QtWidgets.QLabel("SOYADI: {}".format(soyad))
        self.dtsi=QtWidgets.QLabel("DOĞUM TARİHİ: {}".format(dogum))
        self.yasi=QtWidgets.QLabel("YAŞI: {}".format(yas))
        self.hasta_tcsi=QtWidgets.QLabel("TC KİMLİK NUMARASI: {}".format(tc))
        self.yonlendirme=QtWidgets.QLabel("Hasta hakkında eklemek istediklerinizi aşağıya giriniz.")
        self.ekle=QtWidgets.QPushButton("EKLE")
        self.temizle=QtWidgets.QPushButton("TEMİZLE")
        self.yazi_alani=QtWidgets.QTextEdit()
        self.eski_veriler=QtWidgets.QPushButton("GEÇMİŞ BİLGİLERİ GÖR")
        self.recete=QtWidgets.QPushButton("REÇETELE!")
        self.lab=QtWidgets.QPushButton("LABORATUVAR SONUÇLARI")
        self.imageging=QtWidgets.QPushButton("GÖRÜNTÜLEME SONUÇLARI")
        self.alt_alan=QtWidgets.QLabel("")
        self.v4_box=QtWidgets.QVBoxLayout()
        self.v3_box=QtWidgets.QVBoxLayout()
        self.v2_box=QtWidgets.QVBoxLayout()
        self.h2_box=QtWidgets.QHBoxLayout()
        self.v5_box=QtWidgets.QVBoxLayout()
        self.v2_box.addWidget(self.baslik)
        self.v2_box.addWidget(self.adi)
        self.v2_box.addWidget(self.soyadi)
        self.v2_box.addWidget(self.dtsi)
        self.v2_box.addWidget(self.yasi)
        self.v2_box.addWidget(self.hasta_tcsi)
        self.v2_box.addStretch()
        self.v3_box.addWidget(self.yazi_alani)
        self.v3_box.addWidget(self.alt_alan)
        self.v3_box.addWidget(self.ekle)
        self.v3_box.addWidget(self.temizle)
        self.v3_box.addStretch()
        self.v4_box.addWidget(self.eski_veriler)
        self.v4_box.addWidget(self.recete)
        self.v4_box.addWidget(self.imageging)
        self.v4_box.addWidget(self.lab)
        self.v4_box.addStretch()
        self.h2_box.addLayout(self.v2_box)
        self.h2_box.addLayout(self.v3_box)
        self.v5_box.addLayout(self.h2_box)
        self.v5_box.addStretch()
        self.v5_box.addLayout(self.v4_box)
        self.hasta_bilgileri2.setLayout(self.v5_box)
        self.ekle.clicked.connect(self.girdi)
        self.temizle.clicked.connect(self.temizleme)
        self.eski_veriler.clicked.connect(self.eskiyigor)
        #self.recete.clicked.connect(self.receteyaz)
        #self.lab.clicked.connect(self.labak)
        #self.imageging.clicked.connect(self.gorbak)
        self.hasta_bilgileri2.setGeometry(300,100,500,500)
        self.hasta_bilgileri2.setWindowTitle("HACETTEPE ÜNİVERSİTESİ HASTANELERİ")
        self.hasta_bilgileri2.show()
    def girdi(self):
        metin_k=self.yazi_alani.toPlainText()
        an=datetime.datetime.now()
        tarih=str(an.day)+"/"+str(an.month)+"/"+str(an.year)
        metink_son=tarih+":"+metin_k
        print("girdi")
        with open("C:/Users/User/Desktop/hastalar/"+self.tc_no.text()+"/eskiveriler.txt","a+") as file:
            file.write(metink_son+"\n")
        self.alt_alan.setText("Başarıyla eklendi.")
    def temizleme(self):
        print("girmedi")
        self.yazi_alani.clear()
    def eskiyigor(self):
        with open("C:/Users/User/Desktop/hastalar/"+self.tc_no.text()+"/eskiveriler.txt","r") as son:
            verim=son.read()
        self.lastpencere=QtWidgets.QWidget()
        self.yazim_alani=QtWidgets.QTextEdit()
        self.y_box=QtWidgets.QHBoxLayout()
        self.y_box.addWidget(self.yazim_alani)
        self.lastpencere.setLayout(self.y_box)
        self.lastpencere.setGeometry(800,100,400,400)
        self.yazim_alani.setText(verim)
        self.lastpencere.setWindowTitle("HACETTEPE ÜNİVERSİTESİ HASTANELERİ")
        self.lastpencere.show()

app =QtWidgets.QApplication(sys.argv)
pencere=giris_penceresi()
sys.exit(app.exec())
