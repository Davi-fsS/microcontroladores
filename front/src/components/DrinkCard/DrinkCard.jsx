import "./style.css";

const DrinkCard = ({ children, src, onClick }) => {
    return <button className="drink-card" onClick={onClick}>
        <img src={src} />
        {children}
    </button>
};

export default DrinkCard;
