import { useEffect, useState } from 'react'
import Octave from '../../models/octave';
import { Octaves } from '../../data/octaves';
import NoteDuration from '../../models/noteDuration';
import { NoteDurations } from '../../data/noteDurations';

interface Props {
    currentOctaveNumber: number;
    currentNoteDurationNumber: number;
}

export default function Information({ currentOctaveNumber, currentNoteDurationNumber }: Props) {
    const [currentOctave, setCurrentOctave] = useState<Octave>();
    const [currentNoteDuration, setNoteDuration] = useState<NoteDuration>();

    useEffect(() => {
        let octave = Octaves.find(o => o.octaveNumber === currentOctaveNumber);
        setCurrentOctave(octave);
    }, [currentOctaveNumber]);

    useEffect(() => {
        let noteDuration = NoteDurations[currentNoteDurationNumber];
        setNoteDuration(noteDuration);
    }, [currentNoteDurationNumber]);
    return (
        <div>
            <div>
                <span>Current Octave: {currentOctave?.octaveNumber}</span>

                <span>Range: {currentOctave?.frequencyRange?.min}Hz - {currentOctave?.frequencyRange?.max}Hz</span>
            </div>
            <div>
                <span>Current Note Duration: {currentNoteDuration?.friendly} ({currentNoteDuration?.fraction})</span>
            </div>
        </div>
    )
}
