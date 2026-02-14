import { useState } from 'react';
import { Container, Row, Col, Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, NavLink } from 'reactstrap';
import Keyboard from '../keyboardComponent/keyboard';
import './layout.css';
import OctaveSelect from '../octaveComponent/octaveSelect';
import Information from '../informationComponent/information';
import NoteDurationSelect from '../noteDurationComponent/noteDurationSelect';
import PixelGrid from '../pixelGridComponent/pixelGrid';
import GridSize from '../gridSizeComponent/gridSize';

export default function Layout() {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const toggle = () => setIsOpen(!isOpen);
  const [currentOctave, setCurrentOctave] = useState(4); // middle c default
  const [currentNoteDuration, setCurrentNoteDuration] = useState(2); // whole note default
  const [gridHeight, setGridHeight] = useState(16); // default 16x16
  const [gridWidth, setGridWidth] = useState(16); // default 16x16
  const [selectedNote, setSelectedNote] = useState<string>('');
  const [selectedOctave, setSelectedOctave] = useState<number | undefined>(undefined);
  const [selectedMidiNumber, setSelectedMidiNumber] = useState<number | undefined>(undefined);
  const [selectedCellIndex, setSelectedCellIndex] = useState<number>(0);
  const [keyPressId, setKeyPressId] = useState<number>(0);

  const handleOctaveChange = (octave: number) => {
    setCurrentOctave(octave);
  };

  const handleNoteDurationChange = (noteDuration: number) => {
    setCurrentNoteDuration(noteDuration);
  };

  const handleGridSizeChange = (width: number, height: number) => {
    setGridWidth(width);
    setGridHeight(height);
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
          Song Info
        </Col>
        <Col md="8">
          <PixelGrid 
            height={gridHeight} 
            width={gridWidth}
            currentNote={selectedNote}
            currentOctave={selectedOctave}
            currentMidiNumber={selectedMidiNumber}
            currentNoteDuration={currentNoteDuration}
            keyPressId={keyPressId}
            onCellSelect={handleCellSelect}
          />
        </Col>
        <Col md="2">
          
        </Col>
      </Row>
      <Row className="15">
        <Col md="2">
          <OctaveSelect currentOctave={currentOctave} onOctaveChange={handleOctaveChange} />
          <GridSize onGridSizeChange={handleGridSizeChange} />
          <NoteDurationSelect currentNoteDuration={currentNoteDuration} onNoteDurationChange={handleNoteDurationChange} />
        </Col>
        <Col md="8">
          <Keyboard currentOctaveNumber={currentOctave} onKeyClick={handleKeyClick} />
        </Col>
        <Col md="2">
          <Information currentOctaveNumber={currentOctave} currentNoteDurationNumber={currentNoteDuration} gridHeight={gridHeight} gridWidth={gridWidth} />
        </Col>
      </Row>
    </Container>
  );
}
