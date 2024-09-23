import {useQuery,useMutation, useQueryClient} from '@tanstack/react-query'
import { getUser, userSignup } from '../../QueryHelpers/sessionQuery'
import { useEffect, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button } from '@chakra-ui/react'
export default function SignUp(){
    const queryClient = useQueryClient()
    const navigate = useNavigate()
    const [userName,setUsername] = useState('')
    const [firstName,setFirstName] = useState('')
    const [lastName,setLastName] = useState('')
    const [password,setPassword] = useState('')
    const [confirmedPassword,setConfirmedPassword] = useState('')
    const [email,setEmail] = useState('')
    const [formErr,setFormErr] = useState({})
    const [image,setImage] = useState('')
    const {data} = useQuery({queryKey:['user'],queryFn:getUser})

    useEffect(()=>{
        if (data?.user){
            console.log('entered')
            navigate('/profile')
        }
    },[data])
    const userMutation = useMutation({
        mutationFn: userSignup,
        onSuccess: ()=>{
            queryClient.invalidateQueries({queryKey:['user']})
            navigate('/profile')
        },
        onError:()=>{
            queryClient.invalidateQueries({queryKey:['user']})
        }
    })

    const handleFormSubmit = (e)=>{
        e.preventDefault()
        // userMutation.reset()
        console.log('entered submit')

        if (confirmedPassword !== password){
            let errObj = {}
            errObj.password = 'passwords not matching'
            console.log(errObj)
            setFormErr(errObj)
            return
        }
        // creating form data
        const formData = new FormData()
        console.log(userName,firstName,lastName,email)
        formData.append('username',userName)
        formData.append('first_name',firstName)
        formData.append('last_name',lastName)
        formData.append('email',email)
        formData.append('photo_url',image)
        formData.append('password',password)

        userMutation.mutate(formData)
        if(userMutation.isPending){
            console.log('pending')
        }
        if(userMutation.isError){
            setFormErr(userMutation.error.errObj)
        }
        if(userMutation.isSuccess){
            navigate('/profile')
        }
    }
    return(
        <div>
            {Object.keys(formErr).map(err=><div>{err}: {formErr[err]}</div>)}
            <form onSubmit={handleFormSubmit}>
                <input label = 'username' onChange={(e)=>setUsername(e.target.value)} placeholder='Username' required/>
                <input label = 'firstName' onChange={(e)=>setFirstName(e.target.value)} placeholder='First name' required/>
                <input label = 'lastName' onChange={(e)=>setLastName(e.target.value)} placeholder='Last name' required/>
                <input label = 'email' onChange={(e)=>setEmail(e.target.value)} placeholder='email' type='email' required/>
                <input label = 'password' onChange={(e)=>setPassword(e.target.value)} placeholder = 'password' required/>
                <input label = 'confirm' onChange={(e)=>setConfirmedPassword(e.target.value)} placeholder='confirm your password' required/>
                <input label = 'image' onChange={(e)=>setImage(e.target.value)} placeholder='Image url'/>
                <Button isLoading={userMutation.isPending} type='submit'>Submit</Button>
            </form>
        </div>
    )
}
