import React,{FC} from 'react'

interface props{
    columnas:string[],
    filas:any[]
}

export const Tabla:FC<props> = ({columnas,filas}) => {
  return (
    <table style={{borderCollapse:'separate',borderSpacing:'0px'}} className='bg-[#121212] divide-white rounded-lg  w-[100%] shadow-md'>
      <thead className='bg-[#181818] rounded-lg'>
        <tr className='bg-[#181818] rounded-lg'>
          {
            columnas.map((colum)=>{
              return <th className='text-white font-rubik text-center p-2 py-4 rounded-lg'>{colum}</th>
            })
          }
        </tr>
      </thead>
      <tbody>
          {
            filas.map(value=>{
              return(
                <tr >
                  {
                    value.map((dato:any)=>{
                      return <td className='text-white font-rubik p-4 border border-[#1E1E1E]'>{dato}</td>
                    })
                  }
                </tr>
              )
            })
          }
      </tbody>
    </table>
  )
}
