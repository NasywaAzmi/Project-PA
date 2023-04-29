A. Deskripsi program
    Program ini adalah sebuah aplikasi sederhana yang dibuat untuk memanajemen playlist musik. Program ini menggunakan konsep OOP (Object-Oriented Programming) dan memiliki dua buah kelas utama yaitu kelas Playlist dan PlaylistCollection.
    Class Playlist digunakan untuk membuat objek playlist musik, dengan atribut title, artist, genre, dan duration. Sedangkan kelas PlaylistCollection digunakan untuk mengumpulkan semua objek playlist yang telah dibuat menjadi satu kumpulan, yang kemudian dapat digunakan untuk melakukan berbagai operasi seperti menambah, menghapus, mencari, melihat, dan mensortir playlist.
    
    Program ini dimulai dengan user login menggunakan username dan password yang sudah ditentukan dalam sebuah dictionary bernama users. Setelah berhasil login, pengguna akan diarahkan ke menu pilihan yang memungkinkan pengguna untuk melakukan aksi seperti menambahkan playlist, menghapus playlist, mencari playlist, melihat semua playlist, serta mensortir playlist dari durasi terpendek hingga terpanjang.
    
    Untuk melakukan operasi pencarian pada playlist, program menggunakan algoritma Jump Search yang efisien untuk melakukan pencarian dengan cepat, sedangkan untuk mengurutkan playlist, program menggunakan algoritma Quick Sort.
   
   Jadi, program ini merupakan aplikasi sederhana untuk mengelola playlist musik yang efektif dan efisien dengan menggunakan class dan algoritma pencarian yang tepat.


B. Struktur Project
  Struktur project dalam program playlist youtube
  - Class playlist berisi atribut title, artist, genre, dan duration dari sebuah playlist musik.
  - Class PlaylistCollection memungkinkan pengguna untuk menambahkan, menghapus, mencari, melihat, dan mensortir  playlist musik. 
  - Dictionary users: Untuk menyimpan username dan password user.
  - Login user: user diminta untuk memasukkan username dan password, kemudian dicek kecocokannya dengan data yang ada di dictionary users.
  - Function menu: menampilkan pilihan menu dan melakukan aksi sesuai dengan pilihan yang dipilih oleh user
  - Pilihan menu:
    1. Menambahkan Vidio Kedalam Playlist: meminta input dari user untuk menambahkan data Playlist baru, kemudian Playlist ditambahkan ke dalam PlaylistCollection
    2. Hapus Playlist: menghapus Playlist terakhir dari PlaylistCollection
    3. Cari Playlist: mencari Playlist berdasarkan judul dengan menggunakan algoritma jump search
    4. Lihat Playlist: menampilkan seluruh Playlist yang ada di PlaylistCollection
    5. Sort Playlist: mensorting Playlist berdasarkan durasi menggunakan algoritma quick sort
    6. Keluar: keluar dari program 
  - Memanggil fungsi menu untuk menjalankan program.


