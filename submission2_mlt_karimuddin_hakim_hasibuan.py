# -*- coding: utf-8 -*-
"""Submission2_MLT_Karimuddin_Hakim_Hasibuan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V9O_aR10W9tqkwiAJAhIlJi1Oc7177Mm

**Sistem Rekomendasi Tempat Wisata di Indonesia -Submission Machine Learning Terapan**

Oleh: Karimuddin Hakim Hasibuan

# Menyiapkan dataset

Pada tahapan ini dataset akan diimport ke dalam google colab melalui kaggle. Tujuannya untuk menggunakan dataset sebagai data yang akan menjadi model sistem rekomendasi.
"""

# import kredential akun dari kaggle
from google.colab import files
files.upload()

# mengatur akses kredential akun kaggle agar dapat menggunakan API Kaggle untuk mengunduh dataset
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

# mengunduh dataset dari kaggle
!kaggle datasets download -d aprabowo/indonesia-tourism-destination

# mengekstrak file zip dataset agar dapat digunakan
import zipfile
zip_ref = zipfile.ZipFile('indonesia-tourism-destination.zip', 'r')
zip_ref.extractall('')
zip_ref.close()

# menyimpan masing-masing file ke dalam variabel dataframe
import pandas as pd

df_package_tourism = pd.read_csv('/content/package_tourism.csv')
df_tourism_rating = pd.read_csv('/content/tourism_rating.csv')
df_tourism_with_id = pd.read_csv('/content/tourism_with_id.csv')
df_user = pd.read_csv('/content/user.csv')

# menampilkan 5 data teratas untuk data package_tourism

print(df_package_tourism.head())

# menampilkan 5 data teratas untuk data tourism_rating

print(df_tourism_rating.head())

# menampilkan 5 data teratas untuk data tourism_with_id

print(df_tourism_with_id.head())

# menampilkan 5 data teratas untuk data user

print(df_user.head())

"""# Preparation data

1. Pada tahapan ini data akan melalui proses Exploratory Data Analysis (EDA). Bertujuan untuk mendapatkan insight data.

1.1. Proses EDA pada data package_tourism.

1.1.1. Mengecek tipe data pada setiap kolom.
"""

print(df_package_tourism.info())

"""1.1.2. Menampilkan sebaran statistik deskriptif pada kolom numerik, yaitu kolom Package."""

print(df_package_tourism.describe())

"""1.1.3. Menampilkan jumlah data unik pada setiap kolom."""

print(df_package_tourism.nunique())

"""1.1.4. Menampilkan jumlah data deskriptif dari setiap kolom."""

print('Jumlah kota: \n', df_package_tourism['City'].value_counts())
print('--------------------------------------------------------')
print('Jumlah tempat wisata pertama: \n', df_package_tourism['Place_Tourism1'].value_counts())
print('--------------------------------------------------------')
print('Jumlah tempat wisata kedua: \n', df_package_tourism['Place_Tourism2'].value_counts())
print('--------------------------------------------------------')
print('Jumlah tempat wisata ketiga: \n', df_package_tourism['Place_Tourism3'].value_counts())
print('--------------------------------------------------------')
print('Jumlah tempat wisata keempat: \n', df_package_tourism['Place_Tourism4'].value_counts())
print('--------------------------------------------------------')
print('Jumlah tempat wisata kelima: \n', df_package_tourism['Place_Tourism5'].value_counts())

"""1.1.5. Melihat data yang hilang."""

print(df_package_tourism.isnull().sum())

"""1.2. Proses EDA pada data tourism_rating.

1.2.1. Mengecek tipe data pada setiap kolom.
"""

print(df_tourism_rating.info())

"""1.2.2. Menampilkan sebaran statistik deskriptif pada kolom numerik."""

print(df_tourism_rating.describe())

"""1.2.3. Menampilkan jumlah data unik pada setiap kolom."""

print(df_tourism_rating.nunique())

"""1.2.4. Menampilkan jumlah data deskriptif dari setiap kolom."""

