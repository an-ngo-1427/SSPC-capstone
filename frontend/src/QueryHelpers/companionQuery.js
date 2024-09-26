import { MyError } from "./sessionQuery"

export async function getCompanions(){
    const response = await fetch('api/companions/')
    const data = await response.json()
    console.log('this is data',data)
    if(response.ok){
        return data
    }else{
        throw new MyError(data)
    }
}
