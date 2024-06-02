import React from "react";
import { Select } from "@chakra-ui/react"
export function DropDown() {
    return (
        <Select placeholder='Select Major'>
            <option value='option1'>Option 1</option>
            <option value='option2'>Option 2</option>
            <option value='option3'>Option 3</option>
        </Select>
    );
}