print('Jumlah User Id: \n', df_tourism_rating['User_Id'].value_counts())
print('--------------------------------------------------------')
print('Jumlah Place Id: \n', df_tourism_rating['Place_Id'].value_counts())
print('--------------------------------------------------------')
print('Jumlah Place Ratings: \n', df_tourism_rating['Place_Ratings'].value_counts())

"""1.2.5. Melihat data yang hilang."""

print(df_tourism_rating.isnull().sum())

"""1.3. Proses EDA pada data tourism_with_id.

1.3.1. Mengecek tipe data pada setiap kolom.
"""

print(df_tourism_with_id.info())

"""1.3.2. Menampilkan sebaran statistik deskriptif pada kolom numerik."""

print(df_tourism_with_id.describe())

"""1.3.3. Menampilkan jumlah data unik pada setiap kolom."""

print(df_tourism_with_id.nunique())

"""1.3.4. Menampilkan jumlah data deskriptif dari setiap kolom."""

# Daftar nama kolom yang ingin dihitung jumlah data deskriptif
columns_to_count = ['Place_Id', 'Place_Name', 'Description', 'Category', 'City', 'Price', 'Rating', 'Time_Minutes', 'Coordinate', 'Lat', 'Long', 'Unnamed: 11', 'Unnamed: 12']

# Perulangan untuk mencetak jumlah data deskriptif pada setiap kolom
for column in columns_to_count:
    print(f'Jumlah {column}: \n', df_tourism_with_id[column].value_counts())
    print('--------------------------------------------------------')

"""1.3.5. Melihat data yang hilang."""

print(df_tourism_with_id.isnull().sum())

"""1.4. Proses EDA pada data user.

1.4.1. Mengecek tipe data pada setiap kolom.
"""

print(df_user.info())

"""1.4.2. Menampilkan sebaran statistik deskriptif pada kolom numerik."""

print(df_user.describe())

"""1.4.3. Menampilkan jumlah data unik pada setiap kolom."""

print(df_user.nunique())

"""1.4.4. Menampilkan jumlah data deskriptif dari setiap kolom."""

# Daftar nama kolom yang ingin dihitung jumlah data deskriptif
columns_to_count = ['User_Id', 'Location', 'Age']

# Perulangan untuk mencetak jumlah data deskriptif pada setiap kolom
for column in columns_to_count:
    print(f'Jumlah {column}: \n', df_user[column].value_counts())
    print('--------------------------------------------------------')

"""1.4.5. Melihat data yang hilang."""

print(df_user.isnull().sum())

"""2. Melakukan preprocessing data untuk persiapan dalam menggunakan metode Content-base filtering dan Collaborative Filtering.

2.1. Menggabungkan data tourism_with_id, tourism_rating dan user yang bertujuan untuk mengumpulkan keseluruhan data yang memiliki entitas.
"""

# Gabungkan data dari df_tourism_with_id, dan df_tourism_rating berdasarkan kolom Place_Id serta data dari df_user berdasarkna User_Id
data_merged = df_tourism_with_id.merge(df_tourism_rating, on='Place_Id', how='left')
data_merged = data_merged.merge(df_user, on='User_Id', how='left')
data_merged

"""2.2. Menghapus kolom 'Unnamed: 11', 'Unnamed: 12' karena tidak memiliki baris data yang jelas serta nama kolom juga tidak memiliki arti yang jelas.


"""

# Hapus kolom yang tidak diperlukan
data_merged.drop(['Unnamed: 11', 'Unnamed: 12'], axis=1, inplace=True)
data_merged

"""2.3. Melakukan pengecekan nilai null pada data yang sudah digabungkan."""

print(data_merged.isnull().sum())

"""Berdasarkan hasil diatas, dapat diketahui bahwa kolom Time_minutes masih memiliki nilai null. Namun, karena tidak memiliki relevansi terhadap Place_name (kolom target) maka akan di-drop juga."""

# Hapus kolom Time_Minutes karena memiliki nilai null dan tidak digunakan
data_merged.drop(['Time_Minutes'], axis=1, inplace=True)
print(data_merged.isnull().sum())

