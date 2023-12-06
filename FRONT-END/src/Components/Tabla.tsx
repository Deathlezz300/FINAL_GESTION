import React,{FC} from 'react'

interface props{
    columnas:string[],
    filas:any[]
}

export const Tabla:FC<props> = ({columnas,filas}) => {
  return (
    <table style={{borderCollapse:'separate',borderSpacing:'7px'}} className='divide-white  w-[100%] border-2 border-white'>
      <thead className='divide-white'>
        <tr >
          {
            columnas.map((colum)=>{
              return <th className='text-white font-rubik text-left border-2 border-white'>{colum}</th>
            })
          }
        </tr>
      </thead>
      <tbody className='divide-white'>
          {
            filas.map(value=>{
              return(
                <tr>
                  {
                    value.map((dato:any)=>{
                      return <td className='text-white font-rubik '>{dato}</td>
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
