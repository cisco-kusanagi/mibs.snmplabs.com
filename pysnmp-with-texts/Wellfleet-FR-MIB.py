#
# PySNMP MIB module Wellfleet-FR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-FR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:40:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, iso, Bits, NotificationType, enterprises, mgmt, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, NotificationType, Opaque, mib_2, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "iso", "Bits", "NotificationType", "enterprises", "mgmt", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "NotificationType", "Opaque", "mib-2", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfFrameRelayGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfFrameRelayGroup")
wfFrDlcmiTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1), )
if mibBuilder.loadTexts: wfFrDlcmiTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfFrDlcmiTable.setDescription('The Parameters for the Data Link Connection Management Interface')
wfFrDlcmiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1), ).setIndexNames((0, "Wellfleet-FR-MIB", "wfFr1DlcmiCircuit"))
if mibBuilder.loadTexts: wfFrDlcmiEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfFrDlcmiEntry.setDescription('The parameters for a particular Data Link Connection Management Interface')
wfFr1DlcmiDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiDelete.setDescription('Indication to delete this frame relay interface')
wfFr1DlcmiDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiDisable.setDescription('Indicates when a dlcmi entry is to be enabled or disabled.')
wfFr1DlcmiState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiState.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiState.setDescription('The current state of Frame Relay. The not present state is not actually valid except when the record is first added. It is included for consistency.')
wfFr1DlcmiCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiCircuit.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiCircuit.setDescription('Instance identifier. The circuit number of this entry')
wfFr1DlcmiManagementType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("none", 1), ("lmi", 2), ("t1617d", 3), ("t1617b", 4), ("annexa", 5), ("lmiswitch", 6), ("annexdswitch", 7), ("annexaswitch", 8))).clone('t1617d')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiManagementType.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiManagementType.setDescription('This variable indicates which Data Link Connection Management scheme is active (and by implication, what DLCI it uses).')
wfFr1DlcmiStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("start", 1), ("running", 2), ("fault", 3), ("recovered", 4))).clone('start')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiStatus.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiStatus.setDescription('Indicates the status of the interface. FR1_STATUS_START is the state during rebooting or initial start of circuit FR1_STATUS_RUNNING1 is the sate after the circuit is up (either LMI successful or there is no DLCMI and the system just comes up). FR1_STATUS_FAULT is a transient state indicating that errors have caused the circuit to be disabled until DLCMI recovery. FR1_STATUS_RECOVERED indicates that an the system has been in the FR_STATUS_FAULT mode before, but has since recovered.')
wfFr1DlcmiAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("q921", 1), ("q922march90", 2), ("q922november90", 3), ("q922", 4))).clone('q922')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiAddress.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiAddress.setDescription('This states which address format is in use on the FR interface. The default is Q922')
wfFr1DlcmiAddressLen = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4))).clone(namedValues=NamedValues(("twobyte", 2), ("threebyte", 3), ("fourbyte", 4))).clone('twobyte')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiAddressLen.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiAddressLen.setDescription('This variable states the address length in octets. In the case of Q922 format, the length indicates the entire length of the address includeding the control portion.')
wfFr1DlcmiPollingInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 30)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiPollingInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiPollingInterval.setDescription('The number of seconds between successive status enquiry messages')
wfFr1DlcmiFullEnquiryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiFullEnquiryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiFullEnquiryInterval.setDescription('The number of status enquiry intervals that pass before issuance of a full status enquiry message.')
wfFr1DlcmiErrorThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 11), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiErrorThreshold.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiErrorThreshold.setDescription('This is the maximum number of unanswered Status Enquiries the equipment shall accept before declaring the interface down.')
wfFr1DlcmiMonitoredEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 12), Integer32().clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiMonitoredEvents.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiMonitoredEvents.setDescription("This is the number of status polling intervals over which the error threshold is counted. For example, if within 'MonitoredEvents' number of events the station receives 'ErrorThreshold' number of errors, the interface is marked as down.")
wfFr1DlcmiMaxSupportedVCs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiMaxSupportedVCs.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiMaxSupportedVCs.setDescription('The maximum number of Virtual Circuits allowed for this interface. Usually dictated by the Frame Relay network. The system sets this initially.')
wfFr1DlcmiMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1DlcmiMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiMulticast.setDescription('This indicates whether the frame relay provider offers a multicast')
wfFr1DlcmiSeqCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiSeqCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiSeqCount.setDescription("This station's sequence counter. It represents the next value to send.")
wfFr1DlcmiLastReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiLastReceived.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiLastReceived.setDescription('The sequence number just received from the switch.')
wfFr1DlcmiPassiveSeqCount = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiPassiveSeqCount.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiPassiveSeqCount.setDescription("This station's sequence counter for answering status enquiry.")
wfFr1DlcmiPassiveReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiPassiveReceived.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiPassiveReceived.setDescription('The sequence number just received from the enquring station.')
wfFr1DlcmiPolls = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiPolls.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiPolls.setDescription('This is the counter of where we are in the polling cycle.')
wfFr1DlcmiAlarmTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 20), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1DlcmiAlarmTimer.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1DlcmiAlarmTimer.setDescription('This is a counter of 1/2 second timeouts. When it reaches 2 x the polling interval, an enquiry message is sent.')
wfFr1ErrType = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("unknown", 1), ("short", 2), ("long", 3), ("illegaldlci", 4), ("unknowndlci", 5), ("protoerr", 6), ("unknownie", 7), ("sequenceerr", 8), ("unknownrpt", 9), ("reset", 10), ("cntrl", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1ErrType.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1ErrType.setDescription('Indicate the type of the last specific monitored error.')
wfFr1ErrData = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 22), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1ErrData.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1ErrData.setDescription('Contains as much of the error packet as possible.')
wfFr1ErrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 23), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1ErrTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1ErrTime.setDescription('The time the last error occurred.')
wfFr1ErrDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1ErrDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1ErrDiscards.setDescription('The number of inbound frames dropped because of format or other errors or because the VC was not known.')
wfFr1ErrDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1ErrDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1ErrDrops.setDescription('The number of outbound frames dropped. Usually this is due the specified DLCI being unknown or a broadcast packet is too long')
wfFrCircuitTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2), )
if mibBuilder.loadTexts: wfFrCircuitTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfFrCircuitTable.setDescription('Frame Relay Circuit table gives information about a virtual circuits.')
wfFrCircuitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1), ).setIndexNames((0, "Wellfleet-FR-MIB", "wfFr1CircuitNumber"), (0, "Wellfleet-FR-MIB", "wfFr1CircuitDlci"))
if mibBuilder.loadTexts: wfFrCircuitEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfFrCircuitEntry.setDescription('An entry in the Frame Relay Circuit table.')
wfFr1CircuitDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2), ("system", 3))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitDelete.setDescription('Indication to delete this frame relay interface.')
wfFr1CircuitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitNumber.setDescription('Instance identifier. The circuit number of this interface.')
wfFr1CircuitDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(16, 1007, 1024, 64511, 131072, 8257535))).clone(namedValues=NamedValues(("twobyteminimum", 16), ("twobytemaximum", 1007), ("threebyteminimum", 1024), ("threebytemaximum", 64511), ("fourbyteminimum", 131072), ("fourbytemaximum", 8257535)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitDlci.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitDlci.setDescription('Instance identifier. This indicates which virtual circuit.')
wfFr1CircuitState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3), ("xoff", 4), ("control", 5))).clone('invalid')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitState.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitState.setDescription('Indicates the state of the particular virtual circuit.')
wfFr1CircuitStateSet = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3))).clone('invalid')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitStateSet.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitStateSet.setDescription('User access for setting the state of a virtual circuit')
wfFr1CircuitReceivedFECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitReceivedFECNs.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitReceivedFECNs.setDescription('Number of frames received indicating forward congestion.')
wfFr1CircuitReceivedBECNs = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitReceivedBECNs.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitReceivedBECNs.setDescription('Number of frames received indicating backward congestion.')
wfFr1CircuitSentFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitSentFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitSentFrames.setDescription('The number of frames sent from this virtual circuit.')
wfFr1CircuitSentOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitSentOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitSentOctets.setDescription('The number of octets sent from this virtual circuit.')
wfFr1CircuitReceivedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitReceivedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitReceivedFrames.setDescription('The number of frames received from this virtual circuit.')
wfFr1CircuitReceivedOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitReceivedOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitReceivedOctets.setDescription('The number of octets received from this virtual circuit.')
wfFr1CircuitCreationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitCreationTime.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitCreationTime.setDescription('The value of sysUpTime when the vc was created.')
wfFr1CircuitLastTimeChange = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitLastTimeChange.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitLastTimeChange.setDescription('The value of sysUpTime when last there was a change in vc state.')
wfFr1CircuitCommittedBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 14), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitCommittedBurst.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitCommittedBurst.setDescription('Indicates the maximum amount of data, in bits, that the network agrees to transfer under normal conditions, during the measurement interval. Wellfleet does not presently support this.')
wfFr1CircuitExcessBurst = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 15), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitExcessBurst.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitExcessBurst.setDescription('Indicates teh maximum amount of uncommitted data bits that the network will attempt to deliver over the measurement interval. Wellfleet does not presently support this.')
wfFr1CircuitThroughput = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitThroughput.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitThroughput.setDescription("This is the average number of 'Frame Relay Information Field' bits transferred per second across a user network interface in one direction, measured over the measurement interval. Wellfleet does not presently support this.")
wfFr1CircuitMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("multicast", 1), ("unicast", 2))).clone('unicast')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitMulticast.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitMulticast.setDescription('Indicates whether this DLCI is used for multicast or single destination.')
wfFr1CircuitDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitDiscards.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitDiscards.setDescription('The number of inbound frames discarded because of format errors, because the VC is inactive or because the protocol was not registered for this circuit.')
wfFr1CircuitDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfFr1CircuitDrops.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitDrops.setDescription('Indicates how many outbound frames were dropped. Usually these are dropped because the VC is not active.')
wfFr1CircuitSubCct = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 20), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitSubCct.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitSubCct.setDescription('Circuit number to use for this VC when configured in hybrid (for bridging) or direct access (VC as a circuit) mode.')
wfFr1CircuitMode = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("group", 1), ("hybrid", 2), ("direct", 3))).clone('group')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfFr1CircuitMode.setStatus('mandatory')
if mibBuilder.loadTexts: wfFr1CircuitMode.setDescription("The mode of the given VC. GROUP - treats the VC as one of many vc's on a circuit. HYBRID - treats the VC as one of many vc's on a circuit for protocol traffic, but as a separate circuit for bridging. DIRECT - treats the VC as a separate circuit for all applications.")
mibBuilder.exportSymbols("Wellfleet-FR-MIB", wfFr1DlcmiFullEnquiryInterval=wfFr1DlcmiFullEnquiryInterval, wfFr1CircuitThroughput=wfFr1CircuitThroughput, wfFr1DlcmiStatus=wfFr1DlcmiStatus, wfFrCircuitEntry=wfFrCircuitEntry, wfFr1DlcmiAddressLen=wfFr1DlcmiAddressLen, wfFr1CircuitReceivedOctets=wfFr1CircuitReceivedOctets, wfFr1DlcmiSeqCount=wfFr1DlcmiSeqCount, wfFr1DlcmiPassiveSeqCount=wfFr1DlcmiPassiveSeqCount, wfFr1ErrData=wfFr1ErrData, wfFr1DlcmiPassiveReceived=wfFr1DlcmiPassiveReceived, wfFr1CircuitState=wfFr1CircuitState, wfFr1ErrDrops=wfFr1ErrDrops, wfFr1CircuitSentOctets=wfFr1CircuitSentOctets, wfFr1DlcmiMaxSupportedVCs=wfFr1DlcmiMaxSupportedVCs, wfFrCircuitTable=wfFrCircuitTable, wfFr1CircuitStateSet=wfFr1CircuitStateSet, wfFr1DlcmiMonitoredEvents=wfFr1DlcmiMonitoredEvents, wfFr1DlcmiDisable=wfFr1DlcmiDisable, wfFrDlcmiEntry=wfFrDlcmiEntry, wfFr1DlcmiState=wfFr1DlcmiState, wfFrDlcmiTable=wfFrDlcmiTable, wfFr1CircuitMulticast=wfFr1CircuitMulticast, wfFr1CircuitNumber=wfFr1CircuitNumber, wfFr1CircuitDrops=wfFr1CircuitDrops, wfFr1DlcmiErrorThreshold=wfFr1DlcmiErrorThreshold, wfFr1CircuitReceivedFECNs=wfFr1CircuitReceivedFECNs, wfFr1CircuitReceivedBECNs=wfFr1CircuitReceivedBECNs, wfFr1ErrType=wfFr1ErrType, wfFr1CircuitLastTimeChange=wfFr1CircuitLastTimeChange, wfFr1CircuitReceivedFrames=wfFr1CircuitReceivedFrames, wfFr1DlcmiMulticast=wfFr1DlcmiMulticast, wfFr1CircuitExcessBurst=wfFr1CircuitExcessBurst, wfFr1CircuitDiscards=wfFr1CircuitDiscards, wfFr1ErrDiscards=wfFr1ErrDiscards, wfFr1DlcmiLastReceived=wfFr1DlcmiLastReceived, wfFr1DlcmiCircuit=wfFr1DlcmiCircuit, wfFr1ErrTime=wfFr1ErrTime, wfFr1DlcmiAlarmTimer=wfFr1DlcmiAlarmTimer, wfFr1CircuitSentFrames=wfFr1CircuitSentFrames, wfFr1CircuitSubCct=wfFr1CircuitSubCct, wfFr1DlcmiPollingInterval=wfFr1DlcmiPollingInterval, wfFr1CircuitCreationTime=wfFr1CircuitCreationTime, wfFr1CircuitDlci=wfFr1CircuitDlci, wfFr1DlcmiAddress=wfFr1DlcmiAddress, wfFr1DlcmiManagementType=wfFr1DlcmiManagementType, wfFr1CircuitCommittedBurst=wfFr1CircuitCommittedBurst, wfFr1CircuitMode=wfFr1CircuitMode, wfFr1CircuitDelete=wfFr1CircuitDelete, wfFr1DlcmiDelete=wfFr1DlcmiDelete, wfFr1DlcmiPolls=wfFr1DlcmiPolls)