"""2.4. Mengurutkan data berdasarkan Place_Id bertujuan untuk mengorganisir data sehingga data dengan "Place_Id" yang sama akan berada bersamaan dalam DataFrame."""

# Membuat variabel data_preparation yang berisi dataframe data_merged kemudian mengurutkan berdasarkan Place_Id
data_preparation = data_merged
data_preparation.sort_values('Place_Id')

"""2.5. Menghapus data duplikat berdasarkan kolom "Place_Id" bertujuan untuk mengambil data pada kolom "Place_name" yang bersifat unik."""

# Membuang data duplikat pada variabel data_preparation
data_preparation = data_preparation.drop_duplicates('Place_Id')
data_preparation

"""2.6 Mengubah data pada kolom "Category" yang memiliki nilai 2 kata sehingga dipisahkan oleh tanda spasi kemudian diganti menjadi underscore agar menjadi sebuah kata yang terhubung. Tujuannya untuk menghindari terlalu banyak kategori berdasarkan jumlah kata yang dapat menyebabkan ambiguinitas."""

# Mengganti spasi dengan underscore pada kolom 'Category'
data_preparation['Category'] = data_preparation['Category'].str.replace(' ', '_')
data_preparation['Category'].value_counts()

"""2.7. Mengubah data ke dalam bentuk list pada kolom "Place_Id", "Place_Name", dan "Category". Bertujuan untuk pembuatan dataframe baru yang akan dijadikan sebagai data penerapan sistem rekomendasi."""

# Mengonversi data series Place_Id menjadi dalam bentuk list
place_id = data_preparation['Place_Id'].tolist()

# Mengonversi data series Place_Name menjadi dalam bentuk list
place_name = data_preparation['Place_Name'].tolist()

# Mengonversi data series Category menjadi dalam bentuk list
place_category = data_preparation['Category'].tolist()

print(len(place_id))
print(len(place_name))
print(len(place_category))

"""2.8. Membuat dataframe baru dengan cara membuat dictionary dari hasil list sebelumnya pada masing-masing kolom. Bertujuan untuk pemroresan data yang akan digunakan untuk pembuatan Content-base filtering."""

# Membuat dictionary untuk data place_id, place_name, dan place_category
place_new = pd.DataFrame({
    'id': place_id,
    'place_name': place_name,
    'category': place_category
})
place_new

"""Melakukan pengecekan kembali pada data dengan menampilkan 5 contoh data secara acak dan mengecek jumlah nilai unik pada data. Bertujuan untuk pengecekan kembali kesesuaian data berdasarkan preprocessing sebelumnya."""

data = place_new
data.sample(5)

print(data.nunique())

"""2.8.1.a. Melakukan vektorisasi pada data kategori yang bertujuan untuk menemukan representasi fitur penting dari setiap kategori tempat wisata."""

from sklearn.feature_extraction.text import TfidfVectorizer

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data category
tf.fit(data['category'])

# Mapping array dari fitur index integer ke fitur nama category
tf.get_feature_names_out()

"""2.8.1.b. Melakukan transformasi pada data kategori ke dalam bentuk matriks. Hal ini bertujuan untuk mengubah data kategori menjadi repsentasi numerik sehingga memudahkan dalam penerapan ke metode Content-based filtering."""

# Melakukan fit lalu ditransformasikan ke bentuk matrix
data_tfidf_matrix = tf.fit_transform(data['category'])

# Melihat bentuk matrix tfidf ukuran matrix tfidf
print(data_tfidf_matrix)
print(data_tfidf_matrix.shape)

"""2.8.1.c. Mengubah data sebelumnya yang berbentuk sparse matrix menjadi dense matrix. Hal ini dikarenakan, pada tahap sebelumnya saat melakukan transformasi data teks menggunakan TF-IDF, hasilnya adalah sparse matrix (matriks yang banyak elemennya bernilai nol) karena sebagian besar kata tidak muncul dalam setiap dokumen. Fungsi todense() digunakan untuk mengubah sparse matrix ini menjadi bentuk matriks dense, di mana semua elemen (termasuk yang bernilai nol) akan ditampilkan dalam bentuk matriks yang utuh."""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
data_tfidf_matrix.todense()

