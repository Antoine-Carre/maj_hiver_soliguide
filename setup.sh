mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"antoine.carre@gmx.com\"\n\
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
