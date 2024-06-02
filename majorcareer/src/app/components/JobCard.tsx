import React from "react";
import { Box, Text, Button, VStack, HStack } from "@chakra-ui/react";
import { StaticImageData } from "next/image";
import Image from "next/image";

interface JobCardProps {
  header: string;
  subtitle: string;
  code: string
}
export function JobCard({
  header = 'Professor Gemini',
  subtitle = 'AI Grader that efficiently grades any open-ended assignments, essays, and homework.',
  code ='github.com'
}: JobCardProps) {
  return (
    <Box
      w="350px"
      h="500px"
      borderWidth="2px"
      borderColor='#239cc7'
      overflow='hidden'
      borderRadius="40"
      shadow="md"
      position="relative"  // To position the text over the image
      mt="50px"
      border="gray.500"
      transition="transform 0.2s ease-out, shadow 0.2s ease-out"
      _hover={{
        transform: "scale(1.05)",
        shadow: "2xl",
      }}
    >
      
      <VStack mt="200px">
        <HStack>
          <VStack ms="20px" align="left" >
            <Box background='white' zIndex={3} opacity='0.6'>
            <Text
              fontWeight="semibold"
              fontSize="20px"
              color="black"
            >
              {header}
            </Text>
            <Text
              fontSize="20px"
              fontWeight="semibold"
              color="black"
            >
              {subtitle}
            </Text>
            </Box>
          </VStack>
          <VStack>
            <Button mt='200px'
              textColor="white"
              as="a"
              href={code}
              bg="#239cc7"
              borderRadius="3xl"
              w="94px"
              h="39px"
              target="_blank" 
            >
              Code
            </Button>
          </VStack>
        </HStack>
      </VStack>
    </Box>
  );
}
