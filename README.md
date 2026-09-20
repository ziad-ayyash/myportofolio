Nama : Muhammad Ziad Ayyash

NPM : 2506594364

Kelas : PBP C

---

## Tugas 3

1. Sebelumnya, modifikasi model dalam basis data dilakukan melalui `python manage.py shell`. Dengan Form, proses tersebut dapat dilakukan dengan komunikasi antar _client_ dengan _server_ melalui form. Jika membuat form html secara manual, kita harus memroses data (validasi,  konversi tipe data, dll), membuat objek, serta menangani _error_ secara manual. `ModelForm` Django menangani semua hal tersebut secara otomatis serta memberikan kita pilihan untuk men-_generate_ form html sehingga tidak perlu banyak mengetik ulang kode. `CSRF Token` merupakan token unik rahasia yang dibuat oleh server untuk melindungi aplikasi dari request yang tidak terautorisasi. `CSRF Token` mencegah penyerang aplikasi mengubah request yang awalnya ke server Django website kita menjadi ke suatu API yang berbahaya yang misalnya ingin mencuri data.

2. JSON lebih disukai dibandingkan XML pada aplikasi modern, terutama pada arsitektur _RESTful API_, karena ukurannya yang lebih ringkas, kemampuannya untuk di _parse_ dengan cepat, serta keserasiannya dengan JavaScript di sisi frontend. Sintaks JSON juga sangat sederhana yaitu hanya berupa pasangan `key` dan `value`

3. Saat fungsi _view_ untuk mengembalikan data dipanggil (dalam kasus ini, melalui _URL path_), pertama - tama data yang relevan akan diambil dari basis data (`models = Model.objects.all()`). Setelah itu, jika ada, data yang sudah diambil akan difilter kembali berdasarkan _query_ yang tersedia. Kemudian, data di _serialize_ untuk mengubahnya dari yang awalnya object Python menjadi bentuk format JSON (`models_json = serializers.serialize("json", models)`). Terakhir, fungsi akan mengembalikan output berupa respons HTTP untuk dikirim ke client (`return HttpResponse(modles_json, content_type="application/json")`). Tentunya, karena hanya bisa berupe byte, respons HTTP tidak dapat berupa object python secara mentah. Oleh karena itu, object harus diubah dulu ke format yang bisa direpresentasikan dengan byte, seperti JSON, melalui _serialization_ agar bisa dikirim sebagai respons HTTP. Penerima dapat mengelola data dengan mudah karena kita mengirim respons HTTP dengan format yang sudah terstandarisasi.

## AI USAGE
Tugas ini dikembangkan dengan bantuan AI (Claude Sonnet 5 - Free Plan). AI digunakan untuk memudahkan pencarian sumber dokumentasi, memeriksa bug, serta pencarian ide untuk pendekatan masalah. Keluaran AI TIDAK digunakan mentah-mentah untuk implementasi suatu fitur.

Contohnya, dalam tugas ini AI membantu mengimplementasi _field_ berjenis _choice_ dan _date_ dalam suatu form. AI merekomendasi saya menghias _field_ tersebut dengan memberikannya class. Saya memilih untuk langsung men-_select_ tag terkait pada `style.css` agar nantinya tiap _field_ baru yang ditambahkan secara default memiliki style yang sudah ditentukan.

Session yang digunakan untuk tugas ini dapat dilihat pada tautan [berikut.](https://claude.ai/share/e0d74cea-aace-4b03-b4a0-8c78e511380d)

## PREVIOUS ASSIGNMENTS
- [Tugas #1](./pertanyaan%20reflektif/tugas01.md)
- [Tugas #2](./pertanyaan%20reflektif/tugas02.md)