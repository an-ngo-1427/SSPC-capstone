import { useQuery,useMutation, useQueryClient } from "@tanstack/react-query"
import { useEffect, useState } from "react"
import { getUser, userLogin } from "../../QueryHelpers/sessionQuery"
import { useNavigate } from "react-router-dom"
import { Button } from '@chakra-ui/react'

export default function LogInPage(){
    const [username,setUsername] = useState('')
    const [password,setPassword] = useState('')
    const [formErr,setFormErr] = useState({})
    const queryClient = useQueryClient()
    const navigate = useNavigate()
    const {data} = useQuery({queryKey:['user'],queryFn:getUser})
    const user = data?.user

    const userMutation = useMutation({
        mutationFn:userLogin,
        onSuccess:()=>{
            queryClient.invalidateQueries({queryKey:['user']})
            navigate('/')
        }
    })

    useEffect(()=>{
        console.log('user',data)
        if (user){
            navigate('/')
        }
    },[data])

    const handleFormSubmit = (e)=>{

        e.preventDefault()
        const formData = new FormData()
        formData.append('username',username)
        formData.append('password',password)
        userMutation.mutate(formData)

        if(userMutation.isError) setFormErr(userMutation.error.errObj)
        if(userMutation.isSuccess) navigate('/')
    }

    return(
        <div>
            {formErr && Object.keys(formErr).map(ele=><div>{ele} : {formErr[ele]}</div>)}
            <form onSubmit={handleFormSubmit}>
                <input onChange={(e)=>setUsername(e.target.value)}label='username' placeholder="username" required></input>
                <input onChange={(e)=>setPassword(e.target.value)}label='password' placeholder="password" required></input>
                <Button isLoading={userMutation.isPending} type='submit'>Submit</Button>
            </form>
        </div>
    )
}
