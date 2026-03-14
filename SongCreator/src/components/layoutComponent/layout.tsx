import { useState } from 'react';
import { Container, Row, Col, Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, NavLink } from 'reactstrap';
import Keyboard from '../keyboardComponent/keyboard';
import './layout.css';
import PixelGrid from '../pixelGridComponent/pixelGrid';
import SongInfo from '../songInfoComponent/songInfo';
import ConfigComponent from '../configComponent/configComponent';
import Song from '../../models/song';

export default function Layout() {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const toggle = () => setIsOpen(!isOpen);
  const [currentOctave, setCurrentOctave] = useState(4); // middle c default
  const [currentNoteDuration, setCurrentNoteDuration] = useState(2); // whole note default
  const [currentVelocity, setCurrentVelocity] = useState(127); // max velocity default
  const [gridHeight, setGridHeight] = useState(16); // default 16x16
  const [gridWidth, setGridWidth] = useState(16); // default 16x16
  const [selectedNote, setSelectedNote] = useState<string>('');
  const [selectedOctave, setSelectedOctave] = useState<number | undefined>(undefined);
  const [selectedMidiNumber, setSelectedMidiNumber] = useState<number | undefined>(undefined);
  const [selectedCellIndex, setSelectedCellIndex] = useState<number>(0);
  const [keyPressId, setKeyPressId] = useState<number>(0);
  const [gridData, setGridData] = useState<Map<number, { note: string; octave: number; midiNumber: number; duration: number; velocity?: number }>>(new Map());
  const [song, setSong] = useState<Song>({
    song: 'New Song',
    tempo: 120,
    outputFilename: 'song.midi',
    size: 16,
    tracks: []
  });

  const handleOctaveChange = (octave: number) => {
    setCurrentOctave(octave);
  };

  const handleNoteDurationChange = (noteDuration: number) => {
    setCurrentNoteDuration(noteDuration);
  };

  const handleVelocityChange = (velocity: number) => {
    setCurrentVelocity(velocity);
  };

  const handleGridSizeChange = (width: number, height: number) => {
    setGridWidth(width);
    setGridHeight(height);
    setSong(prevSong => ({
      ...prevSong,
      size: width
    }));
  };

  const handleKeyClick = (note: string, octave: number, midiNumber: number) => {
    setSelectedNote(note);
    setSelectedOctave(octave);
    setSelectedMidiNumber(midiNumber);
    setKeyPressId(prev => prev + 1);
  };

  const handleCellSelect = (cellIndex: number) => {
    setSelectedCellIndex(cellIndex);
  };

  return (
    <Container fluid>
      <Navbar className="navbar fixed-top navbar-light bg-light" fluid>
        <NavbarBrand href="/" className="mb-0 h1">Song Creator</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="me-auto" navbar>
            <NavItem>
              <NavLink href="/instructions">Instructions</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/create">Create a Song</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
      <Row id="canvasArea">
        <Col md="2">
          <SongInfo song={song} gridHeight={gridHeight} gridWidth={gridWidth} />
        </Col>
        <Col md="8">
          <PixelGrid 
            height={gridHeight} 
            width={gridWidth}
            gridData={gridData}
            currentNote={selectedNote}
            currentOctave={selectedOctave}
            currentMidiNumber={selectedMidiNumber}
            currentNoteDuration={currentNoteDuration}
            currentVelocity={currentVelocity}
            keyPressId={keyPressId}
            onCellSelect={handleCellSelect}
            onGridDataChange={setGridData}
          />
        </Col>
        <Col md="2">
          <ConfigComponent 
            currentOctave={currentOctave} 
            onOctaveChange={handleOctaveChange}
            currentNoteDuration={currentNoteDuration}
            onNoteDurationChange={handleNoteDurationChange}
            currentVelocity={currentVelocity}
            onVelocityChange={handleVelocityChange}
            onGridSizeChange={handleGridSizeChange}
            song={song}
            gridData={gridData}
            onGridDataChange={setGridData}
            selectedNote={selectedNote}
            selectedOctave={selectedOctave}
            selectedMidiNumber={selectedMidiNumber}
            gridWidth={gridWidth}
            gridHeight={gridHeight}
          />
        </Col>
      </Row>
      <Row id="configArea" className="configRow">
        <Col md="8">
          <Keyboard currentOctaveNumber={currentOctave} onKeyClick={handleKeyClick} />
        </Col>
        <Col md="4">
        
        </Col>
      </Row>
    </Container>
  );
}
