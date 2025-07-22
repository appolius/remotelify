# Remotelify

Flask-based content uploader for signage devices. Built for remote drag-and-drop file management over Tailscale, using a simple, responsive interface and automatic file playback.

---

## 📁 Folder Structure

remotelify/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
│   └── templates/
│       └── index.html
├── .env
├── .env-example
├── main.py
├── requirements.txt
├── Dockerfile
├── run.sh
├── remotelify.service
└── README.md

---

## ⚙️ Environment Configuration

Create a `.env` file based on `.env-example`:

```
cp .env-example .env
```

Default values:

```
UPLOAD_FOLDER=~/RemotelifyContent
SECRET_KEY=supersecretkey
FLASK_PORT=5000
```

---

## 🚀 Manual Run (Python venv)

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

---

## 🐳 Docker Setup

### Build image:

```
docker build -t remotelify .
```

### Run container:

```
docker run -d \
  --name remotelify \
  --restart=unless-stopped \
  -p 5000:5000 \
  -v ~/RemotelifyContent:/root/RemotelifyContent \
  --env-file .env \
  remotelify
```

> Replace `~/RemotelifyContent` with your preferred host path if needed.

---

## ⚙️ Auto Start on Boot (systemd)

### Step 1: Add `remotelify.service` file

Save this file to:  
`/etc/systemd/system/remotelify.service`

```
[Unit]
Description=Remotelify Flask Uploader
After=network.target

[Service]
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME/remotelify
ExecStart=/home/YOUR_USERNAME/remotelify/.venv/bin/python main.py
EnvironmentFile=/home/YOUR_USERNAME/remotelify/.env
Restart=always

[Install]
WantedBy=multi-user.target
```

Replace `YOUR_USERNAME` with your actual Linux username.

### Step 2: Enable and start

```
sudo systemctl daemon-reload
sudo systemctl enable remotelify
sudo systemctl start remotelify
```

---

## 🧩 Included Scripts

### `run.sh` – Quick dev run

```
#!/bin/bash
source .venv/bin/activate
python main.py
```

> Make it executable:

```
chmod +x run.sh
```

---

## 📂 File Management

- Upload supported file types: `.mp4`, `.jpg`, `.png`
- Uploaded files stored in `$UPLOAD_FOLDER`
- Files can be downloaded or deleted via the web interface
- Content is used for signage autoplay

## 📂 Auto play
```
chmod +x display_content.sh
./display_content.sh

```

---

## 🔐 Remote Access

Use [Tailscale](https://tailscale.com/) to securely access this device across networks. No port forwarding or VPN needed.

---

## ✅ Notes

- The interface is fully offline-capable after setup.
- Auto-plays uploaded content in fullscreen loop (if paired with VLC playback script)

