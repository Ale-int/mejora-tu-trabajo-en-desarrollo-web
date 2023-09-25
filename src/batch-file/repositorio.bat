@echo off
color A

echo Preparándose para la creación de la carpeta. ¿Desea continuar (S/N)? [S/N]
choice /c SN /n /m "Elija S para continuar o N para cancelar: "
if errorlevel 2 (
    echo Operación cancelada.
    goto :end
)

set /p "foldername=Introduzca el nombre de la carpeta a crear: "
if "%foldername%"=="" (
    echo El nombre de la carpeta no puede estar vacío.
    goto :end
)

rem Crear la estructura de carpetas
md "%foldername%"
mkdir "%foldername%\src"
mkdir "%foldername%\src\css"
type nul > "%foldername%\src\css\styles.css"
mkdir "%foldername%\src\js"
type nul > "%foldername%\src\js\main.js"
mkdir "%foldername%\src\imgs"

rem Crear archivos HTML básicos
(
    echo ^<!DOCTYPE html^>
    echo ^<html lang="es"^>
    echo.
    echo ^<head^>
    echo.    ^<meta charset="UTF-8"^>
    echo.    ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
    echo.    ^<title^>Document^</title^>
    echo ^</head^>
    echo.
    echo ^<body^>
    echo.
    echo ^</body^>
    echo ^</html^>
) > "%foldername%\index.html"

rem Agregación de texto al archivo CSS

(
    echo /* Estilos Globales */
) > "%foldername%\src\css\styles.css"

rem Agregación de texto al archivo JS

(
    echo // JavaScript Code
) > "%foldername%\src\js\main.js"

echo Carpeta y archivos creados exitosamente.

:end
pause > nul
