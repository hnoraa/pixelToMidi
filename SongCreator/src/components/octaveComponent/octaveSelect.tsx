import { useState } from 'react';
import { Octaves } from '../../data/octaves';

interface Props {
    currentOctave: number;
    onOctaveChange: any;
}

export default function OctaveSelect({ currentOctave, onOctaveChange }: Props) {
    const handleOctaveChange = (e: any) => {
        const selectedOctave = parseInt(e.target.value);
        onOctaveChange(selectedOctave);
    };

    return (
        <div>
            <label htmlFor="octave-select">Select Octave:</label>
            <select id="octave-select" value={currentOctave} onChange={handleOctaveChange}>
                {Octaves.map((octave) => (
                    <option key={octave.octaveNumber} value={octave.octaveNumber}>
                        Octave {octave.octaveNumber}
                    </option>
                ))}
            </select>
        </div>
    );
}
