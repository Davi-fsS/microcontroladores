import { useEffect, useState } from "react";
import Button from "../components/Button/Button";
import Card from "../components/Card/Card";
import DrinkCard from "../components/DrinkCard/DrinkCard";
import { getAllDrinks, getDetailById } from "../services/drinkServices";
import "./style.css";

const Flow = () => {

    const getAllByIdMock = [
        {
            id: 1,
            name: "Fanta + Coca",
            price: 20.0,
            imgUrl: "https://p2.trrsf.com/image/fget/cf/1200/1200/middle/images.terra.com/2013/11/30/cocacoaacucar.jpg",
            description: "Uma bebida muito saborosa, lembra dos odores da Malásia, algo tropical.",
            doseA: "Fanta",
            qtdA: 2,
            doseB: "Coca",
            qtdB: 2
        },
        {
            id: 2,
            name: "Guaraná + Fanta",
            price: 20.0,
            imgUrl: "https://p2.trrsf.com/image/fget/cf/1200/1200/middle/images.terra.com/2013/11/30/cocacoaacucar.jpg",
            description: "Uma bebida muito saborosa, lembra dos odores da Jamaica, algo tropical.",
            doseA: "Guaraná",
            qtdA: 2,
            doseB: "Fanta",
            qtdB: 2
        },
        {
            id: 3,
            name: "Coca",
            price: 10.0,
            imgUrl: "https://p2.trrsf.com/image/fget/cf/1200/1200/middle/images.terra.com/2013/11/30/cocacoaacucar.jpg",
            description: "Uma bebida muito saborosa, lembra dos odores da Sibéria, algo tropical.",
            doseA: "Coca",
            qtdA: 2,
            doseB: "Coca",
            qtdB: 2
        }
    ]

    const [drinks, setDrinks] = useState([]);
    const [drinkDetail, setDrinkDetail] = useState(null);

    const [isCardRead, setIsCardRead] = useState(false);
    const [isSystemStarted, setIsSystemStarted] = useState(false);
    const [isOpenDetail, setIsOpenDetail] = useState(false);

    const [onlyOneDrink, setOnlyOneDrink] = useState(false);

    const [qtdDoseA, setQtdDoseA] = useState(null);
    const [qtdDoseB, setQtdDoseB] = useState(null);

    const [addDoseA, setAddDoseA] = useState(false);
    const [addDoseB, setAddDoseB] = useState(false);
    const [lessDoseA, setLessDoseA] = useState(false);
    const [lessDoseB, setLessDoseB] = useState(false);

    const [orderConfirmation, setOrderConfirmation] = useState(false);

    const [doingDrink, setDoingDrink] = useState(false);

    const [error, setError] = useState(false);
    const [errorMessage, setErrorMessage] = useState(null);

    useEffect(() => {

        setTimeout(() => {
            setIsCardRead(true);
        }, 4000);

    }, [isCardRead]);

    const initializingSystem = async () => {
        setIsSystemStarted(true);

        const listDrinks = await getAllDrinks();
        setDrinks(listDrinks);
    };

    const handleOpenDetail = async (id) => {
        // const getDetailById = getAllByIdMock.filter(value => value.id === id);
        const drinkDetails = await getDetailById(id);
        setIsOpenDetail(true);
        setDrinkDetail(drinkDetails);
        setQtdDoseA(drinkDetails[0]?.qty_A);
        setQtdDoseB(drinkDetails[0]?.qty_B);

        if (drinkDetails[0]?.dose_A === drinkDetails[0]?.dose_B) {
            setOnlyOneDrink(true);
        }
        else {
            setOnlyOneDrink(false);
        }
    };

    useEffect(() => {
        if (qtdDoseB > 1 && qtdDoseA > 1) {
            if (addDoseA) {
                setQtdDoseA(qtdDoseA + 1);
                setQtdDoseB(qtdDoseB - 1);

            }
            if (addDoseB) {
                setQtdDoseB(qtdDoseB + 1);
                setQtdDoseA(qtdDoseA - 1);

            }
            if (lessDoseA) {
                setQtdDoseA(qtdDoseA - 1);
                setQtdDoseB(qtdDoseB + 1);
            }
            if (lessDoseB) {
                setQtdDoseB(qtdDoseB - 1);
                setQtdDoseA(qtdDoseA + 1);
            }
        }
        else if (qtdDoseA === 1) {
            if (addDoseA) {
                setQtdDoseA(qtdDoseA + 1);
                setQtdDoseB(qtdDoseB - 1);
            }
            if (lessDoseB) {
                setQtdDoseB(qtdDoseB - 1);
                setQtdDoseA(qtdDoseA + 1);
            }
        }
        else if (qtdDoseB === 1) {
            if (addDoseB) {
                setQtdDoseB(qtdDoseB + 1);
                setQtdDoseA(qtdDoseA - 1);
            }
            if (lessDoseA) {
                setQtdDoseA(qtdDoseA - 1);
                setQtdDoseB(qtdDoseB + 1);
            }
        }

        setAddDoseA(false);
        setAddDoseB(false);
        setLessDoseA(false);
        setLessDoseB(false);
    }, [addDoseA, addDoseB, lessDoseA, lessDoseB, qtdDoseA, qtdDoseB]);

    const backToDrinksPage = () => {
        setIsOpenDetail(false);
        setDrinkDetail(null);
    };

    const makeOrder = async () => {
        setDoingDrink(true);

        setTimeout(() => {
            setDoingDrink(false);
        }, 3000);
        //chamar api para chamada

        // setError(true);
        // setErrorMessage("Não possuímos doses suficientes de (bebida).")
        setOrderConfirmation(true);
    };

    const goToMenu = () => {
        setOrderConfirmation(false);
        setIsOpenDetail(false);
    };

    const leave = () => {
        setOrderConfirmation(false);
        setIsOpenDetail(false);
        setIsSystemStarted(false);
        setIsCardRead(false);
    };

    return <div className="position">
        {
            !isCardRead ?
                <Card>
                    <h2>Bem vindo ao Drinker</h2>
                    <i>Aproxime o seu cartão</i>
                </Card>
                :
                !isSystemStarted ?
                    <Card>
                        <h2>Bem vindo ao Drinker</h2>
                        <i>Gabriel</i>
                        <Button onClick={initializingSystem}>
                            Vamos começar?
                        </Button>
                    </Card>
                    :
                    !isOpenDetail ?
                        drinks.map((value) => {
                            return <DrinkCard src={value.img_url} onClick={() => handleOpenDetail(value.id)}>
                                <p>{value.name}</p>
                                <p>R$ {value.price}</p>
                            </DrinkCard>
                        })
                        :
                        !orderConfirmation ?
                            drinkDetail.map((value, index) => {
                                return <Card key={index}>
                                    <h2>{value.name}</h2>
                                    <i>{value.description}</i>
                                    <p>R$ {value.price}</p>
                                    <div>
                                        {
                                            !onlyOneDrink && <>
                                                <p>Escolha a proporção de doses na sua bebida</p>
                                                <div className="dose-content">
                                                    <div className="dose-field">
                                                        <button className="doses-button" onClick={() => setLessDoseA(true)}>-</button>
                                                        <p>{qtdDoseA}</p>
                                                        <button className="doses-button" onClick={() => setAddDoseA(true)}>+</button>
                                                    </div>
                                                    <p>{value.dose_A}</p>
                                                </div>

                                                <div className="dose-content">
                                                    <div className="dose-field">
                                                        <button className="doses-button" onClick={() => setLessDoseB(true)}>-</button>
                                                        <p>{qtdDoseB}</p>
                                                        <button className="doses-button" onClick={() => setAddDoseB(true)}>+</button>
                                                    </div>
                                                    <p>{value.dose_B}</p>
                                                </div>
                                            </>
                                        }

                                    </div>
                                    <div className="buttons">
                                        <Button color="white" onClick={backToDrinksPage}>Voltar</Button>
                                        <Button onClick={makeOrder}>Pedir</Button>
                                    </div>
                                </Card>
                            })
                            :
                            doingDrink ?
                                error ?
                                    <Card>
                                        <h1>{errorMessage}</h1>
                                        <Button onClick={goToMenu}>Voltar</Button>
                                    </Card>
                                    :
                                    <Card>
                                        <h2>Preparando sua bebida, aguarde alguns instantes</h2>

                                        <span>adicionar animacao aqui</span>
                                    </Card>
                                : <Card>
                                    <h2>Bebida finalizada</h2>
                                    <h3>Aproveite seu drink!</h3>
                                    <h3>Tire sua foto e nos marque no instagram: @rubio</h3>

                                    <div className="buttons">
                                        <Button color="white" onClick={leave}>Sair</Button>
                                        <Button onClick={goToMenu}>Continuar</Button>
                                    </div>
                                </Card>
        }

    </div>
};

export default Flow;
