from functions import *

def tambah_game(list_game, user_data):
    # Sudah login
    if user_data != []:
        is_admin = validasi_akses(user_data)
        if is_admin:
            nama_game = input("Masukkan nama game: ")
            kategori = input("Masukkan kategori: ")
            tahun_rilis = input("Masukkan tahun rilis: ")
            harga = input("Masukkan harga: ")
            stok_awal = input("Masukkan stok awal: ")

            # Ada input yang kosong
            while nama_game == "" or kategori == "" or tahun_rilis == "" or harga == "" or stok_awal == "":
                print("Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO.")
                nama_game = input("Masukkan nama game: ")
                kategori = input("Masukkan kategori: ")
                tahun_rilis = input("Masukkan tahun rilis: ")
                harga = input("Masukkan harga: ")
                stok_awal = input("Masukkan stok awal: ")
            else:
                # Game ID generator
                game_id = len(list_game) + 1
                if game_id < 10:
                    game_id = "GAME00" + str(game_id)
                elif game_id < 100:
                    game_id = "GAME0" + str(game_id)
                else:
                    game_id = "GAME" + str(game_id)

                try:
                    # Untuk membenarkan/menambahkan peletakan titik pada <harga>
                    harga = convert(harga, int)
                    harga = convert(harga, str)

                    # Cek apakah tahun rilis dan stok berupa angka
                    int(tahun_rilis)
                    int(stok_awal)

                    print("Selamat! Berhasil menambahkan game " + nama_game)
                    new_game = [game_id, nama_game, kategori, tahun_rilis, harga, stok_awal]
                    list_game = append(list_game, new_game)
                except:
                    print("Format penulisan tahun rilis, harga, dan stok harus berupa angka.")
        else:
            print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    # Belum login
    else:
        print('Maaf, anda harus login terlebih dahulu untuk mengirim perintah selain "login".')
    return list_game