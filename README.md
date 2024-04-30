# FMEA Analysis Tool - ML Module

Nástroj vyvinut v rámci Diplomové práce na téma "Nástroj pro tvorbu FMEA analýzy" na Fakultě elektrotechniky a informatiky VŠB-TU Ostrava.

## Složení týmu

- Bc. Adam Krček
- Bc. Vojtěch Grycz

## Seznam repozitářů

- FMEA Analysis Tool - Frontend
- FMEA Analysis Tool - Backend
- FMEA Analysis Tool - Infrastructure
- FMEA Analysis Tool - ML Module (tento repozitář)

## Požadavky

- Python 3.11.8
- poetry
- Docker

## Install and run

```bash
./start.sh
```

## Docker build

```bash
docker build -t fmeaprediktor .
```

## Docker run

```bash
docker run -d -p 8000:80 -v <path_to_config_ini>:/app/config.ini --name fmeaprediktor fmeaprediktor
```

## Nasazení na produkční prostředí

Pomocí CI/CD pipeline je možné nasadit aplikaci na produkční prostředí. Projekt je určený pro nasazení v prostředí Azure.

Tento modul je možné nasadit samostatně, ale je určený pro spolupráci s Frontendem aplikace.
