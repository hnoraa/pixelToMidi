export default interface Octave {
    octaveNumber: number;
    midiNoteNumbers: number[];
    frequencyRange: { min: number; max: number; }
}