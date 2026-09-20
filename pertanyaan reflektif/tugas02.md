## Tugas 2

1. Di dalam `myportofolio/settings.py`, kita telah menentukan bahwa `myportofolio/urls.py` akan bertindak sebagai `ROOT_URLCONF`, yaitu yang memetakan URL yang dimasukkan pengguna, menuju _view_ tertentu berdasarkan URL website. Karena sudah meng-_include_ `main/urls.py`, sebagian URL dipetakan oleh _urlpatterns_ milik `main/urls.py`. Setelah menemukan URL yang cocok, fungsi dari `views.py` akan dipanggil untuk menampilkan template tertentu pada pengguna. Template ditampilkan sesuai dengan context yang diberikan, yang dapat berupa informasi yang sudah ditentukan atau informasi _model_ yang berasal dari database yang sudah didefinisikan di `models.py`.

2. Model membantu dalam mengelola dan memelihara sistem aplikasi. Bayangkan apabila perlu menampilkan lebih dari 1000 item pada suatu laman web, template dari laman tersebut tentu akan menjadi sangat panjang dan tidak _readable_.. Model juga sangat memudahkan dalam menambahkan item baru. Tanpa model, _developer_ harus menambahkan item satu - satu di dalam sebuah file `html`. Menggunakan model, _developer_ hanya perlu membuat data model baru, membuat file migrasi, memasukkan data ke dalam context template, dan sisanya akan ditangani oleh Django sesuai dengan DTL _(Django Template Language)_, sehingga tidak ada repetisi penulisan kode.

3. `makemigrations` akan membuatkan file migrasi berdasarkan perubahan terhadap model yang kita lakukan pada `models.py`. File tersebut dinamakan secara _incremental_, contohnya `0001_initial.py`. File - file ini merepresentasikan perubahan pada skema basis data, dan `migrate` akan menerapkan file - file migrasi tersebut untuk memperbarui basis data. 

## AI USAGE
Tugas ini dikembangkan dengan bantuan AI (Claude Sonnet 5 - Free Plan). AI digunakan untuk memudahkan pencarian sumber dokumentasi, memeriksa bug, serta pencarian ide untuk pendekatan masalah. Keluaran AI TIDAK digunakan mentah-mentah untuk implementasi suatu fitur.

Contohnya, dalam tugas ini AI membantu mengimplementasi _tooltip_ pada status project.

Session yang digunakan untuk tugas ini dapat dilihat pada tautan [berikut.](https://claude.ai/share/678cdd38-b45b-43d3-87ca-accb555a0df9)

### References
- CSS Circle/Dot Trick https://www.w3schools.com/howto/howto_css_circles.asp
- DTL Syntax https://www.codecademy.com/learn/templates-in-django/modules/django-templates/cheatsheet
- Django Admin PWS implementation https://gist.github.com/RedStone576/90f5eb53acae3bc668d2ef3ea9205e3c
- How Migrations Work https://www.geeksforgeeks.org/python/django-basic-app-model-makemigrations-and-migrate/