# Fmea prediktor

## Install and run

```bash
./start.sh
```

## Docker build

```bash
docker build -t fmeaprediktor:latest .
```

## Docker run

```bash
docker run -d -p 8000:80 -v <path_to_config_ini>:/app/config.ini fmeaprediktor:latest
```