C. Fitur dan Fungsionalitas 
   Berikut adalah fitur dan fungsionalitas yang terdapat pada program ini:
   1. Class Playlist
      Class Playlist memiliki 4 atribut yaitu title, artist, genre, dan duration. Atribut-atribut tersebut merepresentasikan informasi dari sebuah playlist musik. Class ini dibuat untuk memudahkan dalam membuat objek playlist musik.
   2. Class PlaylistCollection
      Class PlaylistCollection berfungsi untuk menyimpan beberapa objek playlist musik dalam suatu collection. Collection tersebut dibuat untuk memudahkan dalam mengelola objek-objek playlist musik. Class ini memiliki beberapa method, antara lain:
      - add_playlist(playlist): Metode ini digunakan untuk menambahkan sebuah video playlist ke dalam koleksi playlist.
      - remove_playlist(): Metode ini digunakan untuk menghapus playlist terakhir dalam koleksi.
      - search_playlist(title): Metode ini digunakan untuk mencari sebuah playlist berdasarkan judul.
      - get_all_playlists(): Metode ini digunakan untuk melihat semua playlist dalam koleksi.
      - sort_playlists(): Metode ini digunakan untuk mensortir atau mengurutkan semua playlist berdasarkan durasi.
   3. Login user
      Sebelum menggunakan program ini, user harus login terlebih dahulu. Program akan meminta username dan password untuk login. Username dan password telah didefinisikan pada bagian awal program.
   4. Menu tampilan
      Program ini memiliki menu tampilan yang terdiri dari 6 pilihan:
      - Menambahkan Vidio Kedalam Playlist: Pilihan ini digunakan untuk menambahkan sebuah  video playlist baru ke dalam koleksi playlist.
      - Hapus Playlist: Pilihan ini digunakan untuk menghapus playlist terakhir dalam koleksi.
      - Cari Playlist: Pilihan ini digunakan untuk mencari sebuah playlist berdasarkan judul.
      - Lihat Playlist: Pilihan ini digunakan untuk melihat semua playlist dalam koleksi.
      - Sort Playlist: Pilihan ini digunakan untuk mensortir semua playlist berdasarkan durasi.
      - Keluar: Pilihan ini digunakan untuk keluar dari program.

   Program ini memiliki beberapa fungsionalitas yang dapat membantu pengguna dalam mengelola playlist musik, antara lain:
   - Pengguna dapat menambahkan sebuah video playlist baru ke dalam koleksi playlist.
   - Pengguna dapat menghapus playlist terakhir dalam koleksi.
   - Pengguna dapat mencari sebuah playlist berdasarkan judul.
   - Pengguna dapat melihat semua playlist dalam koleksi.
   - Pengguna dapat mensortir semua playlist berdasarkan durasi.


D. Cara Penggunaan
   Berikut cara penggunaan program:
   1. Program ini dimulai dengan login terlebih dahulu dengan memasukkan username dan password yang sudah di definisikan di dalam program. yaitu dengan username "john" dengan password "12345" atau menggunakan username "jeane" dengan password "12345".
   2. Setelah berhasil login, program akan menampilkan menu pilihan yang terdiri dari 6 pilihan, yaitu:
     - Menambahkan Video Kedalam Playlist (1)
     - Hapus Playlist (2)
     - Cari Playlist (3)
     - Lihat Playlist (4)
     - Sort Playlist (5)
     - Keluar (6)
   3. Pilih salah satu dari ke enam pilihan tersebut, dengan memasukkan angka yang sesuai dengan pilihan yang diinginkan.
   4. Jika anda memasukkan pilihan 1(Menambahkan Video Kedalam Playlist) program akan meminta anda untuk memasukkan informasi tentang playlist yang ingin ditambahkan seperti judul playlist, artis, genre, dan durasi dari playlist. Setelah memasukkan informasi tersebut, playlist akan ditambakan kedalam koleksi playlist.
   5. Jika anda memasukkan pilihan 2(Hapus Playlist) program akan menghapus playlist terakhir dari koleksi playlist.
   6. Jika anda memasukkan pilihan 3(Cari Playlist) program akan meminta Anda untuk memasukkan judul playlist yang ingin Anda cari. Program akan menggunakan algoritma jump search untuk mencari playlist dengan judul yang sesuai. Jika playlist ditemukan, informasi tentang playlist tersebut akan ditampilkan di layar. Jika tidak ditemukan, program akan memberikan pesan bahwa playlist tidak ditemukan.
   7. Jika anda memasukkan pilihan 4(Lihat Playlist) program akan menampilkan semua playlist yang ada di dalam koleksi playlist. Jika koleksi playlist kosong, program akan memberikan pesan bahwa koleksi playlist kosong.
   8. Jika anda memasukkan pilihan 5(Sort Playlist) program akan mengurutkan semua playlist berdasarkan durasi dari playlist dengan menggunakan algoritma quick sort.
   9. Jika Anda memilih pilihan 6 (Keluar), maka program akan berhenti berjalan dan akan memberikan pesan "Anda Berhasil keluar".
   Demikianlah cara menggunakan program Youtube Music Playlist ini.