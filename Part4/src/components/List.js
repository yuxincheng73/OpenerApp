import React, { useState, useEffect, useRef } from 'react';
import Card from './Card';
import './List.css';
import './Card.css';

const List = (props) => {
    const item = props.item
    const [showDropdown, setShowDropdown] = useState(false);
    const dropdownRef = useRef(null);

    //toggle dropdown
    const toggle = () => {
        setShowDropdown(!showDropdown);
        console.log(showDropdown)
    }

    return (
        <div>
            <div className="list" onClick={toggle}>
                <div className='list-body' >
                    <ul>
                        <li className='list-item'>EmployeeId: {item.employeeId}</li>
                        <li className='list-item'>Employee Name: {item.name}</li>
                    </ul>
                </div>
            </div>
            {showDropdown ? (
                <div className='card-container'>
                    <Card item={item} show={showDropdown} innerRef={dropdownRef} onClickOutside={() => {setShowDropdown(false)}} />
                </div>
            ) : (null)
            }

        </div>
    )
}

export default List