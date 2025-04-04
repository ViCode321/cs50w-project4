# Project Chirstian toguether
Red social enfocad hacia la comunidad cristiana llamada Chirstian toguether, un usario puede acceder a ella o registrarse, luego de registrarse es enviado
al template foto.html en el cual el usuario puedo agregar su foto de perfil y hacer una biografía, luego de esto se dirige al home.html donde el usuario puede ver las publicaciones y hacer publicaciones, hay un módulo de la app que brinda al usuario 
una forma para agregar versículos bíblicos de manera mas automatizada.

Usa una api de para obtener la ubicación del usuario, y otra api para cargar versículos bíblicos.

# Configuración del Entorno Virtual

Este proyecto utiliza un entorno virtual para gestionar las dependencias. A continuación, se describen los pasos para configurar un entorno virtual en diferentes sistemas operativos.

## Windows

1. Abre la línea de comandos (Command Prompt) o PowerShell.

2. Navega al directorio raíz de tu proyecto utilizando el comando `cd`:
```bash
cd ruta/a/tu/proyecto
```
3. Crea el entorno virtual en Windows
```bash
python -m venv myenv
```

4. Activa el entorno virtual en powershell
```bash
.\myenv\Scripts\Activate.ps1
```

## macOS y Linux

1. Crea el entorno virtual en macOS y Linux
```bash
python3 -m venv myenv
```
2. Activa el entorno virtual en macOS y Linux
```bash
source myenv/bin/activate
```

## Instalar los paquetes del proyecto

Puedes instalar todos los paquetes necesarios para el proyecto utilizando el siguiente comando:

```bash
pip install -r requirements.txt
```
