import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import FileUploadForm from './components/FileUploadForm';
// import CoolList from './components/tables/CoolList';
import FileList from './components/tables/FileList';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <FileUploadForm/>
        <FileList/>
        {/* <CoolList/> */}
      </header>
    </div>
  );
}

export default App;
