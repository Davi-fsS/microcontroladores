import "./style.css";

const Button = ({ onClick, children, color }) => {
    return <button onClick={onClick} className="button" style={color === "white" ? { background: "#fff", border: "2px solid #FC9B08", color: "#FC9B08" } : null}>
        {children}
    </button>
};

export default Button;
