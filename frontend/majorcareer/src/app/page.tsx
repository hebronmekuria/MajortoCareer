"use client";
import React from "react";
import { Box, ChakraProvider, Heading, Text, HStack, VStack } from "@chakra-ui/react";
import { JobCard } from "./components/JobCard";
import { DropDown } from "./components/DropDown";
import { useEffect, useState } from "react";
import "./styles.css";
import Image from "next/image";
import logo from './static/investigate.png'


interface Job {
  jobtitle: string;
  pay: string;
  location: string;
  skills: string;
  desc: string;
  url: string;
}

export default function Home() {
  const [jobs, setJobs] = useState<Job[]>([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/findjobs')
      .then(response => response.json())
      .then(data => {
        const jobsArray: Job[] = data.map((job: any) => ({
          url: job.url,
          jobtitle: job.jobtitle,
          major: job.major,
          location: job.location,
          pay: job.pay,
          skills: job.skills,
          desc: job.desc
        }));
        setJobs(jobsArray);
      })
      .catch(error => console.error('Error fetching jobs:', error));
  }, []);

  return (
    <ChakraProvider>
      <Box w='100%' h='100vh' display='flex' flexDirection='column' alignItems='center' mt='10px'>
        <Box mt='0px' mb='10px'>
          <Image
            className="mt-20 w-[300px] h-[300px]"
            src={logo}
            alt="logo"
          />
        </Box>
        <VStack spacing='12px' align='center' mb='20px'>
          <Heading>Name of App</Heading>
          <Text width='1000px' overflowWrap='normal' fontSize='20px'>Bacon ipsum dolor amet short ribs brisket venison rump drumstick pig sausage prosciutto chicken spare ribs salami picanha doner. Kevin capicola sausage, buffalo bresaola venison turkey shoulder picanha ham pork tri-tip meatball meatloaf ribeye. Doner spare ribs andouille bacon sausage. Ground round jerky brisket pastrami shank.</Text>
        </VStack>
        <DropDown />
        <Box w='80%' overflowX='auto' className='no-scrollbar'>
          <HStack spacing='30px' w='max-content' h='auto'>
            {jobs.map((job) => (
              <JobCard
                key={job.url}
                jobtitle={job.jobtitle}
                pay={job.pay}
                location={job.location}
                skills={job.skills}
                desc={job.desc}
                url={job.url}
              />
            ))}
          </HStack>
        </Box>
      </Box>
    </ChakraProvider>
  );
}
