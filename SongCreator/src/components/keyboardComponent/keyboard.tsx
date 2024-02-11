import { Col, Row } from "reactstrap";
import './keyboard.css';
import { useState, useEffect } from "react";
import Octave from '../../models/octave';
import { Octaves } from '../../data/octaves';

interface Props {
    currentOctaveNumber: number;
}

export default function Keyboard({currentOctaveNumber} : Props) {
    const keys = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'];
    const [pressedKeys, setPressedKeys] = useState<string[]>([]);
    const [currentOctave, setCurrentOctave] = useState<Octave>();

    useEffect(() => {
        let octave = Octaves.find(o => o.octaveNumber === currentOctaveNumber);
        setCurrentOctave(octave);
    }, [currentOctaveNumber]);

    const handleKeyPress = (key: string) => {
        setPressedKeys((prevKeys) => [...prevKeys, key]);
    };

    const handleKeyRelease = (key: string) => {
        setPressedKeys((prevKeys) => prevKeys.filter((k) => k ! == key));
    };

    return (
        <Row>
            <Col md="12">
                <Row id="board">
                {keys.map((key: string, index: number) => (
                    <Col 
                        md="1" 
                        key={index} 
                        className={`key ${pressedKeys.includes(key) ? 'pressed' : ''} ${key.includes('#') ? 'black' : 'white'}`}
                        onMouseDown={() => handleKeyPress(key)}
                        onMouseUp={() => handleKeyRelease(key)}
                        >
                        {key}<br />{currentOctave?.midiNoteNumbers[index]}
                    </Col>
                ))}
                </Row>
            </Col>
        </Row>
    );
}
