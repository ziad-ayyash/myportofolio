Nama : Muhammad Ziad Ayyash

NPM : 2506594364

Kelas : PBP C

---

## Tugas 5

1. Dengan implementasi sebelumnya, tiap query yang pengguna lakukan akan me-_refresh_ halaman tampilan. Menggunakan AJAX (Asynchronous JavaScript and XML), halaman tampilan dapat di-_update_ secara asinkronus tanpa me-_refresh_ seluruh halaman. Sehingga _load time_ dapat menjadi lebih cepat, konten halaman dapat menjadi lebih dinamis, dan secara keseluruhan membuat website menjadi lebih responsif. Karena dikendalikan JavaScript, _update_ halaman dilakukan setiap kali suatu event terjadi. Namun, hal tersebut dapat membuat server kewalahan. Debouncing adalah suatu teknik untuk menunda suatu fungsi skrip hingga suatu jeda waktu berlalu tanpa adanya event baru agar tidak terjadi spam request. Misal pada implementasi query pekan ini, timer akan terus ter-_reset_ apabila pengguna mengetik query. Namun pada saat pengguna berhenti mengetik hingga selang waktu tertentu, kita akan menampilkan hasil dari query tersebut. Tanpa teknik debouncing tiap huruf yang ditulis oleh pengguna akan me-_request_ data dari server.

Intinya, teknik debouncing penting diterapkan pada fitur pencarian agar website kita dapat terlihat lebih interaktif tanpa mengorbankan stabilitas dan performa website dengan mengurangi jumlah request query yang dikirim oleh pengguna ke server.

2. `await` adalah keyword yang hanya bisa digunakan di dalam async function, dan berfungsi untuk _“menunggu”_ Promise dari fungsi asinkronus, seperti `fetch()`, selesai diproses sebelum lanjut eksekusi kode setelahnya. Tanpa `await`, sebuah Promise akan tetap berjalan di belakang layar dan kode berikutnya yang mungkin membutuhkan hasilnya akan langsung dieksekusi. Hal tersebut dapat menyebabkan error atau luaran yang tidak sesuai.

3. Cross-Site Scripting (XSS) adalah serangan yang menyisipkan kode JavaScript ke dalam halaman web. `script` tersebut dieksekusi di browser korban dan menjalankan kode berbahaya dengan hak/izin yang setingkat dengan halaman web. _template_ Django otomatis melakukan auto-escaping pada setiap { variabel } yang dimasukkan. Penanggulangan tersebut tidak langsung tersedia saat kita beralih ke AJAX karena data dari JSON disisipkan ke dalam template literal yang tidak dimodifikasi kembali oleh Django. Hal tersebut membuat AJAX/JavaScript lebih rentan terhadap serangan XSS dibandingkan _template_ Django.

## AI USAGE
Tugas ini dikerjakan tanpa menggunakan AI, dengan mengandalkan informasi yang tersedia pada *Tutorial #5* yang disesuaikan untuk model terkait.

## PREVIOUS ASSIGNMENTS
- [Tugas #1](./pertanyaan%20reflektif/tugas01.md)
- [Tugas #2](./pertanyaan%20reflektif/tugas02.md)
- [Tugas #3](./pertanyaan%20reflektif/tugas03.md)
- [Tugas #4](./pertanyaan%20reflektif/tugas04.md)