import { Box, HStack, ChakraProvider } from "@chakra-ui/react";
import Image from "next/image";
import { JobCard } from "./components/JobCard";

export default function Home() {
  return (
    <ChakraProvider>
      <Box alignContent='middle'>
      <HStack spacing='30px'>
      <JobCard header={""} subtitle={""} code={""}></JobCard>
      <JobCard header={""} subtitle={""} code={""}></JobCard>
      <JobCard header={""} subtitle={""} code={""}></JobCard>
      <JobCard header={""} subtitle={""} code={""}></JobCard>
      </HStack>
      </Box>
    </ChakraProvider>
  );
}
