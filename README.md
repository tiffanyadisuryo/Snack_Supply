# Snack_Supply
Ini adalah repositori untuk Web Aplikasi Snack Supply, berikut link dari app tersebut : https://tiffanyadisuryo-snacksupply.adaptable.app/main/ 

<details>
<summary>Tugas 2</summary>

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
    
    ![BAGAN DJANGO](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/723a534f-d8cb-4ea6-b698-8ef6d9ce6685)
  
  Saat client mengakses URL, Django kemudian menggunakan 'urls.py' untuk menentukan view. View membaca dan menulis data dengan models.py sesuai permintaan. Disitu views.py akan merender halaman web menggunakan template (file.html). Akhirnya, response akan dikembalikan kepada client.


* Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

  Virtual environment dapat mengisolasi dependensi Django dari paket lain sehingga tidak akan menimbulkan konflik satu sama lain dan dapat konsisten. 
  Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment tetapi security dari dependensi Django akan berkurang. Sehingga terdapat kemungkinan terjadi konflik antara dependensi Django dan paket lainnya.

* Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

  MVC adalah penghubung Model dan View. MVC adalah pola desain yang umum digunakan untuk pengembangan software non-web, sedangkan MVT dan MVVM lebih khusus untuk     pengembangan web.
  Dalam MVT, kerangka kerja Django menjadi controller, yang mengatur alur web request dan memilih view berdasarkan URL yang diakses. Dalam MVT, Template secara khusus merender tampilan web.
  MVVM adalah pola desain untuk pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama yang tampilannya dinamis.
  ViewModel tidak ada di MVC atau MVT. Kegunannya adalah untuk memisahkan tampilan dengan cara yang lebih rapih dan terstruktur.
</details>

<details>
<summary>Tugas 3</summary>

* Apa perbedaan antara form POST dan form GET dalam Django?
  * Form POST
    1. Datanya tidak dapat dilihat dalam URL
    2. Lebih aman jika mengirim data yang sensitif
    3. Data tidak akan tersimpan dalam cache karena data dikirim dalam badan request HTTP
    4. Panjang data yang bisa dikirimkan tidak terbatas
    5. Cocok untuk menyimpan data dalam bentuk form
  * Form GET
    1. Datanya dapat dilihat dalam URL
    2. Kurang aman jika untuk mengirim data yang sensitif
    3. Data tersimpan di cache karena data dikirim sebagai parameter query string di URL
    4. Panjang data yang bisa dikirimkan terbatas
    5. Cocok untuk mengakses halaman web yang datanya tidak berubah

* Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
  * XML
    1. biasa digunakan untuk memindahkan data yang tidak berubah-ubah
    2. menggunakan tag yang mirip tag HTML
    3. lebih sulit untuk dibaca
  * JSON
    1. paling sering digunakan untuk pemindahan data antara server web dan client
    2. menggunakan format key:value
    3. formatnya mudah dipahami sehingga mudah dibaca
  * HTML
    1. biasa digunakan untuk mengatur tampilan dari web tersebut
    2. menggunakan tag HTML
    3. relatif mudah untuk dibaca
  
* Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
  1. format pertukaran datanya ringan dan _compact_.
  2. syntax nya mudah dibaca dan ditulis oleh manusia.
  3. banyak digunakan dan didukung oleh banyak bahasa pemrograman, kerangka kerja, dan pustaka.
  4. mudah dikonversi menjadi objek JavaScript dengan JSON.parse().
  5. berkompatibel dengan API, sebuah arsitektur untuk membuat web yang populer.
  
* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1. Pertama jalankan virtual environment
  2. Lalu buka urls.py pada folder Snack_Supply dan ubah path main menjadi kosong pada urlspatterns.
     ```
     urlpatterns = [
        path('', include('main.urls')),
        path('admin/', admin.site.urls),
     ]
     ```
  3. membuat folder 'template' pada direktori utama kemudian membuat base.html yang isinya sebagai berikut
     ```
      {% load static %}
      <!DOCTYPE html>
      <html lang="en">
          <head>
              <meta charset="UTF-8" />
              <meta
                  name="viewport"
                  content="width=device-width, initial-scale=1.0"
              />
              {% block meta %}
              {% endblock meta %}
          </head>
      
          <body style="background-color: #EEA36B;">
              {% block content %}
              {% endblock content %}
          </body>
      </html>
     ```
  4. Membuka settings.py pada subdirektori Snack_Supply dan menambahkan kode berikut pada TEMPLATES
     ```
      ...
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
              'APP_DIRS': True,
              ...
          }
      ]
       ...
     ```
  5. Kemudian menambahkan kode berikut di awal file main.html
     ```
      {% extends 'base.html' %}
     ```
  6. Selanjutnya, membuat berkas forms.py pada direktori main yang berisi sebagai berikut
     ```
      from django.forms import ModelForm
      from main.models import Item

      class ItemForm(ModelForm):
          class Meta:
              model = Item
              fields = ["name", "amount", "description"]
     ```
  7. Lalu menambahkan berbagai import pada views.py dalam direktori main seperti berikut
     ```
      from django.http import HttpResponseRedirect
      from main.forms import ItemForm
      from django.urls import reverse
     ```
  8. Kemudian pada views.py membuat fungsi create_item
     ```
      def create_item(request):
          form = ItemForm(request.POST or None)
      
          if form.is_valid() and request.method == "POST":
              form.save()
              return HttpResponseRedirect(reverse('main:show_main'))
      
          context = {'form': form}
          return render(request, "create_item.html", context)
     ```
  9. Untuk menunjukkan banyak jenis item (bonus), ditambahkan pada fungsi show_main, setelah baris items = Item.objects.all(), kode berikut
      ```
        banyak_items = len(items)
      ```
  lalu juga pada bagian context setelah class': 'PBP D', menjadi 
      ```
        ...
        'banyak_items' : banyak_items,
        'items' : items.
        ...
      ```
  10. Tidak lupa untuk import create_item di urls.py pada direktori main. Dan juga menambahkan path url ke dalam urlpatterns.
  11. Lalu membuat file baru dengan nama create_item.html di direktori templates di direktori main dengan isi sebagai berikut
     ```
      {% extends 'base.html' %} 
      
      {% block content %}
      <h1>Add More Snack</h1>
      
      <form method="POST">
          {% csrf_token %}
          <table>
              {{ form.as_table }}
              <tr>
                  <td></td>
                  <td>
                      <input type="submit" value="Add Item"/>
                  </td>
              </tr>
          </table>
      </form>
      
      {% endblock %}
     ```
  12. Kemudian buka main.html dan tambahkan kode berikut di dalam {% block content %}
    ```
      <h1>Snack Supply</h1>

          <h5>Name:</h5>
          <p>{{name}}</p>

          <h5>Class:</h5>
          <p>{{class}}</p>

      <table bgcolor="black" width="1200">
          <caption><h3>Ada {{banyak_items}} jenis Snacks yang ter-supply di dalam pantry kamu! Mau Snack apa hari ini?</h3></caption>
          <tr bgcolor="#46B2B5">
              <th width="100">Name</th>
              <th width="100">Amount</th>
              <th width="800">Description</th>
              <th width="100">Date Added</th>
          </tr>

          {% for item in items %}
              <tr bgcolor="#8FD5D5">
                  <td align="center">{{item.name}}</td>
                  <td align="center">{{item.amount}}</td>
                  <td>{{item.description}}</td>
                  <td align="center">{{item.date_added}}</td>
              </tr>
          {% endfor %}
      </table>

      <br />

      <a href="{% url 'main:create_item' %}">
          <button>
              Add More Snacks
          </button>
      </a>
    {% endblock content %}
    ```
  13. Lalu buka views.py pada direktori main dan tambahkan import sebagai berikut
    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```
  14. Kemudian tambahkan kode berikut
    ```
    def show_xml(request):
      data = Item.objects.all()
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    def show_json(request):
        data = Item.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    def show_xml_by_id(request, id):
      data = Item.objects.filter(pk=id)
      return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    def show_json_by_id(request, id):
        data = Item.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
  14. Selanjutnya buka urls.py pada folder main dan masukan import berikut
    ```
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
    Tidak lupa untuk menambahkan kode tersebut dalam urlspatterns
    ```
    ...
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...
    ```
  15. Terakhir setelah git add, commit, dan push, untuk menjalankan server menggunakan perintah python manage.py runserver. Menggunakan beberapa link dibawah akan memunculkan tampilan seperti dibawah
      ![markdown html](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/d1c94e5a-7479-4a67-b147-76768f1c5266)
      ![xml](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/246c37a8-7dbe-46d6-b34f-e014e42e15a7)
      ![json](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/a034b6aa-1289-4219-87aa-3404dccedc9f)
      ![xml by id](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/0c1560e2-62fb-4621-ac62-72c975739b27)
      ![json by id](https://github.com/tiffanyadisuryo/Snack_Supply/assets/119838581/5fc631ab-47f7-4886-b121-1fe9684c0020)
    
</details>

<details>
<summary>Tugas 4</summary>

* Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

  UserCreationForm merupakan sebuah form dari framework web Python, Django untuk mempermudah pembuatan user baru pada web. Terdapat permintaan data seperti username, password dengan ketentuan dan syarat tertentu, dll.
  Kelebihan:
  1. Sudah disediakan dahulu segala form permintaan data dan sangat mudah menggunakannya.
  2. Terdapat validasi secara otomatis. Seperti ketentuan password yang kuat sudah disediakan.
  3. terintegrasi dengan Django Authenticatiom.
  Kekurangan:
  1. Tampilan default-nya membosankan dan kurang menarik.
  2. Walau bisa di-custom, namun terbatas.
     
* Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

  Autentikasi adalah proses verivikasi siapa yang sedang log in.
  Otorisasi adalah proses verifikasi apakah usermemiliki akses terhadap sesuatu.
  
* Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? 

  Cookies merupakan sebuah file yang disimpan di device user yang saat adanya aktivitas pada sebuah web. Cookies biasa digunakan untuk menyimpan informasi seperti preferensi user, riwayat pencarian, dan juga sesi.
  
* Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
  1. Cross-Site Scripting: Terjadi serangan XSS pada cookies yang merupakan script berbahaya untuk mencuri informasi yang tersimpan.
  3. Cookie Theft: Pencurian atau penggandaan cookie untuk mengakses akun user.
  4. Cookie Poisoning: Terjadi pemanipulasian data dalam cookie seperti sesi dan data palsu.
  5. Cross-Site Request Forgery: Terjadi serangan dimana cookie dimanfaatkan untuk melakukan tindakan seperti permintaan otorisasi palsu.
  
* Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  1. Mengubah views.py pada subdirektori main dengan kode berikut:
     ```
        from django.shortcuts import render
        from django.http import HttpResponseRedirect
        from main.forms import ItemForm
        from django.urls import reverse
        from main.models import Item
        from django.http import HttpResponse
        from django.core import serializers
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        from django.contrib.auth import authenticate, login
        from django.contrib.auth import logout
        from django.contrib.auth.decorators import login_required
        import datetime
        
        # Create your views here.
        
        @login_required(login_url='/login')
        def show_main(request):
            items = Item.objects.filter(user=request.user)
            banyak_items = len(items)
        
            context = {
                'name': request.user.username,
                'class': 'PBP D',
                'banyak_items' : banyak_items,
                'items' : items,
                'last_login': request.COOKIES['last_login'],
            }
        
            return render(request, "main.html", context)
        
        def create_item(request):
            form = ItemForm(request.POST or None)
        
            if form.is_valid() and request.method == "POST":
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                return HttpResponseRedirect(reverse('main:show_main'))
        
            context = {'form': form}
            return render(request, "create_item.html", context)
        
        def show_xml(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
        def show_json(request):
            data = Item.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        
        def show_xml_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        
        def show_json_by_id(request, id):
            data = Item.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        
        def register(request):
            form = UserCreationForm()
        
            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
        
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)
        
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        
        def add_item(request, id):
            data = Item.objects.get(pk=id)
            data.amount +=1
            data.save()
            return redirect('main:show_main')
        
        def min_item(request, id):
            data = Item.objects.get(pk=id)
            data.amount -=1
            data.save()
            if (data.amount <= 0):
                data.delete()
            return redirect('main:show_main')
        
        def remove_item(request, id):
            data = Item.objects.get(pk=id)
            data.delete()
            return redirect('main:show_main')
     ```
     Penambahan berbagai import untuk function baru yang ditambahkan. "@login_required(login_url='/login')" digunakan agar sebelum bisa mengakses main.html, harus login terlebih dahulu. Nama yang akan muncul bergantung pada username setelah login berhasil. Menggunakan "UserCreationForm(request.POST)" untuk membuat halaman register yang merupakan framework. Function login user digunakan untuk menyertakan perintah bila user menekan tombol login, sama dengan logout_user. Function add_item digunakan untuk menyertakan perintah bila user menekan tombol "+" untuk menambah amount dari item sesuai dengan pk-nya. Function min_item digunakan untuk menyertakan perintah bila user menekan tombol "-" untuk mengurangi amount dari item sesuai dengan pk-nya, dan jika amount <=0 maka akan langsung dihapus item tersebut dari tabel. Function remove_item digunakan untuk menyertakan perintah bila user menekan tombol "Yummy!" untuk menghilangkan baris item tersebut dari tabel sesuai dengan pk-nya.
  2. Mengubah urls.py pada subdirektori main dengan kode berikut:
     ```
        from django.urls import path
        from main.views import show_main
        from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
        from main.views import register 
        from main.views import login_user
        from main.views import logout_user
        from main.views import add_item
        from main.views import min_item
        from main.views import remove_item
        
        app_name = 'main'
        
        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create_item', create_item, name='create_item'),
            path('xml/', show_xml, name='show_xml'), 
            path('json/', show_json, name='show_json'), 
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
            path('register/', register, name='register'),
            path('login/', login_user, name='login'),
            path('logout/', logout_user, name='logout'),
            path('add_item/<int:id>/', add_item, name='add_item'),
            path('min_item/<int:id>/', min_item, name='min_item'),
            path('remove_item/<int:id>/', remove_item, name='remove_item'),
        ]
     ```
     Mengimport semua button yang ditambahkan di views.py. Kemudian membuat path agar saat tombol ditekan request akan disampaikan menggunakan url dan function dari views.py akan dijalankan. Terdapat /<int:id>/ untuk add_item, min_item, dan remove_item agar spesifik dengan item yang dimaksud.
  3. Mengganti dengan kode berikut pada models.py di subdirektori main
     ```
        from django.db import models
        from django.contrib.auth.models import User
        
        class Item(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            name = models.CharField(max_length=255)
            date_added = models.DateField(auto_now_add=True)
            amount = models.IntegerField()
            description = models.TextField()
     ```
     Bagian yang ditambahkan adalah "user = models.ForeignKey(User, on_delete=models.CASCADE)" yang berfungsi untuk menghubungkan antara list item dan user-nya.
  4. membuat file baru dengan nama login.html pada subdirektori main/templates/ dengan isi
     ```
        {% extends 'base.html' %}
        
        {% block meta %}
            <title>Login</title>
        {% endblock meta %}
        
        {% block content %}
        
        <div class = "login">
        
            <h1>Login</h1>
        
            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>
        
                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>
        
            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>
        
        </div>
        {% endblock content %}
     ```
  5. membuat file baru dengan nama register.html pada subdirektori main/templates/ dengan isi
     ```
        {% extends 'base.html' %}
        
        {% block meta %}
            <title>Register</title>
        {% endblock meta %}
        
        {% block content %}  
        
        <div class = "login">
            
            <h1>Register</h1>  
        
                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>
        
            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}
        
        </div>  
        
        {% endblock content %}
      ```
  6. Mengganti isi main.html dengan kode tersebut
      ```
      {% extends 'base.html' %}
      
      {% block content %}
      <h1>Snack Supply</h1>
      
          <h5>Name:</h5>
          <p>{{name}}</p>
      
          <h5>Class:</h5>
          <p>{{class}}</p>
      
      <table bgcolor="black" width="1200">
          <caption><h3>Ada {{banyak_items}} jenis Snacks yang ter-supply di dalam pantry kamu! Mau Snack apa hari ini?</h3></caption>
          <tr bgcolor="#46B2B5">
              <th width="100">Name</th>
              <th width="100">Amount</th>
              <th width="800">Description</th>
              <th width="100">Date Added</th>
              <th>Finished Already?</th>
          </tr>
          {% for item in items %}
              <tr bgcolor="#8FD5D5">
                  <td align="center">{{item.name}}</td>
                  <td align="center">
                      <table width="100">
                      <th width="40" align="right">{{item.amount}}</th>
                      <th width="40" align="right">
                      <a href="/add_item/{{item.pk}}/">
                          <button class="custom-button">
                              +
                          </button>
                      </a><br>
                      <a href="/min_item/{{item.pk}}/">
                          <button class="custom-button">
                              -
                          </button>
                      </a>
                      </th>
                      </table>
                  </td>
                  <td>{{item.description}}</td>
                  <td align="center">{{item.date_added}}</td>
                  <td align="center">
                      <a href="/remove_item/{{item.pk}}/">
                          <button class="custom-button">
                              Yummy!
                          </button>
                      </a>
                  </td>
              </tr>
          {% endfor %}
      </table>
      
      <br/>
      
      <a href="{% url 'main:create_item' %}">
          <button>
              Add More Snacks
          </button>
      </a>
      
      <h5>Sesi terakhir login: {{ last_login }}</h5>
      
      <a href="{% url 'main:logout' %}">
          <button>
              Logout
          </button>
      </a>
      
      {% endblock content %}
      ```
      Bagian button '+' dan '-' saya letakan di cell yang sama dengan amount, dan penyusunannya menggunakan tabel 'rahasia'. Tombol remove terdapat di paling kanan. Tulisan sesi terdapat diantara tombol add more snacks dan logout.
  7. Karena models.py diganti maka tentu harus run "python manage.py makemigrations" pada command prompt. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data. Ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada. Lalu tidak lupa untuk run "python manage.py migrate".
</details>
  
