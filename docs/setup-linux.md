# Linux Setup (Docker)

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose-plugin
sudo systemctl enable --now docker
cd beast/lab
docker compose up -d
