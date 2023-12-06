import { createSlice } from '@reduxjs/toolkit';

export const MainSlice = createSlice({
    name: 'Main',
    initialState: {
     mainData:[],
     mostarFrames:false,
     columnas:[],
     filas:[],
     mostrarTabla:true
    },
    reducers: {
         setMainData:(state,{payload})=>{
            state.mainData=payload;
         },
         SetMostrarFrames:(state,{payload})=>{
            state.mostarFrames=payload;
         },
         SetColumnas:(state,{payload})=>{
            state.columnas=payload;
         },
         SetFilas:(state,{payload})=>{
            state.filas=payload;
         },
         SetMostrarTabla:(state,{payload})=>{
            state.mostrarTabla=payload;
         }
    }
});


// Action creators are generated for each case reducer function
export const { setMainData,SetMostrarFrames,SetColumnas,SetFilas,SetMostrarTabla } = MainSlice.actions;