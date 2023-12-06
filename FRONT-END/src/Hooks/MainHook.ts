import { RootState } from '../store/store';
import {useSelector,useDispatch} from 'react-redux'
import { evaluarMostrarFrames, extraerUrls, findUrlByOption, organizarFilas, organizarFilasArtistas } from '../utils/HelpersFunction';
import SpotifyApi from '../Api/SpotifyApi';
import { SetColumnas, SetFilas, SetMostrarFrames, SetMostrarTabla, setMainData } from '../store/MainSlice';


export const MainHook=()=>{


    const dispatch=useDispatch();

    const {mainData,mostarFrames,mostrarTabla,filas,columnas}=useSelector((e:RootState)=>e.main);


    const fetchData=async(opcion:string,buscador?:string)=>{

        try{

            const url=findUrlByOption(opcion);

            const {data}= await SpotifyApi.post(`http://127.0.0.1:8000/${url}`,{valor:buscador});

            console.log(data);

            const mostrarFrames=evaluarMostrarFrames(opcion)

            if(mostrarFrames){
                const urls=extraerUrls(data,opcion);
                dispatch(setMainData(urls))
                dispatch(SetMostrarFrames(true));
            }else{
                dispatch(SetMostrarFrames(false));
            }

            if(opcion==="artista"){
                dispatch(SetMostrarTabla(false))
            }else{
                dispatch(SetMostrarTabla(true))
            }

            if(opcion==="artistas"){
                dispatch(SetFilas(organizarFilasArtistas(data)))
                dispatch(SetColumnas(['Nombre',"Nacionalidad"]))
            }else{
                dispatch(SetColumnas(data.vars));
                dispatch(SetFilas(organizarFilas(data._bindings)))
            }


        }catch(error){
            console.log(error);
        }

    }

    return{
        mainData,
        fetchData,
        mostarFrames,
        mostrarTabla,
        filas,
        columnas
    }


}