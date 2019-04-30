#
# PySNMP MIB module EICON-MIB-PORT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EICON-MIB-PORT
# Produced by pysmi-0.3.4 at Mon Apr 29 18:45:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, ObjectIdentity, Unsigned32, Gauge32, NotificationType, Bits, Integer32, Counter32, MibIdentifier, IpAddress, TimeTicks, NotificationType, iso, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Gauge32", "NotificationType", "Bits", "Integer32", "Counter32", "MibIdentifier", "IpAddress", "TimeTicks", "NotificationType", "iso", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
portTable = MibTable((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2), )
if mibBuilder.loadTexts: portTable.setStatus('mandatory')
portEntry = MibTableRow((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1), ).setIndexNames((0, "EICON-MIB-PORT", "portIndex"))
if mibBuilder.loadTexts: portEntry.setStatus('mandatory')
portIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 1), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portIndex.setStatus('mandatory')
portLanaNo = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 2), PortRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portLanaNo.setStatus('mandatory')
portName = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 3), PortName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portName.setStatus('mandatory')
portCardLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 4), CardRef()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portCardLocation.setStatus('mandatory')
portDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portDescription.setStatus('mandatory')
portOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 6), OperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOperState.setStatus('mandatory')
portAdminStateCtr = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 7), AdminState()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: portAdminStateCtr.setStatus('mandatory')
portOpenTime = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portOpenTime.setStatus('mandatory')
portProtocols = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portProtocols.setStatus('mandatory')
portDialerType = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("direct", 1), ("v25bis", 2), ("v22bis", 3), ("at-cmd", 4), ("isdn-stat", 5), ("v32bis", 6), ("none", 7), ("other", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portDialerType.setStatus('mandatory')
portActionState = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 11), ActionState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: portActionState.setStatus('mandatory')
portActionError = MibTableColumn((1, 3, 6, 1, 4, 1, 434, 2, 2, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("no-error", 0), ("err-WARNING", 1), ("err-PARTIAL", 2), ("err-ABORT", 3), ("err-FAILED", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: portActionError.setStatus('mandatory')
portTrapStateChange = NotificationType((1, 3, 6, 1, 4, 1, 434) + (0,31)).setObjects(("SNMPv2-MIB", "sysName"), ("EICON-MIB-PORT", "portIndex"), ("EICON-MIB-PORT", "portOperState"))
mibBuilder.exportSymbols("EICON-MIB-PORT", portActionState=portActionState, portOpenTime=portOpenTime, portEntry=portEntry, portIndex=portIndex, portCardLocation=portCardLocation, portLanaNo=portLanaNo, AdminState=AdminState, portName=portName, CardRef=CardRef, portDialerType=portDialerType, portOperState=portOperState, PortRef=PortRef, OperState=OperState, PositiveInteger=PositiveInteger, portTable=portTable, eicon=eicon, PortName=PortName, management=management, portAdminStateCtr=portAdminStateCtr, mibv2=mibv2, module=module, portTrapStateChange=portTrapStateChange, ActionState=ActionState, portNumberOfPorts=portNumberOfPorts, portProtocols=portProtocols, portActionError=portActionError, portDescription=portDescription, port=port)