"""2.8.1.d. Membuat dataframe baru dengan kolom "category" dan baris "place_name" dengan nilainya adalah nilai matriks yang telah didefinisikan sebelumnya. Hal ini bertujuan menampilkan matriks untuk setiap kata (fitur) dalam kolom kategori tempat wisata dan setiap baris diisi dengan nama tempat wisata.


"""

# Membuat dataframe untuk melihat tf-idf matrix, bagian kolom diisi dengan kategori tempat wisata dan baris diisi dengan nama tempat wisata

pd.DataFrame(
    data_tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=data.place_name
).sample(6, axis=1).sample(10, axis=0)

"""2.8.1.e. Melakukan perhitungan tingkat kemiripan menggunakan metode cosine_similarity pada matriks yang bertujuan untuk mengukur sejauh mana dua vektor mendekati kesamaan berdasarkan arah."""

from sklearn.metrics.pairwise import cosine_similarity

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(data_tfidf_matrix)
cosine_sim

"""2.8.1.f. Membuat dataframe dari matriks cosine similarity (cosine_sim) dengan baris dan kolom yang berupa nama tempat wisata. Bertujuan untuk memvisualisasikan similarity matrix antara tempat wisata dalam bentuk dataframe, sehingga memudahkan dalam menganalisis kemiripan antara tempat-tempat wisata tersebut."""

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama tempat wisata
cosine_sim_df = pd.DataFrame(cosine_sim, index=data['place_name'], columns=data['place_name'])
print('Shape:', cosine_sim_df.shape)

# Menampilkan similarity matrix pada setiap tempat wisata
cosine_sim_df.sample(5, axis=1).sample(10, axis=0)

"""# Modelling Data

Fungsi tourism_recommendations digunakan untuk memberikan rekomendasi tempat wisata berdasarkan similarity dengan tempat wisata tertentu.
"""

import pandas as pd

def tourism_recommendations(tourism_name, similarity_data=cosine_sim_df, items=data[['place_name', 'category']], k=5):
    # Mengambil data dengan menggunakan argsort untuk mendapatkan indeks dari similarity secara terurut
    index = similarity_data.loc[:, tourism_name].to_numpy().argsort()[-2:-(k+2):-1]

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index]

    # Drop tourism_name agar nama tempat wisata yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(tourism_name, errors='ignore')

    # Ambil nilai similarity dari tourism_name dengan tempat wisata lainnya
    similarity_values = similarity_data.loc[:, tourism_name].iloc[index].values

    # Buat DataFrame untuk menyimpan rekomendasi beserta nilai similarity
    recommendations = pd.DataFrame({'place_name': closest, 'Similarity': similarity_values})

    # Reset indeks pada data items untuk menghindari masalah MergeError
    items = items.reset_index(drop=True)

    # Merge dengan data items untuk mendapatkan informasi mengenai nama dan kategori tempat wisata
    recommendations = recommendations.merge(items, on='place_name')

    return recommendations.head(k)

data[data.place_name.eq('Bukit Moko')]

"""Memanggil fungsi tourism_recommendation dengan mengisi nilai Bukit Moko yang merupakan salah satu tempat wisata agar dapat menampilkan rekomendasi tempat wisata lainnya berdasarkan preferensi dari tempat wisata yang disebutkan."""

print(tourism_recommendations('Bukit Moko'))

"""# Preprocessing Data_2

Pada bagian ini, dilakukan preprocessing data untuk persiapan menggunakan metode Collaborative Filtering.

2.8.2.a. Menggunakan data df_tourism_rating untuk pembuatan model collaborative filtering.
"""

data_rating = df_tourism_rating.copy()

data_rating

"""2.8.2.b. Mengubah data pada User_Id menjadi list dengan nilai unik. Tujuannya adalah agar mudah melihat daftar pengguna (user) yang ada dalam data rating tersebut serta persiapan melakukan encoding pada data list."""

# Mengubah data pada User_Id menjadi list dengan nilai unik
list_user_id = data_rating['User_Id'].unique().tolist()
print('hasil list User_Id: ', list_user_id)

