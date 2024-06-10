import React from "react";
import { Select } from "@chakra-ui/react";

export function DropDown() {
    const collegeMajors = [
        'Accounting', 'Actuarial Science', 'Advertising', 'Aerospace Engineering', 'Aeronautical Engineering',
        'African American Studies', 'Agricultural Engineering', 'Agriculture', 'American Sign Language', 'American Studies',
        'Animal Science', 'Anthropology', 'Apparel Design', 'Applied Mathematics', 'Aquatic Biology',
        'Archaeology', 'Architecture', 'Art Education', 'Art History', 'Asian Studies',
        'Astronomy', 'Biochemistry', 'Bioengineering', 'Biology', 'Biomedical Engineering',
        'Biophysics', 'Biotechnology', 'Business Administration', 'Business Analytics', 'Chemical Engineering',
        'Chemical Physics', 'Chemistry', 'Child Development', 'Chinese Language and Literature', 'Civil Engineering',
        'Classical Studies', 'Clinical Psychology', 'Cognitive Science', 'Communication', 'Communications Disorders',
        'Comparative Literature', 'Computer Engineering', 'Computer Science', 'Construction Engineering', 'Construction Management',
        'Counseling', 'Creative Arts', 'Creative Writing', 'Criminal Justice', 'Criminology',
        'Culinary Arts', 'Cybersecurity', 'Dance', 'Data Science', 'Dental Hygiene',
        'Dietetics', 'Digital Media', 'Dramatic Arts', 'Early Childhood Education', 'Earth and Space Science',
        'Earth Science', 'Ecology', 'Economics', 'Education', 'Educational Leadership',
        'Electrical Engineering', 'Elementary Education', 'Engineering', 'Engineering Physics', 'Engineering Technology',
        'English', 'Entomology', 'Environmental Engineering', 'Environmental Health', 'Environmental Science',
        'Epidemiology', 'Equine Studies', 'Ethnic Studies', 'Ethnomusicology', 'European Studies',
        'Exercise Science', 'Family Studies', 'Fashion Design', 'Fashion Merchandising', 'Film and Television',
        'Film Studies', 'Finance', 'Financial Planning', 'Fine Arts', 'Fire Science',
        'Fisheries and Wildlife', 'Food Science', 'Forensic Science', 'Forestry', 'French Language and Literature',
        'Game Design', 'Genetics', 'Geography', 'Geology', 'Geospatial Science',
        'German Language and Literature', 'Graphic Design', 'Health Administration', 'Health Education', 'Health Information Management',
        'Health Sciences', 'Historic Preservation', 'History', 'Horticulture', 'Hospitality Management',
        'Human Biology', 'Human Development', 'Human Resources', 'Human Services', 'Industrial Design',
        'Industrial Engineering', 'Information Science', 'Information Technology', 'Integrated Marketing Communications', 'Interior Design',
        'International Business', 'International Relations', 'Italian Language and Literature', 'Japanese Language and Literature', 'Jewish Studies',
        'Journalism', 'Kinesiology', 'Landscape Architecture', 'Landscape Design', 'Latin American Studies',
        'Law Enforcement', 'Legal Studies', 'Liberal Arts', 'Library Science', 'Linguistics',
        'Management', 'Manufacturing Engineering', 'Marketing', 'Marine Biology', 'Materials Science',
        'Mathematical Economics', 'Mathematics', 'Mechanical Engineering', 'Media Production', 'Media Studies',
        'Medical Laboratory Science', 'Microbiology', 'Middle Eastern Studies', 'Military Science', 'Molecular Biology',
        'Music', 'Music Education', 'Music Performance', 'Museum Studies', 'Nanotechnology',
        'Neuroscience', 'Nuclear Engineering', 'Nursing', 'Nutrition', 'Occupational Health',
        'Occupational Therapy', 'Oceanography', 'Operations Management', 'Optometry', 'Organizational Leadership',
        'Paleontology', 'Parks and Recreation', 'Pharmaceutical Sciences', 'Pharmacy', 'Philosophy',
        'Photography', 'Physical Education', 'Physical Therapy', 'Physics', 'Plant Science',
        'Political Science', 'Pre-Dentistry', 'Pre-Law', 'Pre-Medicine', 'Pre-Veterinary Medicine',
        'Psychology', 'Public Administration', 'Public Health', 'Public Policy', 'Public Relations',
        'Radio and Television', 'Radiologic Technology', 'Real Estate', 'Recreation and Leisure Studies', 'Religious Studies',
        'Renewable Energy', 'Respiratory Therapy', 'Robotics', 'Russian Language and Literature', 'Science Education',
        'Social and Behavioral Sciences', 'Social Work', 'Sociology', 'Software Engineering', 'Soil Science',
        'Spanish Language and Literature', 'Special Education', 'Speech Pathology', 'Sport Management', 'Statistics',
        'Supply Chain Management', 'Sustainable Agriculture', 'Systems Engineering', 'Telecommunications', 'Theatre',
        'Theology', 'Therapeutic Recreation', 'Toxicology', 'Transportation and Logistics', 'Urban Planning',
        'Veterinary Medicine', 'Veterinary Technology', 'Video Game Design', 'Visual Arts', 'Viticulture and Enology',
        'Water Resources', 'Wildlife Biology', 'Wildlife Management', 'Women’s Studies', 'Zoology'
    ];
    
    return (
        <Select
            placeholder='Select Major'
            width='350px'
            borderWidth="2px"
            borderColor="#239cc7"
            overflow="hidden"
            border="gray.500"
            borderRadius="20"
            position="relative"
            shadow="md"
            fontSize='20px'
            textAlign='center' 
        >
            {collegeMajors.map((option, index) => (
                <option key={index} value={option}>
                    {option}
                </option>
            ))}
        </Select>
    );
}
