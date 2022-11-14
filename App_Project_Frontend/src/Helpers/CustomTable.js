import React from 'react'
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

const CustomTable = ({ columnData = [], rowData = [] }) => {
  console.log("rowData", rowData)
  return (

    <TableContainer component={Paper} sx={{
      border: "3px solid #aaa",
    }}>
      <Table  sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow style={{backgroundColor: "#154c79"}}>
            {columnData?.map((data, i) => <TableCell style={{ fontFamily: "Verdana", fontSize: "15px", fontWeight:"bold", color:"white"}} key={i}>{data.label}</TableCell>)}
          </TableRow>
        </TableHead>
        <TableBody>
          {
            rowData?.map((row, r) => <TableRow style={{backgroundColor: "#ffffff", border:"1px solid black", fontFamily: "Verdana"}} className='trStyles' key={r + " " + r}>
              {
                columnData?.map((data,iii) => <TableCell key={iii + " " + r}>{<div className='item'>{row[data.id]}</div>}</TableCell>)
              }
            </TableRow>)
          }
        </TableBody>
      </Table>
    </TableContainer>
  )
}

export default CustomTable