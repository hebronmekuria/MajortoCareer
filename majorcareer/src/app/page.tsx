import { Box, HStack, ChakraProvider } from "@chakra-ui/react";
import Image from "next/image";
import { JobCard } from "./components/JobCard";
import { DropDown } from "./components/DropDown";

export default function Home() {
  return (
    <ChakraProvider>
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
