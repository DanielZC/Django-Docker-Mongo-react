const Alert = ({ type = "text", text, title }) => (
  <div className="m-4">
    <p className="font-bold">{title}</p>
    <p className="text-red-50">{text}</p>
  </div>
);

export default Alert;
