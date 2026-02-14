import { useEffect, useState } from 'react'
import Octave from '../../models/octave';
import { Octaves } from '../../data/octaves';
import NoteDuration from '../../models/noteDuration';
import { NoteDurations } from '../../data/noteDurations';

interface Props {
    currentOctaveNumber: number;
    currentNoteDurationNumber: number;
    gridHeight: number;
    gridWidth: number;
}

export default function Information({ currentOctaveNumber, currentNoteDurationNumber, gridHeight, gridWidth }: Props) {
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
        <table style={{ borderCollapse: 'collapse', width: '100%' }}>
            <tbody>
                <tr>
                    <td>Current Octave: {currentOctave?.octaveNumber}</td>
                </tr>
                <tr>
                    <td>Range: {currentOctave?.frequencyRange?.min}Hz - {currentOctave?.frequencyRange?.max}Hz</td>
                </tr>
                <tr>
                    <td>Current Note Duration: {currentNoteDuration?.friendly} ({currentNoteDuration?.fraction})</td>
                </tr>
                <tr>
                    <td>Grid Size: {gridWidth} x {gridHeight}</td>
                </tr>
            </tbody>
        </table>
    )
}
