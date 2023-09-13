# Snack_Supply
Ini adalah repositori untuk Web Aplikasi Snack Supply, berikut link dari app tersebut : https://tiffanyadisuryo-snacksupply.adaptable.app/main/ 

* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1. Dimulai dengan membuat repositori lokal baru berjudul Snack_Supply kemudian mengaktifkan virtual environment menggunakan terminal.
  2. Dilanjut dengan menyiapkan dependencies dan membiat project Django dengan cara membuat berkas requirements.txt yang berisi dependencies sebagai berikut:
     ```
      django
      gunicorn
      whitenoise
      psycopg2-binary
      requests
      urllib3
     ```
     Kemudian pasang dependencies tersebut dan buat project Django bernama Snack_Supply.
  4. Lalu konfigurasi Proyek dan Menjalankan server. di dalam settings.py, izinkan akses kepada semua host, lalu jalankan server Django.
  5. Kemudian, membuat repositori GitHub dengan nama yang sama lalu diinisiasi di repositori lokal. Ditambahkan berkas .gitignore pada repositori lokal. Tentunya tidak lupa untuk add, commit, dan push.
  6. Selanjutnya membuat aplikasi main ke dalam project. Jangan lupa menambahkan 'main' ke INSTALLED_APPS di settings.py.
  7. Lalu tentunya membuat dan mengisi berkas main.html di direktori templates sesuai keinginan kita. Saya ingin menampilkan nama aplikasi, nama saya, kelas, dan juga tabel dari inventori Snack saya.
  8. Kemudian, mengubah berkas models.py dalam aplikasi main hingga sesuai dengan model aplikasi yang kita inginkan. Sebagai contoh:
     ```
      from django.db import models
      class Product(models.Model):
          name = models.CharField(max_length=255)
          amount = models.IntegerField()
          description = models.TextField()
     ```
  10. Setelah diubah, models.py harus dimigrasi.
  11. Selanjutnya, kita integrasikan komponen MVT dengan menambahkan fungsi show_main ke views.py yang berisi data yang ingin kita masukan ke web aplikasi. Sebagai contoh:
      ```
      from django.shortcuts import render
      def show_main(request):
          context = {
              'name': 'Tiffany Lindy Adisuryo',
              'class': 'PBP D',
              'snacks' : [{'name' : "Chitato", 'amount' : "1", 'description' : "Chitato is a popular Indonesian brand of potato chips known for its wide range of bold and flavorful snack offerings."},
                          {'name' : "Beng Beng", 'amount' : "20", 'description' : "Beng Beng is a well-known Indonesian chocolate snack that combines layers of crispy wafer and creamy chocolate filling, offering a delightful and satisfying treat."},
                          {'name' : "Oreo", 'amount' : "5", 'description' : "Oreo is a globally recognized sandwich cookie brand known for its iconic combination of two chocolate-flavored wafers with a sweet cream filling."}]
          }
          return render(request, "main.html", context)
      ```
  13. Lalu yang tidak kalah penting adalah mengonfigurasi Routing URL dengan mengisi urls.py di direktori main dan Snack_Supply. Sehingga dapat menunjukkan perintah apa yang dilakukan bila url diakses.
  14. Kemudian, tidak lupa untuk add, commit, push pada GitHub agar dapat dilakukan deployment dengan Adaptable. 
  15. Terakhir adalah deployment itu sendiri. Buka akun GitHub dan pilih Repositori Snack_Supply. Lalu pilih Python App Template sebagai template deployment, pilih PostgreSQL sebagai tipe basis data yang akan digunakan, dan isi versi dari python yang digunakan dan pada bagian Start Command masukkan perintah python manage.py migrate && gunicorn Snack_Supply.wsgi. Masukan nama yang akan menjadi link web nantinya dan centang HTTP Listener on PORT lalu klik Deploy App.

* Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    
    ![BAGAN DJANGO](C:\Users\ASUS\Documents\2kuliaahh\PBP\Tugas\Tugas2\BaganDjango.png)
  
  Saat client mengakses URL, Django kemudian menggunakan 'urls.py' untuk menentukan view. View membaca dan menulis data dengan models.py sesuai permintaan. Disitu views.py akan merender halaman web menggunakan template (file.html). Akhirnya, response akan dikembalikan kepada client.


* Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

  Virtual environment dapat mengisolasi dependensi Django dari paket lain sehingga tidak akan menimbulkan konflik satu sama lain dan dapat konsisten. 
  Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment tetapi security dari dependensi Django akan berkurang. Sehingga terdapat kemungkinan terjadi konflik antara dependensi Django dan paket lainnya.

* Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

  MVC adalah penghubung Model dan View. MVC adalah pola desain yang umum digunakan untuk pengembangan software non-web, sedangkan MVT dan MVVM lebih khusus untuk     pengembangan web.
  Dalam MVT, kerangka kerja Django menjadi controller, yang mengatur alur web request dan memilih view berdasarkan URL yang diakses. Dalam MVT, Template secara khusus merender tampilan web.
  MVVM adalah pola desain untuk pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama yang tampilannya dinamis.
  ViewModel tidak ada di MVC atau MVT. Kegunannya adalah untuk memisahkan tampilan dengan cara yang lebih rapih dan terstruktur.
