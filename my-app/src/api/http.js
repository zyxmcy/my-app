import axios from 'axios'

export default function get(){
    return new Promise((resolve,reject)=>{
        axios
            .post('http://localhost:8080/dataVisualization/selectGoodsInfo')
            .then((res)=>{
                resolve(res)
            })
            .catch((err)=>{
                reject(err.data)
            })
    })
}

