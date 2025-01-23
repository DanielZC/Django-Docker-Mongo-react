import React from "react";
import InputField from "../../components/forms/inputField";

const Register = () => {
  const initialValues = {
    nombre: "",
    correo_electronico: "",
    confirmar_contraseña: "",
  };

  const onSubmit = async () => {
    await alert("Datos guadados");
  };

  const { values, errors, isSubmitting, handleChange, handleSubmit } = useForm(
    initialValues,
    onSubmit
  );

  return (
    <div className="max-w-md mx-auto mt-10">
      <h1 className="text-2xl font-bold text-center">Formulario</h1>
      <form onSubmit={handleSubmit} className="mt-5">
        <InputField
          label="Nombre"
          name="name"
          value={values.name}
          onChange={handleChange}
          error={errors.name}
        />
        <InputField
          label="Email"
          name="email"
          type="email"
          value={values.email}
          onChange={handleChange}
          error={errors.email}
        />
        <button
          type="submit"
          className="w-full px-4 py-2 mt-3 text-white bg-blue-500 rounded-md hover:bg-blue-600 disabled:bg-gray-400"
          disabled={isSubmitting}
        >
          {isSubmitting ? "Enviando..." : "Enviar"}
        </button>
      </form>
    </div>
  );
};

export default Register;
