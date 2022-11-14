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
    const [searchValue, setValue] = useState("")
    const [rowData, setRowData] = useState([])
    const [filterData, setFilterData] = useState([])

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

    const onSearch = () => {
        const newData = rowData.filter((row) => {
            console.log(searchValue.toLowerCase())
            console.log(searchValue.toLowerCase().startsWith(row["actorName"].toLowerCase()))
            return row["actorName"].toLowerCase().search(searchValue) != -1
        })

        console.log("Filter result")
        console.log(newData)

        setFilterData(newData)
    }
    const onSearch1 = () => {
        const newData = rowData.filter((row) => {
            console.log(searchValue.toLowerCase())
            console.log(searchValue.toLowerCase().startsWith(row["directorName"].toLowerCase()))
            return row["directorName"].toLowerCase().search(searchValue) != -1
        })

        console.log("Filter result")
        console.log(newData)

        setFilterData(newData)
    }

    const handleChange = (event) => {
        if (event.target.value == "") {
            setFilterData([])
        }
        setValue(event.target.value.toLowerCase())
    }
    const handleChange1 = (event) => {
        if (event.target.value == "") {
            setFilterData([])
        }
        setValue(event.target.value.toLowerCase())
    }
    return (
        <div className='container'>
            <Box sx={{ display: "inline-flex", alignItems: "inline"}}>
                <Box sx={{ padding: "10px",  position: "-10px" }}>
                    <TextField
                        hiddenLabel
                        id="filled-hidden-label-small"
                        defaultValue=""
                        placeholder='Actor Name Filter'
                        variant="outlined"
                        size="small"
                        onKeyDown={handleChange}
                    />
                    <Button onClick={() => onSearch()} variant="contained" sx={{ marginLeft: "20px", backgroundColor:"#CCF381", fontWeight:"bold" }}>Search</Button>
                </Box>
                <Box sx={{  padding: "10px", position:"-10px", marginLeft:"525px" }}>
                    <TextField
                        hiddenLabel
                        id="filled-hidden-label-small"
                        defaultValue=""
                        placeholder='Director Name Filter'
                        variant="outlined"
                        size="small"
                        onKeyDown={handleChange1}
                    />
                    <Button onClick={() => onSearch1()} variant="contained" sx={{ marginLeft: "20px", backgroundColor:"#CCF381", fontWeight:"bold"}}>Search</Button>
                </Box>
            </Box>
            <div>
                <CustomTable columnData={columnData} rowData={filterData.length == 0 ? rowData : filterData} />
            </div>
        </div>
    )
}

export default Dashboard