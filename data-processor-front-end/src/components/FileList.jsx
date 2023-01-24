import React, { useState, useEffect } from "react";
import { Table, Button } from "antd";
import { API_URL } from '../utils/constants';

function FileList() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    fetch(`${API_URL}/getAllFiles`)
      .then(response => response.json())
      .then(data => setFiles(data));
  }, []);

  const handleFileDelete = (fileId) => {
    fetch(`${API_URL}/deleteFile/${fileId}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => console.error(error));
}


  const columns = [
    {
      title: "ID",
      dataIndex: "id",
      key: "id",
    },
    {
      title: "Title",
      dataIndex: "title",
      key: "title"
    },
    {
      title: "Description",
      dataIndex: "description",
      key: "description"
    },
    {
      title: "Model",
      dataIndex: "model",
      key: "model"
    },
    {
      title: "File Path",
      dataIndex: "file_path",
      key: "file_path"
    },
    {
      title: "Timestamp",
      dataIndex: "timestamp",
      key: "timestamp"
    },
    {
      title: 'Action',
      key: 'action',
      render: (_, record) => (
        <Button type="link" danger onClick={()=>handleFileDelete(record.id)}>Delete</Button>
      ),
    },
  ]; 

  return (
    <Table dataSource={files} columns={columns} rowKey="id" />
  );
}

export default FileList;
