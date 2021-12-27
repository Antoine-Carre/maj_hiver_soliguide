mkdir -p ~/.streamlit/

echo "
[general]
email = \"antoine.carre@gmx.com\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
