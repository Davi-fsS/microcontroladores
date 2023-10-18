import "./style.css";

const Card = ({ children, index }) => {
    return <div className="card" key={index}>
        <div className="card-text">
            {children}
        </div>
    </div>
}

export default Card;
