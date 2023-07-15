# Laporan Proyek Machine Learning - Karimuddin Hakim Hasibuan

## Project Overview

Indonesia merupakan negara kepulauan dengan beragam kekayaan alam dan budaya yang menarik bagi wisatawan lokal maupun internasional sebagai destinasi tempat wisata. Objek wisata adalah segala sesuatu yang ada di daerah tujuan wisata yang merupakan daya tarik agar orang-orang ingin datang berkunjung ke tempat tersebut [[1]](https://www.jurnal.ummu.ac.id/index.php/kawasa/article/view/443).

Objek dan daya tarik wisata menurut Undang-undang No 10 tahun 2009 tentang kepariwisataan yaitu daya tarik wisata adalah segala sesuatu yang memiliki keunikan, keindahan, dan nilai yang berupa keanekaragaman kekayaan alam, budaya, dan hasil buatan manusia yang menjadi sasaran atau tujuan kunjungan wisatawan dan daerah tujuan pariwisata yang selanjutnya disebut destinasi pariwisata [[2]](https://ejurnal.bunghatta.ac.id/index.php/JMN/article/view/16895/14264).

Berbagai banyaknya pilihan tempat wisata di Indonesia tak jarang menyebabkan calon wisatawan sering mengalami kesulitan dalam memilih tempat wisata yang sesuai dengan minat dan preferensi mereka. Hal ini disebabkan oleh beberapa faktor, termasuk keterbatasan informasi yang tersedia, kebanyakannya informasi yang bersifat umum dan tidak personal, serta kebingungan dalam mengidentifikasi tempat-tempat yang benar-benar menarik di antara banyaknya pilihan [[3]](https://scholar.archive.org/work/7w2m5zoz5jb75phn6soimle3oy/access/wayback/https://ejournal.unisnu.ac.id/JDPT/article/download/1258/pdf).

Berdasarkan permasalahan diatas, penulis melakukan proyek pengembangan sistem rekomendasi tempat wisata di Indonesia. Proyek ini bertujuan untuk membantu pengguna dengan menyaring informasi dan menyajikan rekomendasi yang sesuai dengan preferensi mereka sehingga meningkatkan pengalaman wisatawan yang memuaskan dan mampu meningkatkan promosi dan pemasaran destinasi wisata.

Sistem yang dikembangkan menggunakan teknik-teknik dalam bidang pemrosesan bahasa alami, analisis data, dan kecerdasan buatan untuk memberikan rekomendasi yang personal dan relevan kepada pengguna seperti _Content Based Filtering_ dan _Collaborative Filtering_. _Content-based filtering_ memberikan suatu rekomendasi berdasarkan hasil analisa kemiripan item yang telah dinilai oleh para penggunanya [[4]](https://scholar.archive.org/work/gxrj3ap7z5ashl3xj57kllenk4/access/wayback/https://ejurnal.mikroskil.ac.id/index.php/jsm/article/download/816/pdf). Sedangkan, _Collaborative filtering_ adalah suatu konsep dimana opini dari pengguna lain yang ada digunakan untuk memprediksi item yang mungkin disukai/diminati oleh seorang pengguna [[5]](https://ejournal.undip.ac.id/index.php/jmasif/article/view/31482). Teknik ini mampu memberikan hasil yang signifikan dalam meningkatkan pengalaman penelurusan pengguna yang dipersonalisasi [[6]](https://ieeexplore.ieee.org/abstract/document/7254144).

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

Penggunaan teknik _Content Based Filtering_ pada proyek ini adalah dalam memberikan rekomendasi yang dipersonalisasi berdasarkan data wisatawan dan tempat wisata yang dikunjungi. Sedangkan, teknik _Collaborative Filtering_ untuk merekomendasikan destinasi wisata lain yang mungkin disukai oleh calon wisatawan yang belum pernah mengunjungi tempat tersebut.

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

[[12]](https://www.ijcaonline.org/archives/volume167/number12/sang-2017-ijca-914490.pdf) A. Sang and S. K., “Design and implementation of collaborative filtering approach for movie recommendation system,” International Journal of Computer Applications, vol. 167, no. 12, pp. 18–24, 2017. doi:10.5120/ijca2017914490
