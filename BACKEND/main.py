from fastapi import FastAPI,Body
from fastapi import HTTPException
from rdflib.plugins.stores.sparqlstore import SPARQLStore
from starlette.middleware.cors import CORSMiddleware
from rdflib import Graph
from pydantic import BaseModel

app = FastAPI()

# Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto permite cualquier origen
    allow_credentials=True,
    allow_methods=["*"],   # Esto permite todos los métodos HTTP
    allow_headers=["*"],   # Esto permite todos los encabezados HTTP
)

class Valor(BaseModel):
    valor: str

# Conectarse a la base de datos de Apache Jena
endpoint = 'http://localhost:3030/musicaSpotify/sparql'
store = SPARQLStore(endpoint)
g = Graph(store)

@app.post("/artistas_Y_nacionalidad")
async def artistas_Y_nacionalidad():
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

            SELECT ?nombreArtista ?nombreNacionalidad
            WHERE {
              ?artista rdf:type data:Artista .
              ?artista data:NombreArtista ?nombreArtista .
              ?artista data:NacionalidadArtista ?nacionalidad .
              ?nacionalidad data:NombreNacionalidad ?nombreNacionalidad .
            }
           """

        results = g.query(query)
        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/cancioneArtistaEspecifico")
async def cancioneArtistaEspecifico(valor:Valor=Body(...)):
    try:
        query = """        
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>
        
           SELECT ?cancionNombre ?URL
            WHERE {
              ?cancion data:TituloCancion ?cancionNombre.
              ?cancion data:URLCancion ?URL .
              ?cancion data:ArtistasCancion ?artista.                    
           """
        query+=f'?artista data:NombreArtista "{valor.valor}" .'
        query+=" }"
        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/filtrarPorNacionalidad")
async def filtrarPorNacionalidad(valor:Valor=Body(...)):
    try:
        query = """        
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

           SELECT ?nombreArtista
            WHERE {
              ?artista rdf:type data:Artista.
              ?artista data:NombreArtista ?nombreArtista.
              ?artista data:NacionalidadArtista ?nacionalidad.                                            
           """
        query += f'?nacionalidad data:NombreNacionalidad "{valor.valor}" .'
        query += " }"
        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/topN")
async def topN(valor:Valor=Body(...)):
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

            SELECT DISTINCT ?titulo ?nombreArtista ?rango ?URL
            WHERE {
              ?cancion data:TituloCancion ?titulo .
              ?cancion data:RangoCancion ?rango .
              ?cancion data:ArtistasCancion ?artista.
              ?cancion data:URLCancion ?URL .
              ?artista data:NombreArtista ?nombreArtista.                      
           """
        query +=f"FILTER(?rango	<= {valor.valor})"
        query+="""
         }
            ORDER BY ASC(?rango)
        """
        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/buscarPorCancion")
async def buscarPorCancion(valor:Valor=Body(...)):
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

            SELECT ?fecha ?nombreArtista ?puntosInd ?puntosTotal ?acustica ?bailabilidad ?energia ?volumen ?valencia ?URL
            WHERE {
            """
        query += f'?cancion data:TituloCancion "{valor.valor}" .'
        query+="""
              ?cancion data:FechaCancion ?fecha .
              ?cancion data:ArtistasCancion ?artista.
              ?artista data:NombreArtista ?nombreArtista.
              ?cancion data:PuntosIndCancion ?puntosInd .
              ?cancion data:PuntosTotalCancion ?puntosTotal .
              ?cancion data:AcusticaCancion ?acustica .
              ?cancion data:BailabilidadCancion ?bailabilidad . 
              ?cancion data:EnergiaCancion ?energia .
              ?cancion data:VolumenCancion ?volumen .
              ?cancion data:ValenciaCancion ?valencia .
              ?cancion data:URLCancion ?URL .
            }
           """

        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/cancionesAlegres")
async def cancionesAlegres(valor:Valor=Body(...)):
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

            SELECT ?NombreCancion ?Valencia ?URL
            WHERE {
               ?cancion data:TituloCancion ?NombreCancion .
               ?cancion data:ValenciaCancion ?Valencia .
               ?cancion data:URLCancion ?URL .
            }
            ORDER BY DESC(?Valencia)
           """
        query+=f"LIMIT {valor.valor}"

        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/cancionesMaxBailabilidad")
async def cancionesMaxBailabilidad(valor:Valor=Body(...)):
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

            SELECT ?NombreCancion ?Bailabilidad ?URL
            WHERE {
                ?cancion data:TituloCancion ?NombreCancion .
                ?cancion data:BailabilidadCancion ?Bailabilidad .
                ?cancion data:URLCancion ?URL .
            }
            ORDER BY DESC(?Bailabilidad)
           """
        query+=f"LIMIT {valor.valor}"

        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/mostrarTripletas")
async def mostrarTripletas():
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

           SELECT ?sujeto ?predicado ?objeto 
            WHERE {
              ?sujeto ?predicado ?objeto.
            }
           """
        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

@app.post("/clases_etiqueta_descripcion")
async def clases_etiqueta_descripcion():
    try:
        query = """
            PREFIX owl: <http://www.w3.org/2002/07/owl#>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX xml: <http://www.w3.org/XML/1998/namespace/>
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX data: <http://www.spotifyproyectofinal.com/spotify#>

           SELECT DISTINCT ?class ?label ?description
            WHERE {
              ?class a owl:Class.
              OPTIONAL { ?class rdfs:label ?label}
              OPTIONAL { ?class rdfs:comment ?description}
            }
           """
        results = g.query(query)

        return results
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))

