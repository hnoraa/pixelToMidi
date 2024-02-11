import { useState } from 'react';
import { Container, Row, Col, Navbar, NavbarBrand, Nav, NavbarToggler, Collapse, NavItem, NavLink } from 'reactstrap';
import Keyboard from '../keyboardComponent/keyboard';
import './layout.css';
import OctaveSelect from '../octaveComponent/octaveSelect';
import Information from '../informationComponent/information';
import NoteDurationSelect from '../noteDurationComponent/noteDurationSelect';

export default function Layout() {
  const [isOpen, setIsOpen] = useState<boolean>(false);
  const toggle = () => setIsOpen(!isOpen);
  const [currentOctave, setCurrentOctave] = useState(4); // middle c default
  const [currentNoteDuration, setCurrentNoteDuration] = useState(2); // whole note default

  const handleOctaveChange = (octave: number) => {
    setCurrentOctave(octave);
  };

  const handleNoteDurationChange = (noteDuration: number) => {
    setCurrentNoteDuration(noteDuration);
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
        <Col md="4">
          Song Info
        </Col>
        <Col md="8">
          Pixel Grid
        </Col>
      </Row>
      <Row className="15">
        <Col md="3">
          <OctaveSelect currentOctave={currentOctave} onOctaveChange={handleOctaveChange} />
        </Col>
        <Col md="3">
          <NoteDurationSelect currentNoteDuration={currentNoteDuration} onNoteDurationChange={handleNoteDurationChange} />
        </Col>
        <Col md="6">
          <Information currentOctaveNumber={currentOctave} currentNoteDurationNumber={currentNoteDuration} />
        </Col>
      </Row>
      <Keyboard currentOctaveNumber={currentOctave} />
    </Container>
  );
}
