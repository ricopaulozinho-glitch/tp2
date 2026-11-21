---
sidebar_position: 2
---

# Instalação

## 1. Obter o código

```bash
git clone https://github.com/grupo-ade/biblioconsole.git
cd biblioconsole/TP2_app
```

## 2. Criar ambiente virtual (opcional)

<details>
<summary>Linux / macOS</summary>

```bash
python3 -m venv .venv
source .venv/bin/activate
```

</details>

<details>
<summary>Windows (PowerShell)</summary>

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

</details>

## 3. Executar

```bash
PYTHONPATH=src python -m biblioteca
```

Os dados são guardados em `dados/biblioteca.json`.

## 4. Correr os testes

```bash
pip install -r requirements-dev.txt
python -m pytest
```

:::warning Cópia de segurança
Antes de atualizar a aplicação, copie o ficheiro `dados/biblioteca.json`.
:::
