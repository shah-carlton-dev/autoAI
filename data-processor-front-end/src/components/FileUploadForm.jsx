import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { API_URL } from "../utils/constants";

function FileUploadForm() {
  const [file, setFile] = useState(null);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [model, setModel] = useState("test-01");

  const handleFileChange = e => {
    setFile(e.target.files[0]);
  };

  const handleTitleChange = e => {
    setTitle(e.target.value);
  };

  const handleDescriptionChange = e => {
    setDescription(e.target.value);
  };

  const handleModelChange = e => {
    setModel(e.target.value);
  };

  const handleSubmit = e => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);
    formData.append("title", title);
    formData.append("description", description);
    formData.append("model", model);
    fetch(`${API_URL}/uploadFile`, {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error(error));
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group>
        <Form.Label>File</Form.Label>
        <Form.Control type="file" onChange={handleFileChange} />
      </Form.Group>
      <Form.Group>
        <Form.Label>Title</Form.Label>
        <Form.Control type="text" value={title} onChange={handleTitleChange} />
      </Form.Group>
      <Form.Group>
        <Form.Label>Description</Form.Label>
        <Form.Control type="text" value={description} onChange={handleDescriptionChange} />
      </Form.Group>
      <Form.Group>
    <Form.Label>Model</Form.Label>
    <Form.Control as="select" value={model} onChange={handleModelChange}>
        <option value="test-01">test-01</option>
        <option value="test-02">test-02</option>
        <option value="test-03">test-03</option>
    </Form.Control>
  </Form.Group>
  <Form.Group>
    <Button variant="primary" type="submit">
        Upload
    </Button>
  </Form.Group>
</Form>
  )};

export default FileUploadForm;