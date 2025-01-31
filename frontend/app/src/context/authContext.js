import React, { createContext, useState } from "react";

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [users, setUsers] = useState(null);
  return (
    <AuthContext.Provider value={{ users, setUsers }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;
