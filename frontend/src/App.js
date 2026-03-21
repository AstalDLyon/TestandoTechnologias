import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:5000/projects')
      .then(response => {
        setProjects(response.data);
      })
      .catch(error => {
        console.error('Erro ao buscar projetos:', error);
      });
  }, []);

  return (
    <div>
      <h1>Projetos</h1>
      <ul>
        {projects.map((project, index) => (
          <li key={index}>{project.nome}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
