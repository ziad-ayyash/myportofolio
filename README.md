Nama : Muhammad Ziad Ayyash

NPM : 2506594364

Kelas : PBP C

---

## Tugas 6

1. REST (Representational State Transfer) adalah gaya arsitektur untuk merancang web API yang mendeskripsikan suatu _interface_ yang seragam antar komponen fisik yang berbeda, umumnya melalui internet dalam arsitektur _Client-Server_.

   Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON bukanlah gaya arsitektur untuk merancang web API, melainkan format data. Pengembalian JSON juga dapat melanggar sejumlah gagasan REST, contohnya.
      - **Data tidak diperlakukan sebagai resource.**, karena sembarang nama _path_ dapat diberikan ke suatu endpoint JSON, nama _path_ belum tentu merepresentasikan resource dengan benar.
      - **HTTP method tidak menyatakan tindakan.**, aksi masih tertulis di URL dan umumnya hanya memanfaatkan metode HTTP request `GET` dan `POST` saja, tidak memanfaatkan metode HTTP request lainnya.
   
   Untuk perbedaan `PUT` dan `PATCH`, `PUT` digunakan untuk mengirim representasi pengganti dan mewajibkan seluruh field dari suatu resource terisi. Sedangkan `PATCH` digunakan untuk mengirim representasi pengganti untuk field yang ingin diubah saja. Sehingga tidak mewajibkan semua field dari suatu resource terisi.

   `PUT` cocok digunakan untuk menggantikan atau memperbarui suatu resource sepenuhnya. Contohnya, memperbarui profil user di mana client memegang keadaan terbaru profil yang utuh. Sedangkan `PATCH` cocok digunakan untuk melakukan pembaruan kecil terhadap resource, contohnya memperbarui status pemesanan suatu paket.
   

2. Peran serializer adalah untuk mengubah objek menjadi data JSON (pada `GET`), serta memvalidasi dan menyimpan input (pada `POST`/`PATCH`). Serializer lebih _reusable_ dibandingkan merakit _dictionary_ secara manual. Pengiriman dan penerimaan resource juga tersentralisasi di satu tempat, sehingga sangat mudah untuk dikelola dan diperbarui.

3. Autentikasi adalah suatu proses untuk mengidentifikasi seorang pengguna. Pada DRF, proses ini dilakukan _authentication class_ dengan mengisi `request.user`. Sedangkan otorisasi adalah suatu proses untuk menentukan apa yang seorang pengguna diizinkan untuk melakukan. Pada DRF, proses ini dilakukan _permission class_ dengan memutuskan apakah request yang dikirim pengguna boleh diteruskan atau tidak.
   
   Hak akses tetap harus diperiksa dengan _permission class_ di server. Jika hanya sekadar menyembunyikan tombol di template, seorang pengguna tetap dapat melakukan aksi yang tidak diizinkan dengan mengirim request ke endpoint API.

4. Walaupun pengguna telah terautentikasi melalui `SessionAuthentication`, autentikasi hanya memastikan identitas pengguna berdasarkan _session_ yang valid, dan belum memastikan bahwa request tersebut memang berasal dari interaksi yang sah dengan aplikasi. Maka dari itu, perlindungan CSRF tetap harus digunakan untuk mencegah request yang dikirim tanpa sepengetahuan pengguna melalui mengeksploitasi _session_ pengguna.

   test yang memakai `force_authenticate` sepenuhnya melewati proses login, sehingga pengecekan CSRF juga terlewati. Namun, tes CSRF masih dapat dilakukan dengan memakai `APIClient(enforce_csrf_checks=True) `dan `.login()` yang membuat session sungguhan.

## AI USAGE
Tugas ini dikerjakan tanpa menggunakan AI, dengan referensi sebagai berikut.

- [**Tutorial 07**](https://pbp.cs.ui.ac.id/tutorial/tutorial-7.html#autentikasi-dan-otorisasi) | 
  Referensi utama untuk implementasi _Serializer_, _Permission_, API _View_, Integrasi REST API dengan halaman, serta _Tests_. Juga referensi untuk menjawab pertanyaan reflektif

- [**Dokumentasi DRF**](https://www.django-rest-framework.org/api-guide/fields/#datetimefield) | 
   Referensi cara membuat serializer menerima format `DateTime` tertentu dan _null_ untuk input field `ended_at` pada resource _experience_.

- [**Dokumentasi Django**](https://docs.djangoproject.com/en/6.1/ref/models/querysets/#:~:text=iexact) | 
   Referensi cara memfilter nama `Groups` dari `User` secara _case-insensitive_.

- [**W3Schools**](https://www.w3schools.com) | 
  Referensi [cara akses field pada variable `payload`](https://www.w3schools.com/jsref/jsref_object_fromentries.asp) dan [cara menggunakan `.querySelector()`](https://www.w3schools.com/jsref/met_document_getelementbyid.asp).

- [**PPT SCELE Materi 08 - Django REST Framework**](https://scele.cs.ui.ac.id/mod/resource/view.php?id=225745) | 
   Referensi tambahan untuk menjawab pertanyaan reflektif.

## PREVIOUS ASSIGNMENTS
- [Tugas #1](./pertanyaan%20reflektif/tugas01.md)
- [Tugas #2](./pertanyaan%20reflektif/tugas02.md)
- [Tugas #3](./pertanyaan%20reflektif/tugas03.md)
- [Tugas #4](./pertanyaan%20reflektif/tugas04.md)
- [Tugas #5](./pertanyaan%20reflektif/tugas05.md)