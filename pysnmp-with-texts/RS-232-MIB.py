#
# PySNMP MIB module RS-232-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RS-232-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:16:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Unsigned32, transmission, NotificationType, MibIdentifier, Gauge32, Bits, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, TimeTicks, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "transmission", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "TimeTicks", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rs232 = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 33))
if mibBuilder.loadTexts: rs232.setLastUpdated('9405261700Z')
if mibBuilder.loadTexts: rs232.setOrganization('IETF Character MIB Working Group')
if mibBuilder.loadTexts: rs232.setContactInfo(' Bob Stewart Postal: Xyplex, Inc. 295 Foster Street Littleton, MA 01460 Tel: 508-952-4816 Fax: 508-952-4887 E-mail: rlstewart@eng.xyplex.com')
if mibBuilder.loadTexts: rs232.setDescription('The MIB module for RS-232-like hardware devices.')
rs232Number = MibScalar((1, 3, 6, 1, 2, 1, 10, 33, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232Number.setStatus('current')
if mibBuilder.loadTexts: rs232Number.setDescription('The number of ports (regardless of their current state) in the RS-232-like general port table.')
rs232PortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 33, 2), )
if mibBuilder.loadTexts: rs232PortTable.setStatus('current')
if mibBuilder.loadTexts: rs232PortTable.setDescription('A list of port entries. The number of entries is given by the value of rs232Number.')
rs232PortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 33, 2, 1), ).setIndexNames((0, "RS-232-MIB", "rs232PortIndex"))
if mibBuilder.loadTexts: rs232PortEntry.setStatus('current')
if mibBuilder.loadTexts: rs232PortEntry.setDescription('Status and parameter values for a port.')
rs232PortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortIndex.setStatus('current')
if mibBuilder.loadTexts: rs232PortIndex.setDescription('The value of ifIndex for the port. By convention and if possible, hardware port numbers map directly to external connectors. The value for each port must remain constant at least from one re-initialization of the network management agent to the next.')
rs232PortType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("rs232", 2), ("rs422", 3), ("rs423", 4), ("v35", 5), ("x21", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortType.setStatus('current')
if mibBuilder.loadTexts: rs232PortType.setDescription("The port's hardware type.")
rs232PortInSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortInSigNumber.setStatus('current')
if mibBuilder.loadTexts: rs232PortInSigNumber.setDescription('The number of input signals for the port in the input signal table (rs232PortInSigTable). The table contains entries only for those signals the software can detect and that are useful to observe.')
rs232PortOutSigNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232PortOutSigNumber.setStatus('current')
if mibBuilder.loadTexts: rs232PortOutSigNumber.setDescription('The number of output signals for the port in the output signal table (rs232PortOutSigTable). The table contains entries only for those signals the software can assert and that are useful to observe.')
rs232PortInSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortInSpeed.setStatus('current')
if mibBuilder.loadTexts: rs232PortInSpeed.setDescription("The port's input speed in bits per second. Note that non-standard values, such as 9612, are probably not allowed on most implementations.")
rs232PortOutSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortOutSpeed.setStatus('current')
if mibBuilder.loadTexts: rs232PortOutSpeed.setDescription("The port's output speed in bits per second. Note that non-standard values, such as 9612, are probably not allowed on most implementations.")
rs232PortInFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ctsRts", 2), ("dsrDtr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortInFlowType.setStatus('current')
if mibBuilder.loadTexts: rs232PortInFlowType.setDescription("The port's type of input flow control. 'none' indicates no flow control at this level. 'ctsRts' and 'dsrDtr' indicate use of the indicated hardware signals.")
rs232PortOutFlowType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ctsRts", 2), ("dsrDtr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232PortOutFlowType.setStatus('current')
if mibBuilder.loadTexts: rs232PortOutFlowType.setDescription("The port's type of output flow control. 'none' indicates no flow control at this level. 'ctsRts' and 'dsrDtr' indicate use of the indicated hardware signals.")
rs232AsyncPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 33, 3), )
if mibBuilder.loadTexts: rs232AsyncPortTable.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortTable.setDescription('A list of asynchronous port entries. Entries need not exist for synchronous ports.')
rs232AsyncPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 33, 3, 1), ).setIndexNames((0, "RS-232-MIB", "rs232AsyncPortIndex"))
if mibBuilder.loadTexts: rs232AsyncPortEntry.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortEntry.setDescription('Status and parameter values for an asynchronous port.')
rs232AsyncPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortIndex.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortIndex.setDescription('A unique value for each port. Its value is the same as rs232PortIndex for the port.')
rs232AsyncPortBits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortBits.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortBits.setDescription("The port's number of bits in a character.")
rs232AsyncPortStopBits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("one", 1), ("two", 2), ("oneAndHalf", 3), ("dynamic", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortStopBits.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortStopBits.setDescription("The port's number of stop bits.")
rs232AsyncPortParity = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("odd", 2), ("even", 3), ("mark", 4), ("space", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortParity.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortParity.setDescription("The port's sense of a character parity bit.")
rs232AsyncPortAutobaud = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232AsyncPortAutobaud.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortAutobaud.setDescription("A control for the port's ability to automatically sense input speed. When rs232PortAutoBaud is 'enabled', a port may autobaud to values different from the set values for speed, parity, and character size. As a result a network management system may temporarily observe values different from what was previously set.")
rs232AsyncPortParityErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortParityErrs.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortParityErrs.setDescription("Total number of characters with a parity error, input from the port since system re-initialization and while the port state was 'up' or 'test'.")
rs232AsyncPortFramingErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortFramingErrs.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortFramingErrs.setDescription("Total number of characters with a framing error, input from the port since system re-initialization and while the port state was 'up' or 'test'.")
rs232AsyncPortOverrunErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232AsyncPortOverrunErrs.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncPortOverrunErrs.setDescription("Total number of characters with an overrun error, input from the port since system re-initialization and while the port state was 'up' or 'test'.")
rs232SyncPortTable = MibTable((1, 3, 6, 1, 2, 1, 10, 33, 4), )
if mibBuilder.loadTexts: rs232SyncPortTable.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortTable.setDescription('A list of asynchronous port entries. Entries need not exist for synchronous ports.')
rs232SyncPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 33, 4, 1), ).setIndexNames((0, "RS-232-MIB", "rs232SyncPortIndex"))
if mibBuilder.loadTexts: rs232SyncPortEntry.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortEntry.setDescription('Status and parameter values for a synchronous port.')
rs232SyncPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortIndex.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortIndex.setDescription('A unique value for each port. Its value is the same as rs232PortIndex for the port.')
rs232SyncPortClockSource = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("internal", 1), ("external", 2), ("split", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortClockSource.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortClockSource.setDescription("Source of the port's bit rate clock. 'split' means the tranmit clock is internal and the receive clock is external.")
rs232SyncPortFrameCheckErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortFrameCheckErrs.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortFrameCheckErrs.setDescription("Total number of frames with an invalid frame check sequence, input from the port since system re-initialization and while the port state was 'up' or 'test'.")
rs232SyncPortTransmitUnderrunErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortTransmitUnderrunErrs.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortTransmitUnderrunErrs.setDescription("Total number of frames that failed to be transmitted on the port since system re-initialization and while the port state was 'up' or 'test' because data was not available to the transmitter in time.")
rs232SyncPortReceiveOverrunErrs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortReceiveOverrunErrs.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortReceiveOverrunErrs.setDescription("Total number of frames that failed to be received on the port since system re-initialization and while the port state was 'up' or 'test' because the receiver did not accept the data in time.")
rs232SyncPortInterruptedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortInterruptedFrames.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortInterruptedFrames.setDescription("Total number of frames that failed to be received or transmitted on the port due to loss of modem signals since system re-initialization and while the port state was 'up' or 'test'.")
rs232SyncPortAbortedFrames = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232SyncPortAbortedFrames.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortAbortedFrames.setDescription("Number of frames aborted on the port due to receiving an abort sequence since system re-initialization and while the port state was 'up' or 'test'.")
rs232SyncPortRole = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2))).clone('dce')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortRole.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortRole.setDescription('The role the device is playing that is using this port. dte means the device is performing the role of data terminal equipment dce means the device is performing the role of data circuit-terminating equipment.')
rs232SyncPortEncoding = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nrz", 1), ("nrzi", 2))).clone('nrz')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortEncoding.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortEncoding.setDescription('The bit stream encoding technique that is in effect for this port. nrz for Non-Return to Zero encoding nrzi for Non-Return to Zero Inverted encoding.')
rs232SyncPortRTSControl = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("controlled", 1), ("constant", 2))).clone('constant')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortRTSControl.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortRTSControl.setDescription("The method used to control the Request To Send (RTS) signal. controlled when the DTE is asserts RTS each time data needs to be transmitted and drops RTS at some point after data transmission begins. If rs232SyncPortRole is 'dte', the RTS is an output signal. The device will issue a RTS and wait for a CTS from the DCE before starting to transmit. If rs232SyncPortRole is 'dce', the RTS is an input signal. The device will issue a CTS only after having received RTS and waiting the rs232SyncPortRTSCTSDelay interval. constant when the DTE constantly asserts RTS.")
rs232SyncPortRTSCTSDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortRTSCTSDelay.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortRTSCTSDelay.setDescription('The interval (in milliseconds) that the DCE must wait after it sees RTS asserted before asserting CTS. This object exists in support of older synchronous devices that cannot recognize CTS within a certain interval after it asserts RTS.')
rs232SyncPortMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("fdx", 1), ("hdx", 2), ("simplex-receive", 3), ("simplex-send", 4))).clone('fdx')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortMode.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortMode.setDescription('The mode of operation of the port with respect to the direction and simultaneity of data transfer. fdx when frames on the data link can be transmitted and received at the same time hdx when frames can either be received from the data link or transmitted onto the data link but not at the same time. simplex-receive when frames can only be received on this data link. simplex-send when frames can only be sent on this data link.')
rs232SyncPortIdlePattern = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mark", 1), ("space", 2))).clone('space')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortIdlePattern.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortIdlePattern.setDescription('The bit pattern used to indicate an idle line.')
rs232SyncPortMinFlags = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 14), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rs232SyncPortMinFlags.setStatus('current')
if mibBuilder.loadTexts: rs232SyncPortMinFlags.setDescription('The minimum number of flag patterns this port needs in order to recognize the end of one frame and the start of the next. Plausible values are 1 and 2.')
rs232InSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 33, 5), )
if mibBuilder.loadTexts: rs232InSigTable.setStatus('current')
if mibBuilder.loadTexts: rs232InSigTable.setDescription('A list of port input control signal entries implemented and visible to the software on the port, and useful to monitor.')
rs232InSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 33, 5, 1), ).setIndexNames((0, "RS-232-MIB", "rs232InSigPortIndex"), (0, "RS-232-MIB", "rs232InSigName"))
if mibBuilder.loadTexts: rs232InSigEntry.setStatus('current')
if mibBuilder.loadTexts: rs232InSigEntry.setDescription('Input control signal status for a hardware port.')
rs232InSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigPortIndex.setStatus('current')
if mibBuilder.loadTexts: rs232InSigPortIndex.setDescription('The value of rs232PortIndex for the port to which this entry belongs.')
rs232InSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("rts", 1), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ("scts", 10), ("sdcd", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigName.setReference('EIA Standard RS-232-C, August 1969.')
if mibBuilder.loadTexts: rs232InSigName.setStatus('current')
if mibBuilder.loadTexts: rs232InSigName.setDescription('Identification of a hardware signal, as follows: rts Request to Send cts Clear to Send dsr Data Set Ready dtr Data Terminal Ready ri Ring Indicator dcd Received Line Signal Detector sq Signal Quality Detector srs Data Signaling Rate Selector srts Secondary Request to Send scts Secondary Clear to Send sdcd Secondary Received Line Signal Detector ')
rs232InSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigState.setStatus('current')
if mibBuilder.loadTexts: rs232InSigState.setDescription('The current signal state.')
rs232InSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232InSigChanges.setStatus('current')
if mibBuilder.loadTexts: rs232InSigChanges.setDescription("The number of times the signal has changed from 'on' to 'off' or from 'off' to 'on'.")
rs232OutSigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 33, 6), )
if mibBuilder.loadTexts: rs232OutSigTable.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigTable.setDescription('A list of port output control signal entries implemented and visible to the software on the port, and useful to monitor.')
rs232OutSigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 33, 6, 1), ).setIndexNames((0, "RS-232-MIB", "rs232OutSigPortIndex"), (0, "RS-232-MIB", "rs232OutSigName"))
if mibBuilder.loadTexts: rs232OutSigEntry.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigEntry.setDescription('Output control signal status for a hardware port.')
rs232OutSigPortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigPortIndex.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigPortIndex.setDescription('The value of rs232PortIndex for the port to which this entry belongs.')
rs232OutSigName = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("rts", 1), ("cts", 2), ("dsr", 3), ("dtr", 4), ("ri", 5), ("dcd", 6), ("sq", 7), ("srs", 8), ("srts", 9), ("scts", 10), ("sdcd", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigName.setReference('EIA Standard RS-232-C, August 1969.')
if mibBuilder.loadTexts: rs232OutSigName.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigName.setDescription('Identification of a hardware signal, as follows: rts Request to Send cts Clear to Send dsr Data Set Ready dtr Data Terminal Ready ri Ring Indicator dcd Received Line Signal Detector sq Signal Quality Detector srs Data Signaling Rate Selector srts Secondary Request to Send scts Secondary Clear to Send sdcd Secondary Received Line Signal Detector ')
rs232OutSigState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("on", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigState.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigState.setDescription('The current signal state.')
rs232OutSigChanges = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rs232OutSigChanges.setStatus('current')
if mibBuilder.loadTexts: rs232OutSigChanges.setDescription("The number of times the signal has changed from 'on' to 'off' or from 'off' to 'on'.")
rs232Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 33, 7))
rs232Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 33, 7, 1))
rs232Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 33, 7, 2))
rs232Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 33, 7, 2, 1)).setObjects(("RS-232-MIB", "rs232Group"), ("RS-232-MIB", "rs232AsyncGroup"), ("RS-232-MIB", "rs232SyncGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs232Compliance = rs232Compliance.setStatus('current')
if mibBuilder.loadTexts: rs232Compliance.setDescription('The compliance statement for SNMPv2 entities which have RS-232-like hardware interfaces.')
rs232Group = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 1)).setObjects(("RS-232-MIB", "rs232Number"), ("RS-232-MIB", "rs232PortIndex"), ("RS-232-MIB", "rs232PortType"), ("RS-232-MIB", "rs232PortInSigNumber"), ("RS-232-MIB", "rs232PortOutSigNumber"), ("RS-232-MIB", "rs232PortInSpeed"), ("RS-232-MIB", "rs232PortOutSpeed"), ("RS-232-MIB", "rs232PortInFlowType"), ("RS-232-MIB", "rs232PortOutFlowType"), ("RS-232-MIB", "rs232InSigPortIndex"), ("RS-232-MIB", "rs232InSigName"), ("RS-232-MIB", "rs232InSigState"), ("RS-232-MIB", "rs232InSigChanges"), ("RS-232-MIB", "rs232OutSigPortIndex"), ("RS-232-MIB", "rs232OutSigName"), ("RS-232-MIB", "rs232OutSigState"), ("RS-232-MIB", "rs232OutSigChanges"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs232Group = rs232Group.setStatus('current')
if mibBuilder.loadTexts: rs232Group.setDescription('A collection of objects providing information applicable to all RS-232-like interfaces.')
rs232AsyncGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 2)).setObjects(("RS-232-MIB", "rs232AsyncPortIndex"), ("RS-232-MIB", "rs232AsyncPortBits"), ("RS-232-MIB", "rs232AsyncPortStopBits"), ("RS-232-MIB", "rs232AsyncPortParity"), ("RS-232-MIB", "rs232AsyncPortAutobaud"), ("RS-232-MIB", "rs232AsyncPortParityErrs"), ("RS-232-MIB", "rs232AsyncPortFramingErrs"), ("RS-232-MIB", "rs232AsyncPortOverrunErrs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs232AsyncGroup = rs232AsyncGroup.setStatus('current')
if mibBuilder.loadTexts: rs232AsyncGroup.setDescription('A collection of objects providing information applicable to asynchronous RS-232-like interfaces.')
rs232SyncGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 3)).setObjects(("RS-232-MIB", "rs232SyncPortIndex"), ("RS-232-MIB", "rs232SyncPortClockSource"), ("RS-232-MIB", "rs232SyncPortFrameCheckErrs"), ("RS-232-MIB", "rs232SyncPortTransmitUnderrunErrs"), ("RS-232-MIB", "rs232SyncPortReceiveOverrunErrs"), ("RS-232-MIB", "rs232SyncPortInterruptedFrames"), ("RS-232-MIB", "rs232SyncPortAbortedFrames"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs232SyncGroup = rs232SyncGroup.setStatus('current')
if mibBuilder.loadTexts: rs232SyncGroup.setDescription('A collection of objects providing information applicable to synchronous RS-232-like interfaces.')
rs232SyncSDLCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 4)).setObjects(("RS-232-MIB", "rs232SyncPortRole"), ("RS-232-MIB", "rs232SyncPortEncoding"), ("RS-232-MIB", "rs232SyncPortRTSControl"), ("RS-232-MIB", "rs232SyncPortRTSCTSDelay"), ("RS-232-MIB", "rs232SyncPortMode"), ("RS-232-MIB", "rs232SyncPortIdlePattern"), ("RS-232-MIB", "rs232SyncPortMinFlags"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rs232SyncSDLCGroup = rs232SyncSDLCGroup.setStatus('current')
if mibBuilder.loadTexts: rs232SyncSDLCGroup.setDescription('A collection of objects providing information applicable to synchronous RS-232-like interfaces running SDLC.')
mibBuilder.exportSymbols("RS-232-MIB", rs232OutSigChanges=rs232OutSigChanges, rs232OutSigState=rs232OutSigState, rs232SyncPortRTSControl=rs232SyncPortRTSControl, rs232PortOutFlowType=rs232PortOutFlowType, rs232SyncPortEncoding=rs232SyncPortEncoding, rs232OutSigName=rs232OutSigName, rs232PortEntry=rs232PortEntry, rs232InSigPortIndex=rs232InSigPortIndex, PYSNMP_MODULE_ID=rs232, rs232PortType=rs232PortType, rs232OutSigTable=rs232OutSigTable, rs232SyncPortAbortedFrames=rs232SyncPortAbortedFrames, rs232AsyncPortBits=rs232AsyncPortBits, rs232AsyncPortParityErrs=rs232AsyncPortParityErrs, rs232InSigName=rs232InSigName, rs232Compliance=rs232Compliance, rs232AsyncPortEntry=rs232AsyncPortEntry, rs232SyncPortMinFlags=rs232SyncPortMinFlags, rs232SyncPortRole=rs232SyncPortRole, rs232AsyncPortStopBits=rs232AsyncPortStopBits, rs232PortOutSigNumber=rs232PortOutSigNumber, rs232AsyncPortOverrunErrs=rs232AsyncPortOverrunErrs, rs232SyncPortTable=rs232SyncPortTable, rs232SyncPortInterruptedFrames=rs232SyncPortInterruptedFrames, rs232InSigEntry=rs232InSigEntry, rs232AsyncPortAutobaud=rs232AsyncPortAutobaud, rs232PortOutSpeed=rs232PortOutSpeed, rs232Compliances=rs232Compliances, rs232SyncSDLCGroup=rs232SyncSDLCGroup, rs232PortInSpeed=rs232PortInSpeed, rs232SyncPortMode=rs232SyncPortMode, rs232AsyncPortParity=rs232AsyncPortParity, rs232PortIndex=rs232PortIndex, rs232Conformance=rs232Conformance, rs232=rs232, rs232SyncPortClockSource=rs232SyncPortClockSource, rs232SyncPortRTSCTSDelay=rs232SyncPortRTSCTSDelay, rs232PortTable=rs232PortTable, rs232AsyncPortIndex=rs232AsyncPortIndex, rs232SyncPortIndex=rs232SyncPortIndex, rs232SyncGroup=rs232SyncGroup, rs232SyncPortTransmitUnderrunErrs=rs232SyncPortTransmitUnderrunErrs, rs232Number=rs232Number, rs232SyncPortIdlePattern=rs232SyncPortIdlePattern, rs232PortInFlowType=rs232PortInFlowType, rs232Group=rs232Group, rs232OutSigEntry=rs232OutSigEntry, rs232InSigChanges=rs232InSigChanges, rs232AsyncPortFramingErrs=rs232AsyncPortFramingErrs, rs232Groups=rs232Groups, rs232SyncPortEntry=rs232SyncPortEntry, rs232SyncPortReceiveOverrunErrs=rs232SyncPortReceiveOverrunErrs, rs232PortInSigNumber=rs232PortInSigNumber, rs232InSigTable=rs232InSigTable, rs232SyncPortFrameCheckErrs=rs232SyncPortFrameCheckErrs, rs232AsyncGroup=rs232AsyncGroup, rs232AsyncPortTable=rs232AsyncPortTable, rs232OutSigPortIndex=rs232OutSigPortIndex, rs232InSigState=rs232InSigState)
