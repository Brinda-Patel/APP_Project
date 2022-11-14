import { Box, Button, TextField } from '@mui/material';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
// import { HOST } from '../App';
import "./Dashboard.css";

import CustomTable from './Helpers/CustomTable';

const columnData = [
    {
        id: "movieDetail_id",
        label: "ID"
    },
    {
        id: "title",
        label: "Title"
    },
    {
        id: "movieIMDbRating",
        label: "MovieIMDbRating"
    },
    {
        id: "totalRatingCount",
        label: "TotalRatingCount"
    },
    {
        id: "totalUserReviews",
        label: "TotalUserReviews"
    },
    {
        id: "totalCriticReviews",
        label: "TotalCriticReviews"
    },
    {
        id: "directorName",
        label: "DirectorName"
    },
    {
        id: "datePublished",
        label: "DatePublished"
    },
    {
        id: "actorName",
        label: "ActorName"
    },
    {
        id: "description",
        label: "Description"
    },
    {
        id: "duration",
        label: "Duration"
    }
]
const Dashboard = () => {
    const [value, setValue] = useState("")
    const [rowData, setRowData] = useState([])

    const getDataFromAPI = async () => {
        await axios.get("http://127.0.0.1:8000/DisplayMovieDetails").then(({ data }) => {
            // console.log(data)
            setRowData(data["movieDetail"])
        })
    }


    useEffect(() => {
        getDataFromAPI()
        return () => {
            setRowData([])
        }
    }, [])


    const handleChange = (event) => {
        setValue(event.target.value)
    }
    return (
        <div className='container'>
            <div>
                <CustomTable columnData={columnData} rowData={rowData} />
            </div>
        </div>
    )
}

export default Dashboard