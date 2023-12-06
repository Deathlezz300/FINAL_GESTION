import lupa from '../assets/images/lupa.webp'
import {useState,ChangeEvent} from 'react'
import { EvaluateHttp } from '../utils/HelpersFunction';
import { MainHook } from '../Hooks/MainHook';

export const Filtros = () => {

  const {fetchData}=MainHook();

  const [select,SetSelect]=useState<string>("");

  const [inputValue,SetInput]=useState<string>("");

  const onChangeEtiqueta=(evento:ChangeEvent<HTMLSelectElement>)=>{
    const {target}=evento;
    SetSelect(target.value);

    const decision=EvaluateHttp(target.value);

    if(decision) fetchData(target.value);

  }

  const onSubmitOption=(evento:ChangeEvent<HTMLFormElement>)=>{

    evento.preventDefault();

    if(select==="" || inputValue==="") return;

    fetchData(select,inputValue);

  }


  return (
    <section className="w-[100%] flex gap-2 justify-center items-center h-fit pt-6">
        <form onSubmit={onSubmitOption} className="flex gap-1 w-[55%] bg-[#1E1E1E] rounded-lg focus-within:border-2 focus-within:border-white">
            <input onChange={(e)=>SetInput(e.target.value)} value={inputValue} type="text" required className="w-[95%] 
            rounded-lg shadow-md py-3 font-rubik font-medium outline-none text-white px-2 bg-[#1E1E1E]
            " />
            <button type='submit' className='cursor-pointer rounded-lg bg-[#1E1E1E]'>
                <img src={lupa} className='w-5' alt="" />
            </button>
        </form>
        <select onChange={onChangeEtiqueta} className='py-3 px-2 rounded-lg bg-[#1E1E1E] font-rubik text-white'>
            <option value=""></option>
            <option value="artistas">Artistas</option>
            <option value="artista">Artista</option>
            <option value="nacionalidad">Nacionalidad</option>
            <option value="rango">Rango</option>
            <option value="cancion">Canción</option>
            <option value="alegres">Alegres</option>
            <option value="bailables">Bailables</option>
            <option value="tripletas">Tripletas</option>
            <option value="clases">Clases</option>
        </select>
    </section>
  )
}
