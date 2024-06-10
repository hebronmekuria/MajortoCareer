"use client";
import { Box, ChakraProvider, Heading, HStack } from "@chakra-ui/react";
import { JobCard } from "./components/JobCard";
import { DropDown } from "./components/DropDown";
import { useEffect, useState } from "react";

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
      <Box w='100%' h='100%'>
        <Heading m='30px'>Name of App</Heading>
        <DropDown />
        <Box overflowX="auto" maxWidth="100%" p="4">
          <HStack spacing='30px' minWidth="1600px" maxWidth="fit-content">
            {jobs.slice(0, 4).map((job) => (
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
