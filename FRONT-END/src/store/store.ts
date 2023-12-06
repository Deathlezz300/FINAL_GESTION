import { configureStore} from "@reduxjs/toolkit";
import { MainSlice } from "./MainSlice";
 
export const store=configureStore({
    middleware:(getDefaultMiddleware)=>getDefaultMiddleware({serializableCheck:false}),
    reducer:{
        main:MainSlice.reducer
    }
});

export type RootState =ReturnType<typeof store.getState>