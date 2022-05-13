import { useEffect, useState } from "react";
import { Link } from "react-router-dom"
import axios from "axios"

export default function News(){
    const [data, setData] = useState([])

    useEffect(() => { GetNews() },[])

    function GetNews() {
        const url="http://127.0.0.1:8000/api/v1/news"
        axios.get(url).then((res) => {
            console.log(res)
            setData(res.data)
        }).catch((err) => {
            console.log(err)
        })
    }

    return (
        <>
        {data.map((item) => (
            <article key={item.id} >
                <img src={item?.news_details.news_image} alt='' id='featuredico'/>
                <h1>{item?.news_details?.title}</h1>
                <p>{item?.news_details?.content[0]}</p>
                <Link to={item.id}>Read Me</Link>
            </article>
        ))}
        </>
    )
}