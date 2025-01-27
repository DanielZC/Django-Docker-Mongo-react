import React from "react";
import { useForm } from "react-hook-form";
import InputField from "../../components/forms/inputField";

const Register = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors, isSubmitting },
  } = useForm();

  const onSubmit = async (data) => {
    console.log("enviar datos");
  };

  return (
    <div className="max-w-md text-white rounded-md dark:bg-gray-800 mx-auto color-white p-4 mt-10">
      <h1 className="text-2xl font-bold text-center">Formulario</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="mt-5">
        <InputField
          label="Nombre"
          name="nombre"
          register={register}
          options={{ required: "El nombre es obligatorio" }}
          error={errors.nombre}
        />
        <InputField
          label="Correo electronico"
          name="email"
          type="email"
          register={register}
          options={{
            required: "El correo electrónico es obligatorio",
            pattern: {
              value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
              message: "El correo electrónico no es válido",
            },
          }}
          error={errors.correo_electronico}
        />
        <InputField
          label="Contraseña"
          name="contraseña"
          type="password"
          register={register}
          options={{
            required: "La contraseña es obligatoria",
            minLength: {
              value: 6,
              message: "La contraseña debe tener al menos 6 caracteres",
            },
          }}
          error={errors.contraseña}
        />
        <InputField
          label="Confirmar contraseña"
          name="confirmar_contraseña"
          type="password"
          register={register}
          options={{
            required: "Debes confirmar la contraseña",
            validate: (value) =>
              value === watch("contraseña") || "Las contraseñas no coinciden",
          }}
          error={errors.confirmar_contraseña}
        />
        <div className="max-w-md text-center">
          <a href="https://www.youtube.com" className="text-white">
            ¿Olvidaste tu contraseña?
          </a>
        </div>
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
