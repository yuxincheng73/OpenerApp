import React, { useState } from 'react'
import SearchList from './SearchList';
import './Search.css';
import './SearchList.css';

const Search = ({ data }) => {
    const [searchTerm, setSearchTerm] = useState("");

    //filtered words to search by 
    const filteredData = data.filter((val) => {
            if (searchTerm == "") {
                return val
            } else if (val.name.toLowerCase().includes(searchTerm.toLowerCase()) || val.email_address.toLowerCase().includes(searchTerm.toLowerCase())){
                return val
            }
        }
    );

    return (
        <div className='search-container'>
            <div className='search'>
                <input type="text" placeholder='Search Employee Name or Email...' onChange={(e) => {
                    setSearchTerm(e.target.value);
                }}
                />
            </div>
            <SearchList filteredData={filteredData} />
        </div>
    )
}

export default Search