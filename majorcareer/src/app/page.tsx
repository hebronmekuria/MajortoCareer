import { Box,  ChakraProvider, Heading, HStack, Text, VStack } from "@chakra-ui/react";
import Image from "next/image";
import { JobCard } from "./components/JobCard";
import { DropDown } from "./components/DropDown";

export default function Home() {
  return (
    <ChakraProvider>
      <Heading m='30px'>
       Name of App
      </Heading>
      <DropDown></DropDown>
      <Box alignContent='middle'>
      <HStack spacing='30px'>
      <JobCard></JobCard>
      <JobCard></JobCard>
      <JobCard></JobCard>
      <JobCard></JobCard>
      </HStack>
      </Box>
      
    </ChakraProvider>
  );
}
