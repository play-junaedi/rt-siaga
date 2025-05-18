# 🖥️ 1. Wireframe Web Admin Dashboard

## 🔐 Halaman Login
```
+-------------------------------------+
|         RT-Siaga - Admin Login      |
+-------------------------------------+
| Email:   [_______________________]  |
| Password:[_______________________]  |
| [Masuk]        [Lupa Password?]     |
+-------------------------------------+
```

---

## 🏠 Dashboard Utama
```
+---------------------------------------------------+
| Header: Logo | Notifikasi Bell | Profil Dropdown |
+---------------------------------------------------+

+----------------------------+
| Menu Sisi Kiri             |
+----------------------------+
| - Beranda                  |
| - Kelola Warga             |
| - Forum Moderasi           |
| - Pengumuman               |
| - Manajemen CCTV           |
| - Struktur Organisasi      |
| - Riwayat SOS              |
| - Laporan & Statistik      |
+----------------------------+

+-------------------------------------------+
| Beranda - Ringkasan Cepat                 |
| +------------------+                      |
| | Total Warga      | 200 orang           |
| | Pengumuman Baru  | 3                   |
| | SOS Hari Ini     | 5                   |
| | Aktivitas Terakhir                    |
| | - Moderator hapus jawaban spam        |
| | - Pengumuman "Vaksinasi Massal" terkirim|
+-------------------------------------------+
```

---

## 👤 Kelola Akun Warga
```
+-------------------------------------------+
| Filter: Status (Aktif / Nonaktif)        |
| Cari Nama / Email                        |
+-------------------------------------------+

+----------------------------------------------------------------------------------+
| Daftar Warga                                                                   |
| No | Nama    | Email            | Role   | Status    | Aksi (Edit / Blokir)  |
+----------------------------------------------------------------------------------+
| 1  | Budi    | budi@email.com   | Warga  | Aktif     | [Blokir]              |
| 2  | Ani     | ani@email.com    | RT     | Aktif     | [Nonaktifkan]         |
+----------------------------------------------------------------------------------+

[ Tambah Manual Akun ] [ Export CSV ]
```

---

## 💬 Moderasi Forum
```
+-----------------------------------------------------------------------------+
| Filter: Semua / Belum Dijawab / Dilaporkan                                 |
+-----------------------------------------------------------------------------+

+----------------------------------------------------------------------------------------+
| Pertanyaan #1                                                                     |
| Oleh: Andi | 2 jam lalu | Dilaporkan? ✅                                         |
| "Bagaimana cara daftar BPJS kesehatan?"                                           |
| Jawaban:                                                                          |
| - Jawaban oleh Sinta: "Langkahnya..."                                             |
| - Jawaban oleh Toni: "Silakan ke puskesmas..."                                    |
| [Hapus Pertanyaan] [Sembunyikan Jawaban]                                          |
+----------------------------------------------------------------------------------------+
```

---

## 📢 Pengelolaan Pengumuman
```
+-------------------------------------------+
| Judul: [Pengumuman Gotong Royong Sabtu]  |
| Isi:                                     |
| [Textarea besar untuk isi pengumuman...] |
| Lampiran: [lampiran.pdf]                 |
| Tanggal Kirim: [Tanggal dan Jam]         |
| [Simpan] [Kirim Sekarang]                |
+-------------------------------------------+

+-------------------------------------------+
| Riwayat Pengumuman                        |
| Judul                     | Status        |
|-------------------------------------------|
| Vaksinasi Massal          | Terkirim      |
| Rapat RT Bulanan          | Jadwal        |
+-------------------------------------------+
```

---

## 📹 CCTV Management
```
+-------------------------------------------+
| Daftar Kamera CCTV                        |
| Nama       | Lokasi       | Status       |
|-------------------------------------------|
| Pintu Masuk| Depan Gang   | Online       |
| Pos RT     | Samping Kantor| Offline      |
+-------------------------------------------+
[ Tambah Kamera ] → Input: URL RTSP, Label Lokasi

+-------------------------------------------+
| Live Streaming Viewer                   |
| [Area Video Stream]                     |
| Keterangan: “Streaming dari: Pintu Masuk”|
+-------------------------------------------+
```

---

## 🏛️ Struktur Organisasi
```
+-------------------------------------------+
| Jabatan        | Nama        | Masa Jabatan |
|-------------------------------------------|
| Ketua RT       | Andi Susilo | Jan 2023 – Des 2025 |
| Sekretaris     | Budi Cahya  | Jan 2023 – Des 2025 |
+-------------------------------------------+
[ Tambah Jabatan ] → Form: Nama Jabatan, Pilih Warga, Tanggal Mulai/Akhir
```