"""2.8.2.c. Melakukan encoding pada list User_Id. Bertujuan untuk menggantikan nilai dalam list list_user_id dengan angka indeksnya sehingga mempermudah representasi dalam bentuk dictionary."""

# Melakukan encoding pada list User_Id
encoded_user_id = {x: i for i, x in enumerate(list_user_id)}
print('hasil encoded User_Id : ', encoded_user_id)

"""2.8.2.d. Melakukan encoding angka ke User_Id. Bertujuan untuk mengonversi angka indeks kembali menjadi nilai User_Id."""

# Melakukan encoding angka ke User_Id
encoded_number_to_user = {i: x for i, x in enumerate(list_user_id)}
print('encoded angka ke userID: ', encoded_number_to_user)

"""2.8.2.e. Melakukan langkah yang sama pada langkah 2,3, dan 4 terhadap kolom Place_Id dengan tujuan yang sama."""

# Mengubah data pada Place_Id menjadi list dengan nilai unik
list_tourism_id = data_rating['Place_Id'].unique().tolist()

# Melakukan encoding pada list Place_Id
encoded_tourism_id = {x: i for i, x in enumerate(list_tourism_id)}
print('hasil encoded Place_Id : ', encoded_tourism_id)

# Melakukan encoding angka ke Place_Id
encoded_number_to_tourism = {i: x for i, x in enumerate(list_tourism_id)}
print('encoded angka ke Place_Id: ', encoded_number_to_tourism)

"""2.8.2.f. Melakukan mapping User_Id dan Place_Id ke dataframe user dan tourism. Bertujuan untuk menghubungkan data pada User_Id dan Place_Id sehingga representasi data lebih mudah dipahami dan dapat digunakan ke proses pembuatan model."""

# Melakukan mapping User_Id dan Place_Id ke dataframe user dan tourism
data_rating['user'] = data_rating['User_Id'].map(encoded_user_id)
data_rating['tourism'] = data_rating['Place_Id'].map(encoded_tourism_id)
data_rating.head()

"""2.8.2.g. Melakukan pengecekan kembali pada data yang baru saja di proses pada tahap sebelumnya guna memastikan pemosisian data dan mengubah Place_Ratings menjadi nilai float."""

import numpy as np

# Mendapatkan jumlah user
sum_user = len(encoded_user_id)
print(sum_user)

# Mendapatkan jumlah tourism
sum_tourism = len(encoded_tourism_id)
print(sum_tourism)

# Mengubah Place_Ratings menjadi nilai float
data_rating['Place_Ratings'] = data_rating['Place_Ratings'].values.astype(np.float32)

# Menampilkan nilai maksimum dan minimum dari Place_Ratings
place_ratings_max = max(data_rating['Place_Ratings'])
place_ratings_min = min(data_rating['Place_Ratings'])

print('Number of User: {}, Number of Place: {}, Min Place Rating: {}, Max Place Rating: {}'.format(
    sum_user, sum_tourism, place_ratings_min, place_ratings_max
))

"""2.8.2.h. Mengacak urutan data agar mendapatkan variasi data pada saat melakukan pembagian dataset."""

# Mengacak data_rating
data_rating = data_rating.sample(frac=1, random_state=42)
data_rating

"""2.8.2.i. Membagi dataset menjadi 80% data latih dan 20% data validasi. Bertujuan untuk persiapan data dalam menerapkan ke model."""

# Membuat variabel X untuk mencocokkan data user dan tourism menjadi satu value
X = data_rating[['user', 'tourism']].values

# Membuat variabel Y untuk membuat rating dari hasil normalisasi data
Y = data_rating['Place_Ratings'].apply(lambda X: (X - place_ratings_min) / (place_ratings_max - place_ratings_min)).values

# Membagi dataset menjadi 80% data train dan 20% data validasi
data_train_split = int(0.8 * data_rating.shape[0])
X_train, X_val, Y_train, Y_val = (
    X[:data_train_split],
    X[data_train_split:],
    Y[:data_train_split],
    Y[data_train_split:]
)

print(X, Y)

