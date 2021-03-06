#
# PySNMP MIB module CT-DAWANCONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DAWANCONN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:28:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, iso, NotificationType, ObjectIdentity, Bits, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, IpAddress, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "iso", "NotificationType", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "IpAddress", "MibIdentifier", "Integer32")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daWanConnection = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 17))
class DisplayString(OctetString):
    pass

daWanNumConnections = MibScalar((1, 3, 6, 1, 4, 1, 52, 4497, 17, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanNumConnections.setStatus('mandatory')
if mibBuilder.loadTexts: daWanNumConnections.setDescription('This is the total number of connection objects currently in the system.')
daWanConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2), )
if mibBuilder.loadTexts: daWanConnectionTable.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionTable.setDescription('A list of Demand Access remote WAN connections')
daWanConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1), ).setIndexNames((0, "CT-DAWANCONN-MIB", "daWanConnectionIndex"))
if mibBuilder.loadTexts: daWanConnectionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionEntry.setDescription('An entry containing wan connection information and statistics.')
daWanConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionIndex.setDescription('This is the index into this table. This index uniquely identifies the Connection.')
daWanConnectionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionIfIndex.setDescription('This is the ifIndex value of the wan connection group. If the ifIndex value is unknown, the value of this object will be zero.')
daWanConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("inactive", 1), ("connecting", 2), ("connected", 3), ("active", 4), ("disconnecting", 5), ("disconnected", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionState.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionState.setDescription('This is the state of the Connection.')
daWanConnectionConnectControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("connect", 1), ("disconnect", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: daWanConnectionConnectControl.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionConnectControl.setDescription('This object controls the desired state of the wan Connection. Setting this object to connect(1) will initiate the set of actions to bring the wan Connection to the active state. Only set the object to connect(1) when the current value of daWanConnectionState is inactive. Setting this object to disconnect(2) will initiate the set of actions to bring the wan Connection to the inactive state. Only set this object to disconnect(2) when the daWanConnectionState is active. After setting the Connection to connect(1) or disconnect(2), refer to daWanConnectionState to determine the state of the wan Connection. Queries to daWanConnectionConnectControl return unknown results.')
daWanConnectionConnectType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("digitalCircuit", 1), ("analogCircuit", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionConnectType.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionConnectType.setDescription('This specifies the type of the wan connection.')
daWanConnectionDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionDeviceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionDeviceIndex.setDescription('This is the index of the device that is associated with this connection. This value will be zero if there is no device associated with this device.')
daWanConnectionConnectSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionConnectSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionConnectSpeed.setDescription('The information transfer speed in bits/second when calling this peer. The detailed media specific information, e.g. information type and information transfer rate for ISDN circuits, has to be extracted from this object. If the transfer speed to be used is unknown the value of this object may be zero.')
daWanConnectionLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionLocalAddress.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionLocalAddress.setDescription("Call Address at which the connection will originate from. Think of this as the set of characters following 'ATDT ' or the 'phone number' included in a D channel call request. The structure of this information will be switch type specific. If there is no address information required for reaching the peer, i.e., for leased lines, this object will be a zero length string.")
daWanConnectionPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionPeerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionPeerAddress.setDescription('Calling Party Number information element, as for example passed in an ISDN SETUP message by a PBX or switch, for incoming calls. This address can be used to identify the peer. If this address is either unknown or identical to daWanConnectionLocalAddress, this object will be a zero length string.')
daWanConnectionSubAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionSubAddress.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionSubAddress.setDescription('Subaddress at which the connection will originate from. If the subaddress is undefined for the given media or unused, then the value is zero.')
daWanConnectionInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10))).clone('other')).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionInfoType.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionInfoType.setDescription('The Information Transfer Capability to be used for this connection. speech(2) refers to a non-data connection, whereas audio31(6) and audio7(7) refer to data mode connections.')
daWanConnectionChargedUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionChargedUnits.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionChargedUnits.setDescription('The number of charged units for this connection. For incoming calls or if charging information is not supplied by the switch, the value of this object will be zero.')
daWanConnectionConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionConnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionConnectTime.setDescription('The value of sysUpTime when this connection was completed. This object will be updated whenever a call is completed.')
daWanConnectionConnectDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionConnectDirection.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionConnectDirection.setDescription('The direction from which this connect occurred.')
daWanConnectionDisconnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionDisconnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionDisconnectTime.setDescription('The value of sysUpTime when this call was disconnected. This object will be updated whenever a call is disconnected.')
daWanConnectionDisconnectDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("in", 1), ("out", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionDisconnectDirection.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionDisconnectDirection.setDescription('The direction from which this disconnect occurred.')
daWanConnectionDisconnectCause = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 17), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionDisconnectCause.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionDisconnectCause.setDescription('The encoded network cause value associated with this call. This object will be updated whenever a call is started or cleared. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface.')
daWanConnectionDisconnectText = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 17, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionDisconnectText.setStatus('mandatory')
if mibBuilder.loadTexts: daWanConnectionDisconnectText.setDescription('ASCII text describing the reason for this call termination. This object exists because it would be impossible for a management station to store all possible cause values for all types of interfaces. It should be used only if a management station is unable to decode the value of daWanConnectionDisconnectCause. This object will be updated whenever a call is started or cleared.')
mibBuilder.exportSymbols("CT-DAWANCONN-MIB", daWanConnectionState=daWanConnectionState, daWanConnectionEntry=daWanConnectionEntry, daWanConnectionSubAddress=daWanConnectionSubAddress, daWanNumConnections=daWanNumConnections, daWanConnectionConnectDirection=daWanConnectionConnectDirection, daWanConnectionInfoType=daWanConnectionInfoType, daWanConnectionDeviceIndex=daWanConnectionDeviceIndex, daWanConnectionTable=daWanConnectionTable, daWanConnectionIfIndex=daWanConnectionIfIndex, daWanConnectionConnectType=daWanConnectionConnectType, daWanConnectionIndex=daWanConnectionIndex, daWanConnectionConnectSpeed=daWanConnectionConnectSpeed, daWanConnectionDisconnectCause=daWanConnectionDisconnectCause, daWanConnectionDisconnectDirection=daWanConnectionDisconnectDirection, daWanConnectionConnectTime=daWanConnectionConnectTime, daWanConnectionPeerAddress=daWanConnectionPeerAddress, daWanConnectionChargedUnits=daWanConnectionChargedUnits, DisplayString=DisplayString, daWanConnection=daWanConnection, daWanConnectionDisconnectText=daWanConnectionDisconnectText, ctSSA=ctSSA, daWanConnectionDisconnectTime=daWanConnectionDisconnectTime, daWanConnectionLocalAddress=daWanConnectionLocalAddress, daWanConnectionConnectControl=daWanConnectionConnectControl)
