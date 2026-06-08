import subprocess
import modal

app = modal.App("main")

image = (
    modal.Image.debian_slim(python_version="3.11")
    .apt_install("git", "curl", "ca-certificates")
    .run_commands(
        "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -",
        "apt-get install -y nodejs",
        "node -v",
        "npm -v",
        "corepack enable",
        "corepack prepare pnpm@9.15.9 --activate",
        "pnpm -v",
        "git clone https://github.com/MoonTechLab/LunaTV /app",
        "cd /app && npm install --legacy-peer-deps",
        "cd /app && pnpm gen:manifest && pnpm exec next build",
        "cd /app && mkdir -p .next/standalone/.next",
        "cd /app && cp -r .next/static .next/standalone/.next/",
        "cd /app && cp -r public .next/standalone/",
    )
    .workdir("/app")
)

@app.function(
    image=image,
    secrets=[modal.Secret.from_name("lunatv-env")],
    timeout=60 * 60,
    scaledown_window=300,
)
@modal.concurrent(max_inputs=20)
@modal.web_server(3000)
def lunatv():
    subprocess.Popen(
        "cd /app && HOSTNAME=0.0.0.0 PORT=3000 node .next/standalone/server.js",
        shell=True,
    )