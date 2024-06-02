import React from "react";
import { Box, Text, Button, VStack, HStack } from "@chakra-ui/react";
import { StaticImageData } from "next/image";
import Image from "next/image";

interface JobCardProps {
  jobtitle: string;
  pay: string;
  skills: string;
  desc: string;
  more: string;
}
export function JobCard({
  jobtitle = "Software Engineer",
  pay = "$50/hour",
  skills = "lenovo, communication skills",
  desc = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor enim ad minim veniam, qrcitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ",
  more = "github.com",
}: JobCardProps) {
  return (
    <Box
      w="350px"
      h="500px"
      borderWidth="2px"
      borderColor="#239cc7"
      overflow="hidden"
      borderRadius="40"
      shadow="md"
      position="relative" // To position the text over the image
      mt="50px"
      border="gray.500"
      transition="transform 0.2s ease-out, shadow 0.2s ease-out"
      _hover={{
        transform: "scale(1.05)",
        shadow: "2xl",
      }}
    >
     
          <VStack align="left" ms='20px' mt='20px' me='20px'>
            <Text fontWeight="semibold" fontSize="20px" color="black">
              {jobtitle}
            </Text>
            <Text fontSize="20px" color="black">
            <Text fontWeight='semibold'>Pay:</Text> {pay}
            </Text>
            <Text fontSize="20px" color="black">
            <Text fontWeight='semibold'>Skills:</Text> {skills}
            </Text>
            <Text fontSize="20px" color="black">
              <Text fontWeight='semibold'>Job Description:</Text> {desc}
            </Text>
            <Button
              textColor="white"
              as="a"
              href={more}
              bg="#239cc7"
              borderRadius="3xl"
              w="94px"
              h="39px"
              target="_blank"
            >
              More
            </Button>
          </VStack>
      
    </Box>
  );
}
