import { IApi } from "../interface/ApiInterface";

export const EvaluateHttp=(opcion:string)=>{

    if(opcion==="artistas") return true;

    if(opcion==="tripletas") return true;

    if(opcion==="clases") return true;

    return false;

}

const possiblesUrls:IApi[]=[
    {
        nombre:"artistas",
        url:'artistas_Y_nacionalidad'
    },
    {
        nombre:"artista",
        url:"cancioneArtistaEspecifico"
    },
    {
        nombre:"nacionalidad",
        url:"filtrarPorNacionalidad"
    },
    {
        nombre:"rango",
        url:"topN"
    },
    {
        nombre:"cancion",
        url:"buscarPorCancion"
    },
    {
        nombre:"alegres",
        url:"cancionesAlegres"
    },
    {
        nombre:"bailables",
        url:"cancionesMaxBailabilidad"
    },
    {
        nombre:"tripletas",
        url:"mostrarTripletas"
    },
    {
        nombre:"clases",
        url:"clases_etiqueta_descripcion"
    }
]


export const findUrlByOption=(opcion:string):string=>{

    const urlOption=possiblesUrls.find((url)=>url.nombre===opcion);

    if(urlOption) return urlOption.url;

    return '';

}

export const organizarFilas=(filas:any)=>{

    let matriz:any=[];

    filas.forEach((fila:any)=>{
        let array=[];
        for(let propiedad in fila){
            array.push(fila[propiedad]);
        }
        matriz.push(array)
        array=[];
    })

    return matriz;

}

export const organizarFilasArtistas=(data:any)=>{

    let matriz:any=[];
    let array=[];

    const keys=Object.keys(data);

    for(let fila in data){
        array.push(data[fila])
    };

    for(let x=0;x<array.length;x++){
        matriz.push([keys[x],array[x]])
    }

    return matriz;

}

export const evaluarMostrarFrames=(opcion:string)=>{

    if(opcion==="artista") return true;

    if(opcion==="rango") return true;

    if(opcion==="cancion") return true;

    if(opcion==="alegres") return true;

    if(opcion==="bailables") return true;


    return false;

}

export const extraerUrls=(data:any,opcion:string)=>{

    let urls:any=[];
    if(opcion==="artista"){
        for (let valor in data){
            urls.push(data[valor])
        }

        return urls;
    }

    if(opcion==="cancion"){
        urls.push(data._bindings[0].URL)
        return urls;
    }

    data._bindings.forEach((valor:any)=>{

        urls.push(valor.URL);

    });

    return urls;

}