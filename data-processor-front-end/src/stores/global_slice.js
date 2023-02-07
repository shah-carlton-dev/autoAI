import { createSlice } from '@reduxjs/toolkit';

export const globalSlice = createSlice({
  name: 'global',
  initialState: {
    themeMode: 'light',
    files: []
  },
  reducers: {
    toggleTheme: (state) => {
      state.themeMode = (state.themeMode === 'light') ? 'dark' : 'light';
    },
    setFiles: (state, action) => {
      state.files = action.payload;
    }
  },
})

// Action creators are generated for each case reducer function
export const { toggleTheme, setFiles } = globalSlice.actions

export default globalSlice.reducer