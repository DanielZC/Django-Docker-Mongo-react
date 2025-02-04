import React from "react";

const DinamycTable = ({ colums = [], data = [] }) => (
  <table className="table-fixed border-collapse border border-sky-500 rounded-md text-center text-white shadow-lg shadow-blue-500/50 w-full">
    <caption className="caption-top">Tabla de usuarios</caption>
    <thead>
      <tr>
        {colums.map((column, index) => (
          <th key={index} className="py-2">
            {column.header}
          </th>
        ))}
      </tr>
    </thead>
    <tbody className="">
      {data.map((row, rowIndex) => (
        <tr key={rowIndex} className="border border-sky-500">
          {colums.map((colum, colIndex) => (
            <td key={colIndex} className="py-2">
              {row[colum.accessor]}
            </td>
          ))}
        </tr>
      ))}
    </tbody>
  </table>
);

export default DinamycTable;
