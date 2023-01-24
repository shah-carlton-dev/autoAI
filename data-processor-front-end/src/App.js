import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import FileUploadForm from './components/FileUploadForm';
import FileList from './components/FileList';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <FileUploadForm/>
        <FileList/>
      </header>
    </div>
  );
}

export default App;
