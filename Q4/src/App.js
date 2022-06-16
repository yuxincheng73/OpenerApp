import React, { useState, useEffect } from 'react';
import './App.css';
import { employees } from './data';
import List from './components/List';
import Card from './components/Card';
import Search from './components/Search';
import './components/List.css';
import './components/Card.css';
import './components/Search.css';

function App() {
  const [data, setData] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  //initalize data to hardcoded employee json object
  useEffect(() => {
    setData(employees.employees)
  }, [])

  return (
    <div className='app'>
      <div className='header'>
        <h1 className='header-text'>Employee Information</h1>
      </div>
      <div className='app-main'>
        <Search data={data} />
      </div>
    </div>
  );
}

export default App;
