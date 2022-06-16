import React from 'react'
import List from './List';
import './SearchList.css';
import './List.css';

const SearchList = ({ filteredData }) => {
    return (
        <div className='list-container'>
            {filteredData.map((item, i) => {
                return (
                    <div>
                        <List key={i} item={item} />
                    </div>
                )
            })}
        </div>
    )
}

export default SearchList