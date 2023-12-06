import React from 'react'
import { Filtros } from '../Components/Filtros'
import { SpotifyCard } from '../Components/SpotifyCard'
import { MainHook } from '../Hooks/MainHook'
import { Tabla } from '../Components/Tabla'

export const HomePage = () => {
  
  const {mostarFrames,mostrarTabla,mainData,filas,columnas}=MainHook();
  
  return (
    <section className='w-[100%] flex-col min-h-screen items-center bg-black flex'>
        <Filtros/>
        <div className='w-[85%] flex justify-center flex-wrap gap-2 py-4'>
            {
              mostarFrames ? 
              mainData.map((url:any)=>{
                  return <SpotifyCard id={url.split("/")[4]}/>
              })
              : ''
            }
        </div>
        <div className='w-[85%] flex  flex-wrap gap-2 py-4 overflow-auto'>
            {
              mostrarTabla ? <Tabla filas={filas} columnas={columnas}/> : ''
            }
        </div>
    </section>
  )
}
