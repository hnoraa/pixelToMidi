import './pixelGrid.css';
import { useState, useEffect, useRef } from 'react';
import { NoteDurations } from '../../data/noteDurations';

interface Props {
    height: number;
    width: number;
    currentNote?: string;
    currentOctave?: number;
    currentMidiNumber?: number;
    currentNoteDuration?: number;
    currentVelocity?: number;
    keyPressId?: number;
    onCellSelect?: (cellIndex: number) => void;
    onGridDataChange?: (gridData: Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>) => void;
    gridData?: Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>;
};

export default function PixelGrid({ height, width, currentNote, currentOctave, currentMidiNumber, currentNoteDuration, currentVelocity, keyPressId, onCellSelect, onGridDataChange, gridData }: Props) {
    const [clickedCell, setClickedCell] = useState<number>(0);
    const [cellNotes, setCellNotes] = useState<Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>>(new Map());
    const previousKeyPressIdRef = useRef<number>(-1);

    // Sync internal cell notes when parent provides gridData (e.g. Fill action)
    useEffect(() => {
        if (gridData) {
            setCellNotes(new Map(gridData));
        }
    }, [gridData]);

    const handleClick = (i: number) => {
        setClickedCell(i);
        if (onCellSelect) {
            onCellSelect(i);
        }
    };

    // Update cell note when keyPressId changes (new key is clicked)
    useEffect(() => {
        if (currentNote && currentOctave !== undefined && currentMidiNumber !== undefined && currentNoteDuration !== undefined && currentVelocity !== undefined && keyPressId !== undefined && keyPressId !== previousKeyPressIdRef.current) {
            previousKeyPressIdRef.current = keyPressId;
            setCellNotes(prevCellNotes => {
                const newCellNotes = new Map(prevCellNotes);
                newCellNotes.set(clickedCell, { note: currentNote, octave: currentOctave, midiNumber: currentMidiNumber, duration: currentNoteDuration, velocity: currentVelocity });
                if (onGridDataChange) {
                    onGridDataChange(newCellNotes);
                }
                return newCellNotes;
            });
        }
    }, [keyPressId, clickedCell, currentNote, currentOctave, currentMidiNumber, currentNoteDuration, currentVelocity, onGridDataChange]);

    let gridItems: JSX.Element[] = [];
    for (let i = 0; i < height; i++) {
        for (let j = 0; j < width; j++) {
            const cellIndex = i * width + j;
            const cellNote = cellNotes.get(cellIndex);
            const isSelected = clickedCell === cellIndex;
            
            // Calculate background color: R=midiNumber, G=duration scaled to 0-255, B=100
            let backgroundColor = 'white';
            if (cellNote && !isSelected) {
                const r = Math.min(cellNote.midiNumber, 255);
                const g = Math.round((cellNote.duration / 9) * 255); // Scale 0-9 to 0-255
                const b = 100;
                backgroundColor = `rgb(${r}, ${g}, ${b})`;
            }
            
            gridItems.push(
                <div
                    key={cellIndex}
                    className={`grid-cell ${isSelected ? 'clicked' : ''}`}
                    style={{ backgroundColor }}
                    onClick={() => {
                        handleClick(cellIndex);
                    }}
                >
                    {cellNote && (
                        <div className="cell-content">
                            <div>{cellNote.note}</div>
                            <div style={{ fontSize: '0.6em', display: 'flex', gap: '4px', justifyContent: 'center' }}>
                                <span>{cellNote.midiNumber}</span>
                                <span>{NoteDurations[cellNote.duration]?.short || cellNote.duration}</span>
                                {cellNote.velocity !== undefined && (
                                    <span>V{cellNote.velocity}</span>
                                )}
                            </div>
                        </div>
                    )}
                </div>
            );
        }
    }

    return (
        <div id="pixelGridContainer" style={{
            display: 'grid',
            gridTemplateColumns: '1fr',
            gridTemplateRows: '1fr',
            width: '100%',
            height: '100%',
        }}>
            <div 
                id="scrollWrapper"
                style={{
                    overflow: 'auto',
                    boxSizing: 'border-box',
                }}
            >
                <div 
                    id="gridArea"
                    style={{
                        display: 'grid',
                        gridTemplateColumns: `repeat(${width}, 40px)`,
                        gridTemplateRows: `repeat(${height}, 40px)`,
                        width: 'fit-content',
                        height: 'fit-content',
                        border: '3px solid black',
                    } as React.CSSProperties}
                >
                    {gridItems}
                </div>
            </div>
        </div>
    )
}
