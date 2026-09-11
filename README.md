# 01-poos-n2p13c3
## Luis Arriagada

A continuación se detalla el flujo de comandos de Git utilizados en este proyecto, junto con su propósito:

### 1. Clonar el repositorio
```bash
git clone url_proyecto .
```
**Explicación:** Descarga el repositorio remoto desde la `url_proyecto` y coloca todo su contenido directamente en la carpeta actual (gracias al punto `.`), evitando que se cree una subcarpeta con el nombre del proyecto.

### 2. Configurar credenciales de usuario
```bash
git config --global user.name "usuario_github"
git config --global user.email "email_github"
```
**Explicación:** Establece a nivel global (para todos los proyectos en tu computadora) el nombre y el correo electrónico que quedarán registrados como autor en cada uno de los *commits* que realices. Es importante que el correo coincida con el de tu cuenta de GitHub.

### 3. Verificar la configuración
```bash
git config --global --list
```
**Explicación:** Despliega una lista con todas las configuraciones globales que tiene Git actualmente, lo que permite comprobar que el nombre de usuario y el email quedaron bien guardados.

### 4. Preparar los archivos (Staging)
```bash
git add .
```
**Explicación:** Añade todos los archivos nuevos, modificados o eliminados del directorio actual al área de preparación (*staging area*). Esto le dice a Git qué cambios deben incluirse en el próximo guardado.

### 5. Confirmar los cambios (Commit)
```bash
git commit -m "avance clase paciente"
```
**Explicación:** Toma una "fotografía" de los archivos preparados en el paso anterior y los guarda en el historial local del repositorio. El parámetro `-m` permite adjuntar un mensaje descriptivo para saber de qué trata este cambio (en este caso, un avance en la clase paciente).

### 6. Subir los cambios (Push)
```bash
git push origin main
```
**Explicación:** Sincroniza el repositorio local con el remoto. Envía todos tus *commits* hacia la rama principal (`main`) del servidor original (`origin`), actualizando el código en la plataforma de GitHub.