---

# 📱 2. Wireframe Mobile App (Warga)

## 🔐 Halaman Login
```
+-------------------------------------+
|         RT-Siaga - Warga Login      |
+-------------------------------------+
| Email:   [_______________________]  |
| Password:[_______________________]  |
| [Masuk]        [Lupa Password?]     |
+-------------------------------------+
```

---

## 🏠 Dasbor Utama
```
+---------------------------------------------------+
| Header: Logo | Notifikasi Bell | Profil Icon     |
+---------------------------------------------------+

+--------------------------+
| Tombol SOS Darurat       |
| [🆘 SOS]                 |
+--------------------------+

+---------------------------------------+
| Menu Utama                            |
| [❓ Forum] [📹 CCTV] [📣 Pengumuman]   |
| [🏛️ Organisasi] [🤖 Chatbot] [🔔 Notif]|
+---------------------------------------+
```

---

## 🆘 Tombol SOS
```
+-------------------------------------------+
| Tombol SOS                                |
| [🔴 Tekan dan Tahan untuk SOS]            |
| Atau tekan cepat 3x dalam 3 detik         |
+-------------------------------------------+

+-------------------------------------------+
| Riwayat SOS                               |
| Tanggal        | Lokasi       | Status   |
|-------------------------------------------|
| 20 Apr 2025    | -6.123, 106.45| Selesai  |
| 18 Apr 2025    | -6.124, 106.46| Dibatalkan|
+-------------------------------------------+
```

---

## ❓ Forum QnA
```
+-------------------------------------------+
| Forum Diskusi Warga                       |
+-------------------------------------------+
[ Cari Pertanyaan ... ]

+-------------------------------------------+
| Pertanyaan #1                             |
| Oleh: Andi | 2 jam lalu | 3 jawaban       |
| "Cara buat surat domisili?"               |
| [Lihat Detail]                            |
+-------------------------------------------+

+-------------------------------------------+
| [➕ Ajukan Pertanyaan Baru]                |
+-------------------------------------------+
```

---

## 📺 CCTV Streaming
```
+-------------------------------------------+
| Streaming CCTV                            |
+-------------------------------------------+
[ Pilih Kamera ] → Dropdown lokasi

+-------------------------------------------+
| [Live Video Area]                         |
| Informasi waktu real-time di kamera       |
| [Pause] [Fullscreen]                      |
+-------------------------------------------+
```

---

## 📣 Pengumuman
```
+-------------------------------------------+
| Daftar Pengumuman                         |
+-------------------------------------------+

+-------------------------------------------+
| Pengumuman 1                              |
| Judul: "Gotong Royong Sabtu Besok"        |
| Tanggal: 20 Apr 2025                      |
| Isi: "Seluruh warga dimohon hadir..."     |
| [Bookmark] [Bagikan ke WA]                |
+-------------------------------------------+
```

---

## 🤖 AI Chatbot
```
+-------------------------------------------+
| Chat dengan AI Bot                        |
+-------------------------------------------+
| Halo! Saya siap bantu pertanyaan Anda.    |

+-------------------------------------------+
| [Input]: "Cara daftar vaksin?"            |
| [Send]                                    |
+-------------------------------------------+

+-------------------------------------------+
| Jawaban:                                  |
| "Anda bisa mendaftar melalui posyandu..." |
+-------------------------------------------+
```

---

## 🔔 Notifikasi
```
+-------------------------------------------+
| Riwayat Notifikasi                        |
+-------------------------------------------+

+-------------------------------------------+
| [🔔] SOS dari tetangga dekat rumah Anda   |
| 10 menit lalu                             |
+-------------------------------------------+

+-------------------------------------------+
| [📢] Pengumuman baru: "Rapat RT hari ini" |
| 1 jam lalu                                |
+-------------------------------------------+

+-------------------------------------------+
| [💬] Jawaban untuk pertanyaan Anda        |
| "Cara daftar listrik prabayar"            |
+-------------------------------------------+
```

---

## 🧑‍💼 Struktur Organisasi
```
+-------------------------------------------+
| Jabatan        | Nama        | Kontak     |
|-------------------------------------------|
| Ketua RT       | Andi Susilo | [📞 Call]  |
| Bendahara      | Siti Rahma  | [📧 Email]  |
+-------------------------------------------+

+-------------------------------------------+
| Riwayat Jabatan                           |
| Andi Susilo - Ketua RT (2021–2023)        |
| Budi Prasetyo - Ketua RT (2019–2021)      |
+-------------------------------------------+
```