import React, { useState, useRef, useEffect } from 'react';

const Card = (props) => {
    const item = props.item

    return (
        <div className='card' >
            <div className='card-body' >
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