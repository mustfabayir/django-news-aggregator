import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import axios from "axios"

export default function NewsDetails(){
    const [data,setData]=useState([])
    const { urlparams } = useParams()

    useEffect(() => { GetDetail() },[])
    function GetDetail() {
        const url = `http://127.0.0.1:8000/api/v1/news/${urlparams.id}`
        axios.get(url).then((response) => {
            console.log(response)
            setData(response.data)
        }).catch((error) => {
            console.log(error)
        })
    }



    return(
        <>
        <article class='singlepage' id='featured'>
            <h1>{data?.news_details?.title}</h1>
            <img class='headerpic' src={data?.news_details?.news_image} alt='' id='featuredico'/>

            <p>{data?.news_details.content[0]}</p>
        </article>
        </>
    );


}