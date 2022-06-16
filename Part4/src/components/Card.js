import React, { useState, useRef, useEffect } from 'react';

const Card = (props) => {
    const item = props.item
    const showDropdown = props.show
    const {onClickOutside} = props;
    // const dropdownRef = useRef(null);
    const dropdownRef = props.innerRef;

    useEffect(() => {
        const handleClickOutside = (e) => {
            //if the dropdown is active AND click was outside of dropdown element
            if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
                onClickOutside && onClickOutside()
            }
        };

        //only if dropdown is shown, listen for clicks
        if (showDropdown) {
            document.addEventListener('click', handleClickOutside, true);
        }
        return () => {
            document.removeEventListener('click', handleClickOutside, true);
        }
    }, [dropdownRef]);

    if (!showDropdown) {
        return null;
    }

    return (
        <div className='card' >
            <div className='card-body' ref={dropdownRef}>
                <ul>
                    <li className='card-item'>Email: {item.email_address}</li>
                    <li className='card-item'>Phone: {item.phone_number}</li>
                    <li className='card-item'>Dep: {item.department}</li>
                </ul>
            </div>
        </div>
    )
}

export default Card