#
# PySNMP MIB module EICON-MIB-PORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EICON-MIB-PORT
# Produced by pysmi-0.3.4 at Wed May  1 12:59:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
NotificationType, ObjectIdentity, NotificationType, ModuleIdentity, Unsigned32, Gauge32, enterprises, TimeTicks, Bits, Counter64, MibIdentifier, Counter32, Integer32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Unsigned32", "Gauge32", "enterprises", "TimeTicks", "Bits", "Counter64", "MibIdentifier", "Counter32", "Integer32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eicon = MibIdentifier((1, 3, 6, 1, 4, 1, 434))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2))
mibv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2))
module = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 4))
port = MibIdentifier((1, 3, 6, 1, 4, 1, 434, 2, 2, 3))
class OperState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("disabled", 2), ("ready", 3), ("active", 4), ("busy", 5))

class AdminState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("start", 1), ("stop", 2), ("dump", 3), ("test", 4), ("invalid", 5))

class ActionState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("done", 1), ("failed", 2), ("in-progress", 3))

class CardRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 6)

class PortRef(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 48)

class PortName(DisplayString):
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 15)

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

portNumberOfPorts = MibScalar((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 1), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portNumberOfPorts.setStatus('mandatory')
if mibBuilder.loadTexts: portNumberOfPorts.setDescription('The number of existing ports on all installed EiconCards, as seen by the Agent.')
portTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
if mibBuilder.loadTexts: portTable.setDescription('The table of the ports seen by the agent.')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1), ).setIndexNames((0, "EICON-MIB-PORT", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
if mibBuilder.loadTexts: portEntry.setDescription('The set of attributes for one port.')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 1), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
if mibBuilder.loadTexts: portIndex.setDescription('The index of the port generated by the Agent. Used in all other tables refering to ports.')
portLanaNo = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 2), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLanaNo.setStatus('mandatory')
if mibBuilder.loadTexts: portLanaNo.setDescription('The LANA number of the port from the configuration, range: 1..48.')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 3), PortName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('mandatory')
if mibBuilder.loadTexts: portName.setDescription('The unique port name.')
portCardLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 4), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCardLocation.setStatus('mandatory')
if mibBuilder.loadTexts: portCardLocation.setDescription('The card reference. It should match the cardIndex (from the cardTable) of the card that this port belongs to.')
portDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portDescription.setStatus('mandatory')
if mibBuilder.loadTexts: portDescription.setDescription('A general description of the port set by the Operator.')
portOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 6), OperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOperState.setStatus('mandatory')
if mibBuilder.loadTexts: portOperState.setDescription('The operational state of the port.')
portAdminStateCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 7), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portAdminStateCtr.setStatus('mandatory')
if mibBuilder.loadTexts: portAdminStateCtr.setDescription("The parameter that can be modified by the Operator in order to change the state of the port. The value 'locked' is used to stop the port, the value 'unlocked' isued to start the port.")
portOpenTime = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOpenTime.setStatus('mandatory')
if mibBuilder.loadTexts: portOpenTime.setDescription('The time the port was activated.')
portProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portProtocols.setStatus('mandatory')
if mibBuilder.loadTexts: portProtocols.setDescription('The mask indicating what is running on the port: lapb=0x1, sdlc=0x2, x25=0x4, frbs=0x8, dialer=0x100, ppp=0x1000.')
portDialerType = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("direct", 1), ("v25bis", 2), ("v22bis", 3), ("at-cmd", 4), ("isdn-stat", 5), ("v32bis", 6), ("none", 7), ("other", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portDialerType.setStatus('mandatory')
if mibBuilder.loadTexts: portDialerType.setDescription('The dialer type.')
portActionState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 11), ActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portActionState.setStatus('mandatory')
if mibBuilder.loadTexts: portActionState.setDescription('The state of the operation performed on the port by the Agent as a result of setting the values to the portAdminStateCtr. The Management station will poll that variable after initiating an action on the port. The value done(1) indicates that the action terminated successfully. The value failed(2) indicates that the action terminated with an error. In this case the variable portActionError indicates the error code.')
portActionError = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("no-error", 0), ("err-WARNING", 1), ("err-PARTIAL", 2), ("err-ABORT", 3), ("err-FAILED", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portActionError.setStatus('mandatory')
if mibBuilder.loadTexts: portActionError.setDescription('The error code after the unsuccessful operation.')
portTrapStateChange = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,31)).setObjects(("SNMPv2-MIB", "sysName"), ("EICON-MIB-PORT", "portIndex"), ("EICON-MIB-PORT", "portOperState"))
if mibBuilder.loadTexts: portTrapStateChange.setDescription('The trap indicates that the port has changed state.')
mibBuilder.exportSymbols("EICON-MIB-PORT", module=module, ActionState=ActionState, PortRef=PortRef, portOperState=portOperState, portAdminStateCtr=portAdminStateCtr, portCardLocation=portCardLocation, portTable=portTable, portActionError=portActionError, portEntry=portEntry, AdminState=AdminState, portOpenTime=portOpenTime, portDialerType=portDialerType, portName=portName, portIndex=portIndex, portProtocols=portProtocols, portTrapStateChange=portTrapStateChange, portNumberOfPorts=portNumberOfPorts, mibv2=mibv2, PositiveInteger=PositiveInteger, eicon=eicon, port=port, PortName=PortName, management=management, portDescription=portDescription, portLanaNo=portLanaNo, CardRef=CardRef, portActionState=portActionState, OperState=OperState)
