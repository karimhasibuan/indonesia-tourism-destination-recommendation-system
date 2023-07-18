# Laporan Proyek Machine Learning - Karimuddin Hakim Hasibuan

## Project Overview

Indonesia merupakan negara kepulauan dengan beragam kekayaan alam dan budaya yang menarik bagi wisatawan lokal maupun internasional sebagai destinasi tempat wisata. Objek wisata adalah segala sesuatu yang ada di daerah tujuan wisata yang merupakan daya tarik agar orang-orang ingin datang berkunjung ke tempat tersebut [[1]](https://www.jurnal.ummu.ac.id/index.php/kawasa/article/view/443).

Objek dan daya tarik wisata menurut Undang-undang No 10 tahun 2009 tentang kepariwisataan yaitu daya tarik wisata adalah segala sesuatu yang memiliki keunikan, keindahan, dan nilai yang berupa keanekaragaman kekayaan alam, budaya, dan hasil buatan manusia yang menjadi sasaran atau tujuan kunjungan wisatawan dan daerah tujuan pariwisata yang selanjutnya disebut destinasi pariwisata [[2]](https://ejurnal.bunghatta.ac.id/index.php/JMN/article/view/16895/14264).

Berbagai banyaknya pilihan tempat wisata di Indonesia tak jarang menyebabkan calon wisatawan sering mengalami kesulitan dalam memilih tempat wisata yang sesuai dengan minat dan preferensi mereka. Hal ini disebabkan oleh beberapa faktor, termasuk keterbatasan informasi yang tersedia, kebanyakannya informasi yang bersifat umum dan tidak personal, serta kebingungan dalam mengidentifikasi tempat-tempat yang benar-benar menarik di antara banyaknya pilihan [[3]](https://scholar.archive.org/work/7w2m5zoz5jb75phn6soimle3oy/access/wayback/https://ejournal.unisnu.ac.id/JDPT/article/download/1258/pdf).

Berdasarkan permasalahan diatas, penulis melakukan proyek pengembangan sistem rekomendasi tempat wisata di Indonesia. Proyek ini bertujuan untuk membantu pengguna dengan menyaring informasi dan menyajikan rekomendasi yang sesuai dengan preferensi mereka sehingga meningkatkan pengalaman wisatawan yang memuaskan dan mampu meningkatkan promosi dan pemasaran destinasi wisata.

Sistem yang dikembangkan menggunakan teknik-teknik dalam bidang pemrosesan bahasa alami, analisis data, dan kecerdasan buatan untuk memberikan rekomendasi yang personal dan relevan kepada pengguna seperti _Content-based Filtering_ dan _Collaborative Filtering_. _Content-based filtering_ memberikan suatu rekomendasi berdasarkan hasil analisa kemiripan item yang telah dinilai oleh para penggunanya [[4]](https://scholar.archive.org/work/gxrj3ap7z5ashl3xj57kllenk4/access/wayback/https://ejurnal.mikroskil.ac.id/index.php/jsm/article/download/816/pdf). Sedangkan, _Collaborative filtering_ adalah suatu konsep dimana opini dari pengguna lain yang ada digunakan untuk memprediksi item yang mungkin disukai/diminati oleh seorang pengguna [[5]](https://ejournal.undip.ac.id/index.php/jmasif/article/view/31482). Teknik ini mampu memberikan hasil yang signifikan dalam meningkatkan pengalaman penelurusan pengguna yang dipersonalisasi [[6]](https://ieeexplore.ieee.org/abstract/document/7254144).

## Business Understanding

### Problem Statements

Berdasarkan latar belakang yang telah diuraikan sebelumnya, maka terdapat rumusan masalah sebagai berikut:

- Bagaimana membuat sistem rekomendasi dengan yang dipersonalisasi berdasarkan data wisatawan dan tempat wisata yang dikunjungi?

- Bagaimana sistem merekomendasikan destinasi wisata lain yang mungkin disukai oleh calon wisatawan yang belum pernah mengunjungi tempat tersebut?

### Goals

Melalui latar belakang dan solusi yang ditawarkan, terdapat tujuan yang ingin dicapai sebagai berikut:

- Memahami pendekatan teknik yang digunakan dalam mengembangkan sistem rekomendasi tempat wisata di Indonesia.

- Mengembangkan sistem rekomendasi tempat wisata yang ada di Indonesia secara personal dan relevan sehingga meningkatkan pengalaman wisatawan dalam memilih tempat wisata.

### Solution Approach

Pada proyek ini, penulis menggunakan teknik _Content-based Filtering_ dan _Collaborative Filtering_ dalam mengembangkan sistem rekomendasi tempat wisata di Indonesia. Berikut penjelasan lebih mendalam mengenai _Content-based Filtering_ dan _Collaborative Filtering_ sebagai solusi yang ditawarkan dalam mengembangkan sistem rekomendasi tempat wisata di Indonesia:

- _Content-based Filtering_:
  _Content-based Filtering_ adalah metode dalam sistem rekomendasi yang menggunakan informasi tentang item yang direkomendasikan dan preferensi pengguna untuk memberikan rekomendasi yang sesuai. Metode ini menganalisis fitur-fitur atau konten dari item untuk menentukan kemiripan antara item tersebut dengan preferensi pengguna [[7]](http://e-journal.hamzanwadi.ac.id/index.php/edumatic/article/view/2162/1162).

  Cara kerja _Content-based Filtering_ dimulai dengan ekstraksi fitur dari item-item yang akan direkomendasikan, seperti lokasi geografis, jenis wisata, fasilitas, harga, ulasan, dan lain sebagainya. Kemudian, profil pengguna dibentuk berdasarkan preferensi pengguna terhadap item-item yang sudah diketahui. Setelah itu, perhitungan kemiripan antara item-item dengan profil pengguna dilakukan menggunakan metrik seperti _euclidean distance_ atau _cosine similarity_. Item yang memiliki kemiripan tertinggi dengan profil pengguna akan direkomendasikan [[8]](https://ieeexplore.ieee.org/abstract/document/9321202).

  Kelebihan dari _Content-based Filtering_ adalah kemampuannya memberikan rekomendasi yang personal dan relevan. Metode ini mempertimbangkan preferensi pengguna dan mengadaptasi rekomendasi dengan karakteristik item yang diinginkan [[9]](https://www.ijcaonline.org/archives/volume110/number4/19308-0760).

- _Collaborative Filtering_:
  _Collaborative Filtering_ adalah metode dalam sistem rekomendasi yang menggunakan informasi dari pengguna lain untuk memberikan rekomendasi kepada pengguna. Metode ini mencari pola dan hubungan antara preferensi pengguna secara kolektif untuk membuat rekomendasi yang sesuai [[10]](https://ieeexplore.ieee.org/abstract/document/10054282).

  Cara kerja _Collaborative Filtering_ melibatkan pengumpulan data preferensi pengguna terhadap item-item yang ada. Berdasarkan data ini, pengguna yang memiliki pola preferensi yang mirip dengan pengguna yang akan direkomendasikan diidentifikasi. Kemudian, item-item yang disukai oleh pengguna-pengguna mirip yang belum diketahui oleh pengguna yang akan direkomendasikan dianggap sebagai item yang potensial untuk direkomendasikan [[11]](https://dl.acm.org/doi/fullHtml/10.1145/3482632.3487539).

  Kelebihan dari _Collaborative Filtering_ adalah kemampuannya dalam menemukan item yang baru atau tidak pernah diketahui oleh pengguna. Metode ini mengandalkan kebijaksanaan kolektif pengguna untuk memberikan rekomendasi [[12]](https://www.ijcaonline.org/archives/volume167/number12/sang-2017-ijca-914490.pdf).

Penggunaan teknik _Content-based Filtering_ pada proyek ini adalah dalam memberikan rekomendasi yang dipersonalisasi berdasarkan data wisatawan dan tempat wisata yang dikunjungi. Sedangkan, teknik _Collaborative Filtering_ untuk merekomendasikan destinasi wisata lain yang mungkin disukai oleh calon wisatawan yang belum pernah mengunjungi tempat tersebut.

## Data Understanding

_Dataset_ yang digunakan pada proyek ini adalah [_Indonesia Tourism Destination_](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination?select=user.csv) yang bersumber dari situs Kaggle. _Dataset_ ini terdiri dari 4 _file_, yaitu `package_tourism.csv`, `tourism_rating.csv`, `tourism_with_id.csv` dan `user.csv`. Berikut informasi mengenai jumlah kolom dan data pada setiap _file_ dapat dilihat pada Tabel 1.

Tabel 1. Jumlah kolom dan data pada masing-masing _file_.

| No. | Nama _File_         | Jumlah Kolom | Jumlah Data |
| --- | ------------------- | ------------ | ----------- |
| 1   | package_tourism.csv | 7            | 100         |
| 2   | tourism_rating.csv  | 3            | 10,000      |
| 3   | tourism_with_id.csv | 12           | 437         |
| 4   | user.csv            | 3            | 300         |

Berdasarkan informasi pada Tabel 1 maka dapat dijabarkan variabel pada masing-masing _file_ sebagai berikut:

1. Variabel pada `package_tourism.csv` berisi informasi tentang paket rekomendasi tempat terdekat berdasarkan waktu, biaya, dan _rating_.

   - `Package` merupakan data paket destinasi wisata.
   - `City` merupakan data kota pada paket destinasi wisata.
   - `Place_Tourism1` merupakan data tempat destinasi wisata pertama.
   - `Place_Tourism2` merupakan data tempat destinasi wisata kedua.
   - `Place_Tourism3` merupakan data tempat destinasi wisata ketiga.
   - `Place_Tourism4` merupakan data tempat destinasi wisata keempat.
   - `Place_Tourism5` merupakan data tempat destinasi wisata kelima.

2. Variabel pada `tourism_rating.csv` berisi informasi tentang pengguna yang memberikan _rating_ pada suatu tempat wisata.

   - `User_Id` merupakan data _id_ wisatawan yang memberikan _rating_.
   - `Place_Id` merupakan data _id_ tempat wisata yang diberikan _rating_.
   - `Place_Ratings` merupakan data _rating_ tempat wisata.

3. Variabel pada `tourism_with_id.csv` berisi informasi tentang tempat wisata di 5 kota besar yaitu Yogyakarta, Bandung, Jakarta, Semarang dan Surabaya.

   - `Place_Id` merupakan data _id_ tempat wisata.
   - `Place_Name` merupakan data nama tempat wisata.
   - `Description` merupakan data deskripsi tempat wisata.
   - `Category` merupakan data kategori tempat wisata.
   - `City` merupakan data kota tempat wisata berada.
   - `Price` merupakan data harga tempat wisata.
   - `Rating` merupakan data _rating_ tempat wisata.
   - `Time_Minutes` merupakan data durasi waktu berwisata.
   - `Coordinate` merupakan data koordinat tempat wisata.
   - `Lat` merupakan data _latitude_ tempat wisata.
   - `Long` merupakan data _longitude_ dari tempat wisata.
   - `Unnamed: 11` merupakan data tanpa penjelasan.
   - `Unnamed: 12` merupakan data tanpa penjelasan.

4. Variabel pada `user.csv` berisi informasi tentang data lokasi dan umur dari pengguna.
   - `User_Id` merupakan data _id_ dari pengguna.
   - `Location` merupakan data lokasi pengguna.
   - `Age` merupakan data umur pengguna.

Berdasarkan data yang digunakan diatas dilakukan representasi data dalam bentuk tabel serta visualisasi untuk membantu memahami data, contoh visualisasi yang digunakan adalah _line chart_. _Line Chart_ merupakan bentuk visualisasi statistik yang bertujuan untuk menampilkan data yang berkelanjutan dengan periode atau rentang nilai tertentu. Garis yang dihasilkan dapat menunjukkan tren kenaikan atau penurunan pada data. Misalnya pada Gambar 1, terdapat empat data penjualan tahunan per kuartal selama 3 bulan yang terlihat mengalami kenaikan setiap bulannya.

[![line-chart.png](https://i.postimg.cc/1zFycnDW/line-chart.png)](https://postimg.cc/cKsqdJ9Y)

Gambar 1. Contoh bentuk _line chart_ [[13]](https://bitlabs.id/blog/diagram-garis-adalah/).

## Data Preparation

Tahapan data preparation yang dilakukan pada proyek ini dapat dijabarkan sebagai berikut:

**1. Melakukan EDA (_Exploratory Data Analysis_), bertujuan untuk mendapatkan informasi fitur mengenai _dataset_ yang digunakan.**

Pada tahapan ini diperlihatkan hasil dari setiap tahapan EDA pada _dataset_ `package_tourism`. Tahapan ini juga diterapkan pada _dataset_ `tourism_rating`, `tourism_with_id`, dan `user`.

**1.1.1. Memeriksa tipe data setiap kolom.**

Tabel 2. stuktur data pada data `package_tourism`.

| _Column_       | _Count_ | _Dtype_ |
| -------------- | ------- | ------- |
| Package        | 100     | int64   |
| City           | 100     | object  |
| Place_Tourism1 | 100     | object  |
| Place_Tourism2 | 100     | object  |
| Place_Tourism3 | 100     | object  |
| Place_Tourism4 | 66      | object  |
| Place_Tourism5 | 39      | object  |

Penjelasan dari Tabel 2 adalah sebagai berikut:

- Kolom `Package` berisi nilai _integer_ (int64) dan memiliki 100 data.
- Kolom `City` berisi data berupa teks atau _string_ (_object_) dan memiliki 100 data.
- Kolom `Place_Tourism1` berisi data berupa teks atau _string_ (_object_) dan memiliki 100 data.
- Kolom `Place_Tourism2` berisi data berupa teks atau _string_ (_object_) dan memiliki 100 data.
- Kolom `Place_Tourism3` berisi data berupa teks atau _string_ (_object_) dan memiliki 100 data.
- Kolom `Place_Tourism4` berisi data berupa teks atau _string_ (_object_) dan memiliki 66 data. Terdapat 34 nilai _null_ atau kosong pada kolom ini.
- Kolom `Place_Tourism5` berisi data berupa teks atau _string_ (_object_) dan memiliki 39 data. Terdapat 61 nilai _null_ atau kosong pada kolom ini.

Dengan melihat tabel di atas, kita dapat mengetahui informasi tentang struktur dataset, jumlah data yang kosong (null), dan tipe data dari setiap kolom. Hal ini penting untuk melakukan analisis data lebih lanjut atau mempersiapkan data sebelum dilakukan pemodelan.

**1.1.2. Menampilkan sebaran statistik deskriptif pada kolom numerik, yaitu kolom `Package`.**

Tabel 3. Distribusi statistik pada kolom `Package`.

|       | _Package_  |
| ----- | ---------- |
| count | 100.000000 |
| mean  | 50.500000  |
| std   | 29.011492  |
| min   | 1.000000   |
| 25%   | 25.750000  |
| 50%   | 50.500000  |
| 75%   | 75.250000  |
| max   | 100.000000 |

Tabel 3 menunjukkan informasi terkait distribusi data dari 100 entri. Rata-rata nilai `Package` adalah 50.5 dengan standar deviasi sebesar 29.01, menandakan bahwa data memiliki variasi yang cukup signifikan. Nilai minimum adalah 1 dan nilai maksimum adalah 100, menunjukkan rentang nilai yang luas. Kuartil pertama (25%) terletak pada 25.75, median (50%) berada pada nilai 50.5, dan kuartil ketiga (75%) berada pada 75.25. Dengan demikian, setengah dari data berada di bawah nilai median, sementara setengahnya lagi berada di atasnya. Informasi ini memberikan gambaran tentang distribusi dan karakteristik data pada kolom `Package`.

**1.1.3. Menampilkan jumlah data unik pada setiap kolom.**

Tabel 4. Jumlah data unik pada setiap kolom di data `package_tourism`.

| Kolom          | Jumlah |
| -------------- | ------ |
| Package        | 100    |
| City           | 5      |
| Place_Tourism1 | 89     |
| Place_Tourism2 | 93     |
| Place_Tourism3 | 92     |
| Place_Tourism4 | 61     |
| Place_Tourism5 | 38     |

Pada Tabel 4, dapat diketahui jumlah data unik pada masing-masing kolom. Pertama, pada kolom `Package` terdapat 100 data unik, menandakan adanya 100 jenis paket dalam _dataset_ ini. Selanjutnya, kolom `City` memiliki 5 data unik, yang mengindikasikan bahwa _dataset_ ini mencakup 5 kota berbeda tempat berbagai tempat wisata berada. Kemudian, kolom `Place_Tourism1` hingga `Place_Tourism5` memiliki masing-masing 89, 93,92, 61 dan 38 data unik. Angka ini menunjukkan adanya variasi tempat wisata yang cukup signifikan dalam _dataset_ ini, yang dapat memberikan informasi tentang beragamnya destinasi yang ditawarkan. Hal ini bertujuan untuk memahami variasi dan distribusi nilai pada suatu kolom atau atribut dalam _dataset_.

**1.1.4. Menampilkan jumlah data deskriptif dari setiap kolom.**

Tabel 5. Sebaran data deskriptif pada kolom `City`.

| Kota       | Jumlah |
| ---------- | ------ |
| Jakarta    | 20     |
| Yogyakarta | 20     |
| Bandung    | 20     |
| Semarang   | 20     |
| Surabaya   | 20     |

Tabel 5 merupakan contoh jumlah sebaran data deskriptif pada salah satu kolom yaitu kolom `City`. Informasi tersebut menunjukkan jumlah data atau entri untuk setiap kota dalam _dataset_ dengan jumlah 20 entri atau tempat wisata untuk masing-masing kota, yaitu Jakarta, Yogyakarta, Bandung, Semarang, dan Surabaya. Hal ini bertujuan untuk mengetahui jumlah persebaran setiap data pada masing-masing kolom.

**1.1.5. Melihat data yang hilang.**

Tabel 6. Jumlah data yang hilang pada setiap kolom.

| Kolom          | Jumlah |
| -------------- | ------ |
| Package        | 0      |
| City           | 0      |
| Place_Tourism1 | 0      |
| Place_Tourism2 | 0      |
| Place_Tourism3 | 0      |
| Place_Tourism4 | 34     |
| Place_Tourism5 | 61     |

Tabel 6 menunjukkan jumlah nilai yang hilang (_missing values_) pada setiap kolom dalam _dataset_. Nilai yang hilang menunjukkan bahwa tidak ada data yang tersedia untuk kolom tersebut pada entri atau tempat wisata tertentu. Hal ini dilakukan untuk memastikan kualitas dan integritas data dalam _dataset_. Dengan mengetahui jumlah dan lokasi nilai yang hilang maka dapat diketahui kelengkapan, identitas, serta kualitas data.

**2. Melakukan _data preprocessing_ untuk persiapan dalam menggunakan metode _Content-based Filtering_ dan _Collaborative Filtering_.**

**2.1. Menggabungkan data tourism_with_id, tourism_rating dan user yang bertujuan untuk mengumpulkan keseluruhan data yang memiliki entitas yang sama.**

Tabel 7. Contoh hasil penggabungan _dataset_.

| Place_Id | Place_Name       | Description                                     | Category | City    | Price | Rating | Time_Minutes | Coordinate                       | Lat       | Long       | Unnamed: 11 | Unnamed: 12 | User_Id | Place_Ratings | Location              | Age |
| -------- | ---------------- | ----------------------------------------------- | -------- | ------- | ----- | ------ | ------------ | -------------------------------- | --------- | ---------- | ----------- | ----------- | ------- | ------------- | --------------------- | --- |
| 1        | Monumen Nasional | Monumen Nasional atau yang populer disingkat... | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | NaN         | NaN         | 1       | 36            | Solo, Jawa Tengah     | 20  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | NaN         | NaN         | 1       | 38            | Serang, Banten        | 26  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | NaN         | NaN         | 1       | 64            | Bandung, Jawa Barat   | 38  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | NaN         | NaN         | 1       | 74            | Semarang, Jawa Tengah | 30  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | NaN         | NaN         | 1       | 86            |                       |     |

Tabel 7 merupakan data dari tempat wisata yang berisi informasi tentang identifikasi tempat wisata, seperti `Place_Id` dan `Place_Name`. Terdapat juga deskripsi singkat tentang tempat wisata tersebut dalam kolom `Description` dan kategori tempat wisata dalam kolom `Category`. Data ini terkait dengan kota di mana tempat wisata berada, yang dinyatakan dalam kolom `City`.

Selain itu, terdapat informasi tentang harga tiket masuk (`Price`) dan `rating` tempat wisata (`Rating`) dalam kolom yang sesuai. Durasi waktu yang direkomendasikan untuk mengunjungi tempat wisata tersebut ditampilkan dalam kolom `Time_Minutes`.

Data koordinat lokasi tempat wisata tersedia dalam bentuk `dictionary` dalam kolom `Coordinate`, dengan informasi `latitude` (_Lat_) dan `longitude` (_Long_). Terdapat pula beberapa kolom dengan nama `Unnamed: 11` dan `Unnamed: 12` yang tidak memiliki informasi yang terlihat dalam contoh data ini.

Selanjutnya, data terkait pengguna atau pengunjung tempat wisata juga disajikan dalam tabel ini, seperti `User_Id` yang merupakan identifikasi pengguna, dan `Place_Ratings` yang menunjukkan `rating` yang diberikan oleh pengguna untuk tempat wisata tersebut. Informasi lokasi dan usia pengguna juga terdapat dalam kolom `Location` dan `Age`.

**2.2. Menghapus kolom `Unnamed: 11`, `Unnamed: 12` karena tidak memiliki arti baris dan nama kolom yang jelas.**

Tabel 8. Contoh hasil penghapusan kolom `Unnamed: 11`, `Unnamed: 12` pada _dataset_.

| Place_Id | Place_Name       | Description                                     | Category | City    | Price | Rating | Time_Minutes | Coordinate                       | Lat       | Long       | User_Id | Place_Ratings | Location              | Age |
| -------- | ---------------- | ----------------------------------------------- | -------- | ------- | ----- | ------ | ------------ | -------------------------------- | --------- | ---------- | ------- | ------------- | --------------------- | --- |
| 1        | Monumen Nasional | Monumen Nasional atau yang populer disingkat... | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | 36      | 4             | Solo, Jawa Tengah     | 20  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | 38      | 2             | Serang, Banten        | 26  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | 64      | 2             | Bandung, Jawa Barat   | 38  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | 74      | 2             | Semarang, Jawa Tengah | 30  |
| 1        | Monumen Nasional | ...                                             | Budaya   | Jakarta | 20000 | 4.6    | 15.0         | {'lat': -6.1753924, 'lng': ... } | -6.175392 | 106.827153 | 86      | 4             | Depok, Jawa Barat     | 32  |

Tabel 8 menampilkan kolom saat ini seperti `Place_Id`, `Place_Name`, `Description`, `Category`, `City`, `Price`, `Rating`, `Time_Minutes`, `Coordinate`, `Lat`, `Long`, `User_Id`, `Place_Ratings`, `Location`, dan `Age`.

**2.3. Melakukan pengecekan nilai _null_ pada data yang sudah digabungkan.**

Tabel 9. Hasil pengecekan nilai _null_.

| Kolom         | Jumlah |
| ------------- | ------ |
| Place_Id      | 0      |
| Place_Name    | 0      |
| Description   | 0      |
| Category      | 0      |
| City          | 0      |
| Price         | 0      |
| Rating        | 0      |
| Time_Minutes  | 5372   |
| Coordinate    | 0      |
| Lat           | 0      |
| Long          | 0      |
| User_Id       | 0      |
| Place_Ratings | 0      |
| Location      | 0      |
| Age           | 0      |

Pada Tabel 9, dapat diketahui bahwa kolom `Time_minutes` masih memiliki nilai _null_. Namun, karena tidak memiliki relevansi terhadap `Place_name` (kolom target) maka akan di-_drop_ juga.

**2.4. Mengurutkan data berdasarkan `Place_Id` bertujuan untuk mengorganisir data sehingga data dengan `Place_Id` yang sama akan berada bersamaan dalam _DataFrame_.**

**2.5. Menghapus data duplikat berdasarkan kolom `Place_Id` bertujuan untuk mengambil data pada kolom `Place_name` yang bersifat unik.**

Hasil pada tahapan ini akan mendapatkan 437 data unik berdasarkan kolom `Place_Id` dari total 10000 jumlah data pada _dataset_.

**2.6 Mengubah data pada kolom `Category` yang memiliki nilai 2 kata sehingga dipisahkan oleh tanda spasi kemudian diganti menjadi _underscore_ agar menjadi sebuah kata yang terhubung. Tujuannya untuk menghindari terlalu banyak kategori berdasarkan jumlah kata yang dapat menyebabkan ambiguinitas.**

Hasil dari tahapan ini dapat dilihat pada Tabel 10.

Tabel 10. Jumlah sebaran data deskriptif pada kolom `Category`.

| Category           | Jumlah |
| ------------------ | ------ |
| Taman_Hiburan      | 135    |
| Budaya             | 117    |
| Cagar_Alam         | 106    |
| Bahari             | 47     |
| Tempat_Ibadah      | 17     |
| Pusat_Perbelanjaan | 15     |

Tabel 10 menunjukkan jumlah data unik pada kolom `Category` yang terdiri dari beberapa kategori tempat wisata.

**2.7. Mengubah data ke dalam bentuk _list_ pada kolom `Place_Id`, `Place_Name`, dan `Category`. Bertujuan untuk pembuatan _dataframe_ baru yang akan dijadikan sebagai data penerapan sistem rekomendasi.**

Jumlah _value_ pada _list_ yang dimiliki saat ini dari setiap kolom adalah 437.

**2.8 Membuat _dataframe_ baru dengan cara membuat _dictionary_ dari hasil _list_ sebelumnya pada masing-masing kolom. Bertujuan untuk pemroresan data yang akan digunakan untuk pembuatan _Content-based Filtering_ dan _Collaborative Filtering_.**

Tabel 11. Beberapa data pada kolom `id`, `place_name`, dan `category`.

| id  | place_name                                | category      |
| --- | ----------------------------------------- | ------------- |
| 1   | Monumen Nasional                          | Budaya        |
| 2   | Kota Tua                                  | Budaya        |
| 3   | Dunia Fantasi                             | Taman_Hiburan |
| 4   | Taman Mini Indonesia Indah (TMII)         | Taman_Hiburan |
| 5   | Atlantis Water Adventure                  | Taman_Hiburan |
| ... | ...                                       | ...           |
| 433 | Museum Mpu Tantular                       | Budaya        |
| 434 | Taman Bungkul                             | Taman_Hiburan |
| 435 | Taman Air Mancur Menari Kenjeran          | Taman_Hiburan |
| 436 | Taman Flora Bratang Surabaya              | Taman_Hiburan |
| 437 | Gereja Perawan Maria Tak Berdosa Surabaya | Tempat_Ibadah |

Tabel 11 menampilkan beberapa data dari kolom `id`, `place_name`, dan `category` yang terdapat dalam _dataset_. Data ini akan digunakan pada pembuatan sistem rekomendasi menggunakan metode _Content-based Filtering_ dan _Collaborative Filtering_.

**2.8.1. _Data preprocessing_ untuk penggunaan metode _Content-based Filtering_.**

a. Melakukan vektorisasi pada data kategori yang bertujuan untuk menemukan representasi fitur penting dari setiap kategori tempat wisata.

b. Melakukan transformasi pada data kategori ke dalam bentuk matriks. Hal ini bertujuan untuk mengubah data kategori menjadi repsentasi numerik sehingga memudahkan dalam penerapan ke metode _Content-based filtering_.

c. Mengubah data sebelumnya yang berbentuk _sparse matrix_ menjadi _dense matrix_. Hal ini dikarenakan, pada tahap sebelumnya saat melakukan transformasi data teks menggunakan TF-IDF, hasilnya adalah _sparse matrix_ (matriks yang banyak elemennya bernilai nol) karena sebagian besar kata tidak muncul dalam setiap dokumen. Fungsi `todense()` digunakan untuk mengubah _sparse matrix_ menjadi bentuk matriks _dense_, di mana semua elemen (termasuk yang bernilai nol) akan ditampilkan dalam bentuk matriks yang utuh.

d. Membuat _dataframe_ baru dengan kolom `category` dan baris `place_name` dengan nilainya adalah nilai matriks yang telah didefinisikan sebelumnya. Hal ini bertujuan menampilkan matriks untuk setiap kata (fitur) dalam kolom kategori tempat wisata dan setiap baris diisi dengan nama tempat wisata.

e. Melakukan perhitungan tingkat kemiripan menggunakan metode _Cosine Similarity_ pada matriks yang bertujuan untuk mengukur sejauh mana dua vektor mendekati kesamaan berdasarkan arah.

f. Membuat _dataframe_ dari matriks _cosine similarity_ (`cosine_sim`) dengan baris dan kolom yang berupa nama tempat wisata. Bertujuan untuk memvisualisasikan _similarity matrix_ antara tempat wisata dalam bentuk _dataframe_, sehingga memudahkan dalam menganalisis kemiripan antara tempat-tempat wisata tersebut.

Setelah tahapan ini, maka tahapan selanjutnya adalah melakukan _modelling_ menggunakan metode _Content-based Filtering_.

**2.8.2. _Data preprocessing_ untuk penggunaan metode _Collaborative Filtering_.**

a. Menggunakan data `tourism_rating.csv` untuk pembuatan model _collaborative filtering_.

Tabel 12. Beberapa data pada kolom `User_Id`, `Place_Id`, dan `Place_Ratings` dari dataset `tourism_rating.csv`.

| User_Id | Place_Id | Place_Ratings |
| ------- | -------- | ------------- |
| 1       | 179      | 3             |
| 1       | 344      | 2             |
| 1       | 5        | 5             |
| 1       | 373      | 3             |
| 1       | 101      | 4             |
| ...     | ...      | ...           |
| 300     | 425      | 2             |
| 300     | 64       | 4             |
| 300     | 311      | 3             |
| 300     | 279      | 4             |
| 300     | 163      | 2             |

Tabel 12 menampilkan beberapa data dari kolom `User_Id`, `Place_Id`, dan `Place_Ratings` yang terdapat dalam _dataset_ `tourism_rating.csv`.

b. Mengubah data pada `User_Id` menjadi _list_ dengan nilai unik. Tujuannya adalah agar mudah melihat daftar pengguna (_user_) yang ada dalam data _rating_ tersebut serta persiapan melakukan _encoding_ pada data _list_. Hasil dari proses ini disimpan dalam variabel `list_user_id`.

c. Melakukan _encoding_ pada variabel `list_user_id`. Bertujuan untuk menggantikan nilai dalam _list_ `list_user_id` dengan angka indeksnya sehingga mempermudah representasi dalam bentuk _dictionary_.

d. Melakukan _encoding_ angka ke data `User_Id`. Bertujuan untuk mengonversi angka indeks kembali menjadi nilai `User_Id`.

e. Melakukan langkah yang sama pada langkah b,c, dan d diatas terhadap kolom `Place_Id` dengan tujuan yang sama.

f. Melakukan _mapping_ pada `User_Id` dan `Place_Id` ke _dataframe_ `user` dan `tourism`. Bertujuan untuk menghubungkan data pada `User_Id` dan `Place_Id` sehingga representasi data lebih mudah dipahami dan dapat digunakan ke proses pembuatan model.

g. Mengubah kolom `Place_Ratings` menjadi tipe data `float` agar mendapatkan representasi numerik yang lebih tepat untuk _rating_ tempat wisata.

h. Mengacak urutan data agar mendapatkan variasi data pada saat melakukan pembagian _dataset_.

i. Membagi _dataset_ menjadi 80% data latih dan 20% data validasi. Bertujuan untuk persiapan data dalam menerapkan ke model _Collaborative Filtering_.

## Modelling

Pada proyek ini, digunakan 2 metode untuk mengatasi rumusan masalah yang telah didefinisikan sebelumnya. Dalam membuat sistem rekomendasi yang dipersonalisasi akan menggunakan metode _Content-based Filtering_. Sedangkan, pembuatan sistem rekomendasi yang merekomendasikan destinasi wisata lain yang mungkin disukai oleh calon wisatawan yang belum pernah mengunjungi tempat tersebut menggunakan metode _Collaborative Filtering_. Berikut penjelasan mengenai lebih lanjut mengenai penggunaan metode tersebut:

**_Content-based Filtering_**

_Content-Based Filtering_ adalah salah satu metode sistem rekomendasi yang menggunakan informasi atau konten dari item (misalnya, film, produk, atau tempat wisata) yang akan direkomendasikan untuk menentukan kesesuaian atau relevansi dengan preferensi pengguna. Dalam melakukan perhitungan karakteristik dapat menggunakan _cosine similarity_. _Cosine Similarity_ adalah salah satu metode perhitungan kesamaan atau _similarity_ yang digunakan dalam _content-based filtering_. Metode ini mengukur kemiripan antara dua vektor dalam ruang fitur dengan menghitung kosinus sudut antara kedua vektor tersebut. Semakin kecil sudut kosinus, semakin mirip kedua vektor dan semakin tinggi nilai _similarity_ [[14]](https://www.sciencedirect.com/science/article/abs/pii/S0020025515001243).

Kelebihan dari metode ini adalah metode ini tidak memerlukan data riwayat pengguna atau kolaborasi antar pengguna, sehingga cocok untuk kasus _cold-start_, yaitu ketika terdapat item baru atau pengguna baru tanpa data sebelumnya. Sedangkan, kekurangannya adalah terbatas dalam menemukan item yang tidak sejenis dengan preferensi pengguna sebelumnya. Jika konten yang ada tidak cukup beragam, rekomendasi dapat menjadi terbatas dan kurang beragam.

Cara kerja metode _content-based filtering_ menggunakan _cosine similarity_ adalah sebagai berikut:

1. Representasi Vektor: Setiap item direpresentasikan sebagai vektor fitur, di mana setiap dimensi vektor mewakili suatu atribut atau karakteristik dari item tersebut.

2. Penghitungan _Similarity_: Ketika pengguna memberikan preferensi atau _rating_ terhadap beberapa item, sistem akan menggunakan vektor fitur dari item tersebut dan menghitung _similarity_ dengan vektor fitur item lainnya menggunakan _cosine similarity_.

3. Perankingan Item: Item yang memiliki nilai _similarity_ tertinggi akan diurutkan dalam urutan tertentu dan dianggap sebagai item yang cocok untuk direkomendasikan.

Hasil _Top-N Recommendations_ pada rekomendasi tempat wisata selain "Bukit Moko" dapat dilihat pada Tabel 13.

Tabel 13. 5 Rekomendasi tempat wisata menggunakan metode _content-based filtering_.

| place_name             | Similarity | category   |
| ---------------------- | ---------- | ---------- |
| Curug Bugbrug          | 1.0        | Cagar_Alam |
| Taman Bunga Cihideung  | 1.0        | Cagar_Alam |
| Observatorium Bosscha  | 1.0        | Cagar_Alam |
| Goa Pindul             | 1.0        | Cagar_Alam |
| Perkebunan Teh Malabar | 1.0        | Cagar_Alam |

Tabel 13 menampilkan 5 rekomendasi tempat wisata beserta nilai similaritas dan kategori mereka untuk tempat wisata "Bukit Moko". Semua tempat wisata dalam tabel memiliki similaritas maksimum dengan nilai 1.0.

**_Collaborative Filtering_**

_Collaborative filtering_ adalah salah satu metode dalam sistem rekomendasi yang mengandalkan informasi dari pengguna lain atau kesamaan preferensi pengguna untuk menghasilkan rekomendasi. Tujuan dari _collaborative filtering_ adalah mencari korelasi antara pengguna dan item (misalnya produk, film, atau tempat wisata) berdasarkan data riwayat interaksi antara pengguna dan item tersebut.

RecommenderNet adalah model rekomendasi yang menggunakan arsitektur _neural network_ untuk menerapkan _collaborative filtering_. Model ini dapat mengambil informasi dari data riwayat interaksi pengguna dan item, seperti _rating_ atau _review_, dan menghasilkan rekomendasi yang personal untuk setiap pengguna [[15]](https://arxiv.org/abs/1708.01715).

_Collaborative filtering_ menggunakan RecommenderNet memiliki kelebihan dalam memberikan rekomendasi personal dan relevan berdasarkan preferensi pengguna sebelumnya serta kemampuannya menangani data besar dan kompleks. Model ini dapat diadaptasi untuk berbagai jenis data, seperti data peringkat atau data biner. Namun, metode ini memiliki kelemahan, seperti kesulitan dalam memberikan rekomendasi untuk pengguna atau item baru (_cold-start problem_).

Cara kerja metode _collaborative filtering_ menggunakan RecommenderNet adalah sebagai berikut:

1. Representasi Pengguna dan Item: Setiap pengguna dan item diwakili oleh vektor _embedding_ dalam ruang fitur multidimensional. Representasi ini digunakan untuk mencari kesamaan antara pengguna dan item.

2. Menemukan Kesamaan: Metode _collaborative filtering_ mencari kesamaan antara pengguna dan item berdasarkan vektor _embedding_. Kesamaan ini dapat diukur dengan menggunakan metrik _dot product_.

3. Memperkirakan _Rating_: Setelah kesamaan antara pengguna dan item ditemukan, model akan memperkirakan _rating_ yang mungkin akan diberikan oleh pengguna untuk item yang belum dilihat atau diinteraksikan sebelumnya sehingga dapat memberikan rekomendasi.

Pada proyek ini, digunakan paramter `epochs=100`, `batch_size=8`, _binary crossentropy_ untuk menghitung _loss function_, Adam (_Adaptive Moment Estimation_) sebagai _optimizer_, dan _root mean squared error_ (RMSE) sebagai metrics evaluation.

Hasil _Top-N Recommendations_ pada rekomendasi tempat wisata lain berdasarkan _rating_ tempat wisata sebelumnya yang pernah dikunjungi oleh pengguna dengan _Id_ 195 dapat dilihat pada Tabel 14.

Tabel 14. Contoh rekomendasi tempat wisata menggunakan metode _Collaborative Filtering_.

| Place Name                  | Category           |
| --------------------------- | ------------------ |
| Jembatan Kota Intan         | Budaya             |
| Pasar Tanah Abang           | Pusat_Perbelanjaan |
| Embung Tambakboyo           | Taman_Hiburan      |
| Candi Borobudur             | Budaya             |
| Panghegar Waterboom Bandung | Taman_Hiburan      |
| Wot Batu                    | Cagar_Alam         |
| Saung Angklung Mang Udjo    | Budaya             |
| Grand Maerakaca             | Taman_Hiburan      |
| GPIB Immanuel Semarang      | Tempat_Ibadah      |
| La Kana Chapel              | Taman_Hiburan      |

## Evaluation

**_Content-based Filtering_**

Dari hasil penggunaan _cosine similarity_ pada pemberian rekomendasi tempat wisata dapat dilihat seperti pada Tabel 13. Tempat wisata yang direkomendasikan memiliki nilai _similarity_ tertinggi yaitu 1.0. Hal itu juga menunjukkan bahwa tidak terjadi selisih nilai _similarity_ antar rekomendasi tempat ke 1 sampai 5.

**_Collaborative Filtering_**

Dalam melakukan evaluasi terhadap hasil pelatihan menggunakan RecommenderNet pada metode collaborative filtering digunakan metrik evaluasi RMSE (_Root Mean Square Error_). RMSE adalah salah satu metrik evaluasi yang digunakan untuk mengukur kesalahan atau selisih antara nilai prediksi dan nilai aktual dalam suatu model. RMSE mengukur seberapa akurat model dalam membuat prediksi dengan membandingkan nilai prediksi dengan nilai aktual dan menghitung rata-rata dari kuadrat selisih antara keduanya [[16]](https://gmd.copernicus.org/preprints/7/1525/2014/gmdd-7-1525-2014.pdf).

Rumus dari RMSE adalah sebagai berikut:

RMSE = √(1/n \* ∑(y_i - ŷ_i)^2)

Keterangan:

- `n` adalah jumlah sampel data.
- `y_i` adalah nilai aktual dari data ke-i.
- `ŷ_i` adalah nilai prediksi dari data ke-i.

Cara kerja RMSE adalah dengan menghitung selisih antara nilai aktual dan nilai prediksi untuk setiap data, kemudian mengkuadratkan selisih tersebut, menjumlahkan semua kuadrat selisih, dan kemudian mengambil akar kuadrat dari nilai tersebut. Semakin kecil nilai RMSE, semakin baik model dalam melakukan prediksi yang akurat, karena nilai RMSE yang lebih kecil menunjukkan bahwa selisih antara nilai prediksi dan nilai aktual lebih kecil dan mendekati nol.

Pada proyek ini, hasil dari perhitngan RMSE selama proses _training_ dapat dilihat pada Gambar 2.

[![training result](https://i.postimg.cc/VkGLPMJ8/download-2.png)](https://postimg.cc/FYSQjYbW)

Gambar 2. Hasil proses _training_ pada menggunakan model RecommenderNet.

Dari Gambar 2 tersebut dapat diketahui bahwa model memiliki nilai _Root Mean Square Error_ (RMSE) yang relatif rendah pada data _training_ sebesar 0.31. Hal ini menunjukkan bahwa prediksi model cenderung mendekati nilai aktual dengan tingkat kesalahan yang rendah pada data _training_. Selain itu, nilai _loss_ pada data _training_ sebesar 0.64 juga menunjukkan bahwa model telah berhasil mengurangi kesalahan prediksi pada data _training_.

Namun, pada data validasi, nilai RMSE sedikit meningkat menjadi 0.36. Ini menunjukkan bahwa model mungkin mengalami sedikit _overfitting_, yaitu ketika model terlalu terfokus pada data _training_ dan tidak secara akurat dapat menggeneralisasi pada data yang belum pernah dilihat sebelumnya. Nilai _loss_ pada data validasi sebesar 0.72 juga menunjukkan adanya peningkatan kesalahan prediksi pada data validasi.

## Conclusion

## REFERENSI

[[1]](https://www.jurnal.ummu.ac.id/index.php/kawasa/article/view/443) T. A. Ruray and R. Pratama, “PENGARUH DAYA TARIK DAN AKSESIBILITAS TERHADAP KEPUTUSAN BERKUNJUNG PADA OBJEK WISATA PANTAI AKESAHU KOTA TIDORE KEPULAUAN,” KAWASA: Jurnal Ilmu-Ilmu Sosial dan Politik, vol. XI, no. 2, Jun. 2020.

[[2]](https://ejurnal.bunghatta.ac.id/index.php/JMN/article/view/16895/14264) M. K. Dewi, M. Rivandi, and E. Meirina, “Pengaruh Daya Tarik Wisata, Fasilitas Dan Aksesibilitas Terhadap&nbsp; Keputusan Berkunjung di Objek Wisata pantai air manis kota Padang,” Jurnal Manajemen Universitas Bung Hatta, vol. 15, no. 2, 2020. doi:10.37301/jmubh.v15i2.16895.

[[3]](https://scholar.archive.org/work/7w2m5zoz5jb75phn6soimle3oy/access/wayback/https://ejournal.unisnu.ac.id/JDPT/article/download/1258/pdf) A. Dwihastadi, A. Mulyanto, and M. G. Wonoseto, “Prototipe Aplikasi mobile Pendukung Keputusan pemilihan Destinasi Wisata di Yogyakarta,” Jurnal Disprotek, vol. 11, no. 2, pp. 59–66, 2020. doi:10.34001/jdpt.v11i2.1258.

[[4]](https://scholar.archive.org/work/gxrj3ap7z5ashl3xj57kllenk4/access/wayback/https://ejurnal.mikroskil.ac.id/index.php/jsm/article/download/816/pdf) A. R. Harischandra, M. F. Pratama, F. Felix, and A. P. Laia, “Aplikasi Pendukung Desain interior Dengan Sistem Rekomendasi Berdasarkan nama brand Perabot Menggunakan ALGORITMA content-based filtering berbasis web,” Jurnal SIFO Mikroskil, vol. 23, no. 1, pp. 1–16, 2022. doi:10.55601/jsm.v23i1.816.

[[5]](https://ejournal.undip.ac.id/index.php/jmasif/article/view/31482) A. H. Ritdrix and P. W. Wirawan, “Sistem Rekomendasi Buku Menggunakan metode item-based collaborative filtering,” JURNAL MASYARAKAT INFORMATIKA, vol. 9, no. 2, pp. 24–32, 2018. doi:10.14710/jmasif.9.2.31482.

[[6]](https://ieeexplore.ieee.org/abstract/document/7254144) F. Zhao, F. Yan, H. Jin, L. T. Yang and C. Yu, "Personalized Mobile Searching Approach Based on Combining Content-Based Filtering and Collaborative Filtering," in IEEE Systems Journal, vol. 11, no. 1, pp. 324-332, March 2017, doi: 10.1109/JSYST.2015.2472996.

[[7]](http://e-journal.hamzanwadi.ac.id/index.php/edumatic/article/view/2162/1162) A. I. Putra and R. R. Santika, “Implementasi Machine learning Dalam Penentuan Rekomendasi Musik Dengan metode content-based filtering,” Edumatic : Jurnal Pendidikan Informatika, vol. 4, no. 1, pp. 121–130, 2020. doi:10.29408/edumatic.v4i1.2162.

[[8]](https://ieeexplore.ieee.org/abstract/document/9321202) K. A. Fararni, F. Nafis, B. Aghoutane, A. Yahyaouy, J. Riffi and A. Sabri, "Hybrid recommender system for tourism based on big data and AI: A conceptual framework," in Big Data Mining and Analytics, vol. 4, no. 1, pp. 47-55, March 2021, doi: 10.26599/BDMA.2020.9020015.

[[9]](https://www.ijcaonline.org/archives/volume110/number4/19308-0760) P. B.Thorat, R. M. Goudar, and S. Barve, “Survey on collaborative filtering, content-based filtering and hybrid recommendation system,” International Journal of Computer Applications, vol. 110, no. 4, pp. 31–36, 2015. doi:10.5120/19308-0760.

[[10]](https://ieeexplore.ieee.org/abstract/document/10054282) L. N. S. Prakash Goteti, "Design and Implementation of Item Based Collaborative Filtering -A Case Study," 2022 IEEE 7th International Conference on Recent Advances and Innovations in Engineering (ICRAIE), MANGALORE, India, 2022, pp. 83-86, doi: 10.1109/ICRAIE56454.2022.10054282.

[[11]](https://dl.acm.org/doi/fullHtml/10.1145/3482632.3487539) H. Wang, “Design and implementation of web online education platform based on user collaborative filtering algorithm,” 2021 4th International Conference on Information Systems and Computer Aided Education, 2021. doi:10.1145/3482632.3487539.

[[12]](https://www.ijcaonline.org/archives/volume167/number12/sang-2017-ijca-914490.pdf) A. Sang and S. K., “Design and implementation of collaborative filtering approach for movie recommendation system,” International Journal of Computer Applications, vol. 167, no. 12, pp. 18–24, 2017. doi:10.5120/ijca2017914490.

[[13]](https://bitlabs.id/blog/diagram-garis-adalah/) Minlab, “Diagram Garis: Pengertian, Cara Membuat, & Serba-Serbinya” Bitlabs, https://bitlabs.id/blog/diagram-garis-adalah/ (accessed Jul. 18, 2023).

[[14]](https://www.sciencedirect.com/science/article/abs/pii/S0020025515001243) P. Xia, L. Zhang, and F. Li, “Learning similarity with cosine similarity ensemble,” Information Sciences, vol. 307, pp. 39–52, 2015. doi:10.1016/j.ins.2015.02.024.

[[15]](https://arxiv.org/abs/1708.01715) O. Kuchaiev and B. Ginsburg, “Training Deep AutoEncoders for Collaborative Filtering,” Arxiv, 2017.

[[16]](https://gmd.copernicus.org/preprints/7/1525/2014/gmdd-7-1525-2014.pdf) T. Chai and R. R. Draxler, Root mean square error (RMSE) or mean absolute error (mae)?, 2014. doi:10.5194/gmdd-7-1525-2014.
