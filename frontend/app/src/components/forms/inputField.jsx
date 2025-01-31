const InputField = ({
  label,
  name,
  register,
  type = "text",
  value,
  onChange,
  error,
}) => (
  <div className="mb-4">
    <label htmlFor={name} className="block text-sm font-medium text-white">
      {label}
    </label>
    <input
      id={name}
      name={name}
      type={type}
      value={value}
      {...register(name)}
      onChange={onChange}
      placeholder={label}
      className={`mt-1 block w-full bg-gray-900 p-1 text-white border-b-2 border-blue-500 shadow-md sm:text-sm md:text-md ${
        error ? "border-red-500" : ""
      }`}
    />
    {error && <p className="mt-1 text-sm text-red-600">{error}</p>}
  </div>
);

export default InputField;
