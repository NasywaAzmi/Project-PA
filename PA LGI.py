import os
os.system('cls')

#akun1:john,12345
#akun2:jeane,12345

class video:
    def __init__(self, title):
        self.data = title
        self.video = None

    #Get Berfungsi Buat Getter untuk Atribut, Disebut get_title dsb
    def get_title(self):
        return self.data
    
    def set_title(self, title):
        self.data = str(title.title())

    def get_next_song(self):
        return self.video

    def set_next_song(self, next_title):
        self.video = next_title

    # Data Video
    def str(self):
        return str(self.data)

    # Menampilkan Urutan video
    def repr(self):
        return f"{self.data} -> {self.video}"

class Playlist:
    def __init__(self):
        self.head = None

    # Buat METHOD add_video Membuat Objek video dan Menambahkan Ke Daftar Putar. Metode ini Memiliki 1 Parameter Yaitu TITLE
    def add_video(self, title):
        video_baru = video(title)
        video_baru.set_title(title)
        video_baru.set_next_song(self.head)
        self.head = video_baru

    # Buat METHOD find_song yang Mencari Apakah video Keluar dari Playlist dan Mengembalikan indeksnya. Method ini mempunyai Parameter juga yaitu TITLE 
    def find_song(self, title):
        song = self.head
        index = 0
        if self.length() is None:
            return -1
        else:
            while song:
                if song.get_title() == title:
                    return index
                else:
                    index += 1
                    song = song.get_next_song()
            return -1



  #Buat Method remove_song Yang Menghapus video dari Playlist. Method ini Mempunyai Parameter TITLE, yaitu video yang harus di Hapus 
    def remove_song(self, title):
        song = self.head

        if song == None:
            return print('Tidak Ada Video Didalam Playlist. Harap Menambahkan Video Terlebih Dahulu.')
        elif song.get_title() == title: 
            self.head = song.get_next_song()
            return print(f'Video {title} berhasil dihapus dari Playlist')
        else: 
            song = song.get_next_song()

    # Method length, Mengembalikan jumlah video Dalam Playlist 
    def length(self):
        index = 0
        song = self.head

        while song != None:
            index += 1
            song = song.get_next_song()
        return index


    # Method print_video,Mencetak Playlist Bernomor di Playlist
    # Contoh:
    # 1. Judul video  1
    # 2. Judul video 2
    # 3. Judul video 3

    def print_video(self):
        index = 1
        song = self.head
        if song == None:
            print(f"==========================================================")
            print(f"Tidak Ada Video Didalam Playlist. Silahkan Tambahkan Video dahulu")
            print(f"==========================================================")
            return None
        while song:
            print(f"{index}. {song.get_title()}")
            index += 1
            song = song.get_next_song()

    def print_linkedlist(self):
        if self.head is None:
            print("Tidak Ada Video Didalam Playlist.")
            
        else:
            n = self.head
            while n is not None:
                print(n.repr(), end=" ---> ")
                n = n.repr()

playlist = Playlist()
users = {
    "john": "12345",
    "jeane": "12345"
}

# Login user
while True:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username] == password:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah.")

while True:
    # Pilihan menu awal
    print('''
    I=====================================I
    I    * * * Youtube Playlist * * *     I
    I=====================================I
    Pilihan :
    1: Menambahkan Vidio Kedalam Playlist
    2: Lihat isi Playlist
    3: Menghapus Vidio Dari Playlist
    4: Mencari Vidio Didalam Playlist
    5: Melihat Jumlah Vidio Dalam Playlist
    6: Keluar
    =====================================
    ''')

    # Pilihan inputan user
    Pilihan = input('Silahkan masukkan pilihan anda : ')
    if Pilihan.isnumeric():
        Pilihan = int(Pilihan)
    print()


    # Pilihan 1: Untuk Menambahkan video Pada Playlist
    if Pilihan == 1:
        pilihan2 = input('Judul Video yang ingin ditambahkan : ')
        playlist.add_video(pilihan2)
        
    # Pilihan 2: Untuk melihat playlist
    elif Pilihan == 2:
        playlist.print_video()

    # Pilihan 3: Untuk Menghapus video Pada Playlist
    elif Pilihan == 3:
        pilihan3 = input('Judul video yang ingin dihapus :  ')
        print(playlist.remove_song(pilihan3))

    # Pilihan 4: Untuk Mencari video Pada Playlist
    elif Pilihan == 4:
        pilihan4 = input('Judul video yang ingin dicari :  ')
        index = playlist.find_song(pilihan4)
        if index == -1:
            print(f"Judul video {pilihan4} Tidak Ada Didalam Playlist.")
        else:
            print(f"Judul video {pilihan4} Berada Pada Nomor {index+1}")

    # Pilihan 5: Untuk Melihat Urutan Playlist
    elif Pilihan == 5:
        print(f"Terdapat {playlist.length()} Judul video Dalam Playlist.")

    # Pilihan 6: Untuk Keluar  
    elif Pilihan == 6:
        print(f"Berhasil keluar.")
        break
    
    # Else jika pilihan tidak sesuai 
    else:
        print('Pilihan Tidak Valid Silahkan Masukkan Pilihan Dengan Benar!!!.\n')
