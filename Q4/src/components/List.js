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

    //handle clicking outside to toggle dropdown
    useEffect(() => {
        const handleClickOutside = (e) => {
            //if the dropdown is active AND click was outside of dropdown element
            if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
                setShowDropdown(false)
                console.log(showDropdown)
            }
        };

        //only if dropdown is shown, listen for clicks
        if (showDropdown) {
            document.addEventListener('click', handleClickOutside, true);
        }
        return () => {
            document.removeEventListener('click', handleClickOutside, true);
        }
    }, [showDropdown]);

    return (
        <div className='list-wrapper' ref={dropdownRef}>
            <div className="list" onClick={toggle}>
                <div className='list-body' >
                    <ul>
                        <li className='list-item'>EmployeeId: {item.employeeId}</li>
                        <li className='list-item'>Employee Name: {item.name}</li>
                    </ul>
                </div>
            </div>
            {showDropdown ? (
                <div className='card-wrapper'>
                    <div className='card-container'>
                        <Card item={item} />
                    </div>
                </div>
            ) : (null)
            }
        </div>
    )
}

export default List