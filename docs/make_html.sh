python main.py
make clean
make html
\cp -r ./build/html/* .
cd ..
git add .
git commit -m 'new commits'
git push -u origin main
