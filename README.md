# ERP Portal User Interaction 

 Este repositorio contiene un script en Python que demuestra el proceso de autenticación con el Cloud Portal User system y la comprobación del user's status. 
 
## Overview

El script realiza los siguientes pasos:

1.  **Signs in to the Cloud Portal User system** using a `POST` request to the `/web-oauth/signin` endpoint with the provided credentials (`ClientId`, `username`, `userpassword`) and the `X-WEB-KEY` header.
2.  **Extrae el `web_token`** del successful sign-in response. 
3.  **Comprueba el Portal User status** mediante una `GET` request al `/check` endpoint para la plataforma especificada (`cloudframework`).
4.  **Prints the JSON responses** de sign-in and check requests y comprobación en la consola.

## Prerequisites

* **Python 3.x** instalado en su sistema.
* The **`requests` library** Para realizar HTTP requests. Puede instalarlo utilizando pip:
    ```bash
    pip install requests
    ```
  
## Setup and Usage

1.  **Clone this repository** (if you haven't already) to your local machine:
    ```bash
    git clone https://github.com/MohamedAmineRami/CF_API_Integration-.git>
    cd CF_API_Integration-
    ```
    
## Troubleshooting and Lessons Learned

Durante el desarrollo de este script, me encontré con algunos desafíos que muestran la importancia de una cuidadosa API interaction y documentation review:

   - **Incorrect `web_token` Extraction Path:** Inicialmente, el script no pudo extraer el `web_token` del sign-in response debido a una suposición incorrecta sobre la estructura JSON basada en un snippet parcial de la documentación. Al utilizar `print(json.dumps(data_signin, indent=4))` para inspeccionar la respuesta completa, pudimos identificar la ruta correcta al `web_token` dentro del data dictionary en el nivel superior del JSON.


**Author:**
[Mohamed Amine Rami]