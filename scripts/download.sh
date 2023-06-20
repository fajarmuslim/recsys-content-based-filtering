ls -lha kaggle.json
pip install -q kaggle
mkdir -p ~/.kaggle
cp kaggle.json ~/.kaggle/
chmod 600 /root/.kaggle/kaggle.json
kaggle datasets download -d tmdb/tmdb-movie-metadata
unzip tmdb-movie-metadata.zip -d dataset
rm -rf tmdb-movie-metadata.zip