"use client";
import { Box,  ChakraProvider, Heading, HStack, Text, VStack } from "@chakra-ui/react";
import Image from "next/image";
import { JobCard } from "./components/JobCard";
import { DropDown } from "./components/DropDown";
import { useEffect, useState } from "react";

interface Job{
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
    fetch('http://127.0.0.1:5000/findjobs', {
      mode: 'no-cors',
    })
      .then(response => response.json())
      .then(data => {
        const jobsArray: Job[] = data.map((job: any[]) => ({
          url: job[0],
          jobtitle: job[1],
          major: job[2],
          location: job[3],
          pay: job[4],
          skills: job[5],
          desc: job[6]
        }));
        setJobs(jobsArray);
      })
      .catch(error => console.error('Error fetching jobs:', error));
  }, []);
  return (
    <ChakraProvider>
      <Heading m='30px'>
       Name of App
      </Heading>
      <DropDown></DropDown>
      <Box alignContent='middle'>
      <HStack spacing='30px'>
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
    </ChakraProvider>
  );
}
