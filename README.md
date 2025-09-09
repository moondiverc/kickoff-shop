# KickOff Shop

KickOff Shop adalah project Django sederhana mengenai toko yang menjual perlengkapan sepak bola. Tugas ini dikerjakan oleh Nezzaluna Azzahra dengan NPM 2406495741 dari kelas PBP-D.

## Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step.

- Membuat dan mengaktifkan virtual environment
- Menyiapkan dan menginstall dependencies
- Membuat project Django
- Membuat .env dan .env.prod file
- Setting library di kickoff-shop/settings.py
- Mengubah allowed hosts di kickoff-shop/settings.py
- Menambah konfigurasi production di kickoff-shop/settings.py
- Mengubah konfigurasi database di kickoff-shop/settings.py
- Melakukan migrasi dan run server
- Membuat file .gitignore
- Membuat new project di PWS
- Mengubah environs dengan isi file .env.prod
- Menambahkan URL web di allowed hosts
- Melakukan add, commit, dan push ke GitHub
- Menjalankan command git di Project Command kemudian isi username dan password
- Membuat aplikasi Django
- Mendaftarkan main ke project di kickoff-shop/settings.py
- Membuat template folder di dalam main dan isi dengan main.html
- Membuat model dengan membuat class Product dan atribut wajib di main/models.py
- Melakukan migrasi model
- Membuat fungsi show_main pada main/views.py
- Membuat tampilan HTML pada main/templates/main.html beserta parameter yang akan ditampilkan
- Membuat file untuk routing pada main/urls.py
- Mendaftarkan routing main ke project pada kickoff-shop/urls.py

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan peran settings.py dalam proyek Django!
   Secara umum settings.py berfungsi untuk mengatur konfigurasi pada project Django yang sedang dikerjakan. Beberapa konfigurasi yang diatur pada settings.py antara lain adalah konfigurasi database, aplikasi yang digunakan, host yang diizinkan, templates dan static, middleware, informasi keamanan, dan konfigurasi lainnya.
4. Bagaimana cara kerja migrasi database di Django?
   Migrasi model adalah cara framework Django untuk melacak perubahan pada model basis data pada project dan command migrasi ini dilakukan untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinikan dalam kode terbaru. Cara kerja migrasi database di Django adalah dengan menjalankan command "make migrations" untuk membuat berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Kemudian, menggunakan command "migrate" untuk menerapkan migrasi ke dalam basis data lokal, command tersebut mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data dengan menjalankan command sebelumnya. Setiap kali melakukan perubahan pada model, migrasi harus selalu dilakukan untuk merefleksikan perubahan tersebut.
5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Menurut saya, framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena Django menyediakan banyak fitur bawaan dan library yang memudahkan pengembangan aplikasi web, menerapkan konsep MVT dimana Django memisahkan antara data, logika, dan tampilan sehingga memiliki struktur project yang jelas, memiliki keamanan bawaan yang baik, mudah integrasi dengan database, serta memiliki dapat digunakan untuk mengembangkan dari project skala kecil hingga besar.
6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
   Asisten dosen sudah stand-by ketika tutorial sehingga dapat membantu jika ada pertanyaan atau kendala.