"""# Modelling_2

Pada tahap ini dilakukan proses pembentukan model untuk metode Collaborative Filtering.
"""

# Membuat class RecommenderNet dari Keras Model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):
  # Insialisasi fungsi
  def __init__(self, sum_users, sum_tourism, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.sum_users = sum_users
    self.sum_tourism = sum_tourism
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        sum_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(sum_users, 1) # layer embedding user bias
    self.tourism_embedding = layers.Embedding( # layer embeddings tourism
        sum_tourism,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.tourism_bias = layers.Embedding(sum_tourism, 1) # layer embedding tourism bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    tourism_vector = self.tourism_embedding(inputs[:, 1]) # memanggil layer embedding 3
    tourism_bias = self.tourism_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_tourism = tf.tensordot(user_vector, tourism_vector, 2)

    x = dot_user_tourism + user_bias + tourism_bias

    return tf.nn.sigmoid(x) # melakukan aktivasi sigmoid

"""Proses di atas adalah pembuatan sebuah class model neural network menggunakan Keras untuk sistem rekomendasi (Recommendation System). Class model ini disebut "RecommenderNet". Tujuan dari class ini adalah untuk mengimplementasikan sebuah sistem rekomendasi berbasis collaborative filtering menggunakan metode matrix factorization dengan menggunakan layer embedding pada model neural network. Selanjutnya, melakukan proses compile pada class diatas sebagai model."""

# melakukan inisiasi model
model = RecommenderNet(sum_user, sum_tourism, 50)

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""Tujuannya dari inisiasi dan kompilasi model adalah untuk mempersiapkan model agar siap digunakan untuk proses training dan evaluasi. Model yang digunakan memiliki beberapa parameter seperti Binary Crossentropy untuk menghitung loss function, Adam (Adaptive Moment Estimation) sebagai optimizer, dan root mean squared error (RMSE) sebagai metrics evaluation.

Selanjutnya, melakukan proses training data pada model.
"""

history = model.fit(
    x = X_train,
    y = Y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (X_val, Y_val)
)

"""Melakukan visualisasi pada hasil training."""

import matplotlib.pyplot as plt

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

df_place = place_new
data_rating_place = pd.read_csv('/content/tourism_rating.csv')

# mengambil sample user secara acak
user_id = data_rating_place.User_Id.sample(1).iloc[0]
place_visited_by_user = data_rating_place[data_rating_place.User_Id == user_id]

# Menerapkan operator bitwise
place_not_visited = df_place[~df_place['id'].isin(place_visited_by_user.Place_Id.values)]['id']
place_not_visited = list(
    set(place_not_visited)
    .intersection(set(encoded_tourism_id.keys()))
)

place_not_visited = [[encoded_tourism_id.get(x)] for x in place_not_visited]
user_encoder = encoded_user_id.get(user_id)
user_place_array = np.hstack(
    ([[user_encoder]] * len(place_not_visited), place_not_visited)
)

"""Tujuan dari kode di atas adalah untuk memperoleh tempat wisata yang belum dikunjungi oleh seorang pengguna (user) tertentu berdasarkan data rating tempat wisata yang ada. Selanjutnya, melakukan prediksi untuk memberikan rekomendasi tempat wisata kepada user yang dipilih secara acak."""

ratings_result = model.predict(user_place_array).flatten()

top_ratings_indices = ratings_result.argsort()[-10:][::-1]
recommended_place_by_id = [
    encoded_tourism_id.get(place_not_visited[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Top Place Ratings from user')
print('----' * 8)

top_place_user = (
    place_visited_by_user.sort_values(
        by = 'Place_Ratings',
        ascending=False
    )
    .head(5)
    .Place_Id.values
)

place_data_rows = df_place[df_place['id'].isin(top_place_user)]
for row in place_data_rows.itertuples():
    print(row.place_name, ':', row.category)

print('----' * 8)
print('Top 10 place recommendation')
print('----' * 8)

recommended_place = df_place[df_place['id'].isin(recommended_place_by_id)]
for row in recommended_place.itertuples():
    print(row.place_name, ':', row.category)