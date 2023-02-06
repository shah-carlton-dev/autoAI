import { createSlice } from '@reduxjs/toolkit';

export const globalSlice = createSlice({
  name: 'global',
  initialState: {
    themeMode: 'light',
  },
  reducers: {
    toggleTheme: (state) => {
      state.themeMode = (state.themeMode === 'light') ? 'dark' : 'light';
    }
  },
})

// Action creators are generated for each case reducer function
export const { toggleTheme } = globalSlice.actions

export default globalSlice.reducer