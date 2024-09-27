import { Image, useDisclosure, WrapItem } from '@chakra-ui/react'
import {
    Tr,
    Td,
  } from '@chakra-ui/react'
  import { Avatar, AvatarBadge, AvatarGroup } from '@chakra-ui/react'
  import {
    Modal,
    ModalOverlay,
    ModalContent,
    ModalHeader,
    ModalFooter,
    ModalBody,
    ModalCloseButton,
  } from '@chakra-ui/react'
export default function AppointmentRow({appointment,modalContexts}){
    const {onOpen,setSelectedAppointment} = modalContexts
    const {walker,start_time,end_time,appointment_notes,type,status} = appointment
    return(
        <>
        <Tr onClick={()=>{onOpen(),setSelectedAppointment(appointment)}} _hover={{cursor:'pointer',bg:'teal'}}>
            <Td display='flex' flexDirection='row' justifyContent='left' alignItems='center'>
                <Avatar className = "avatar-appointment" bgColor='teal.500' size='2xs' src={walker.user.photo_url}/>
                <div>{walker.user.firstname} {walker.user.lastname}</div>
            </Td>
            <Td>
                {new Date(start_time).toLocaleDateString('en-US',{weekday:'short',day:'numeric',month:'short'})}
            </Td>
            <Td>{new Date(start_time).getHours()}:{new Date(start_time).getMinutes()}</Td>
            <Td>{new Date(end_time).getHours()}:{new Date(end_time).getMinutes()}</Td>
        </Tr>
        </>
    )
}
