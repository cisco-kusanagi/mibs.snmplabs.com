#
# PySNMP MIB module NV-ATKK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NV-ATKK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:16:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Unsigned32, ObjectIdentity, Counter32, NotificationType, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Counter64, enterprises, NotificationType, ModuleIdentity, IpAddress, Gauge32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter32", "NotificationType", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Counter64", "enterprises", "NotificationType", "ModuleIdentity", "IpAddress", "Gauge32", "Bits", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

c3716TR = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3))
atiSystemConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3, 1))
atiSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 3, 3))
atiSysSerialno = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiSysSerialno.setStatus('mandatory')
atiSysTftpIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpIPAddress.setStatus('mandatory')
atiSysTftpFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpFilename.setStatus('mandatory')
atiSysPowerupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiSysPowerupCount.setStatus('mandatory')
atiSysBrcastCutoffRate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysBrcastCutoffRate.setStatus('mandatory')
atiSysGatewayIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysGatewayIPAddress.setStatus('mandatory')
atiPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 3, 2), )
if mibBuilder.loadTexts: atiPortTable.setStatus('mandatory')
atiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1), ).setIndexNames((0, "NV-ATKK-MIB", "atiPort"))
if mibBuilder.loadTexts: atiPortEntry.setStatus('mandatory')
atiPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPort.setStatus('mandatory')
atiPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortStatus.setStatus('mandatory')
atiPortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortDuplexStatus.setStatus('mandatory')
atiPortForwardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortForwardedFrames.setStatus('mandatory')
atiPortRcvdLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortRcvdLocalFrames.setStatus('mandatory')
atiSwitchIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchIPAddress.setStatus('mandatory')
atiSwitchSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSubnetMask.setStatus('mandatory')
atiActiveAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiActiveAgingTime.setStatus('mandatory')
atiPurgeAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPurgeAgingTime.setStatus('mandatory')
atiSwitchSTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSTPStatus.setStatus('mandatory')
atiSwitchManager = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchManager.setStatus('mandatory')
atiSwitcTrapRcvr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr1.setStatus('mandatory')
atiSwitcTrapRcvr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr2.setStatus('mandatory')
atiSwitcTrapRcvr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr3.setStatus('mandatory')
atiSwitcTrapRcvr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr4.setStatus('mandatory')
mibBuilder.exportSymbols("NV-ATKK-MIB", atiPortStatus=atiPortStatus, atiPurgeAgingTime=atiPurgeAgingTime, atiSwitcTrapRcvr4=atiSwitcTrapRcvr4, MacAddress=MacAddress, atiPortTable=atiPortTable, atiSwitch=atiSwitch, atiSwitcTrapRcvr1=atiSwitcTrapRcvr1, atiPortEntry=atiPortEntry, atiSystemConfig=atiSystemConfig, atiSwitchIPAddress=atiSwitchIPAddress, atiSwitchSubnetMask=atiSwitchSubnetMask, atiSysGatewayIPAddress=atiSysGatewayIPAddress, atiPortRcvdLocalFrames=atiPortRcvdLocalFrames, c3716TR=c3716TR, atiPortForwardedFrames=atiPortForwardedFrames, atiSysSerialno=atiSysSerialno, atiSwitcTrapRcvr2=atiSwitcTrapRcvr2, atiSwitcTrapRcvr3=atiSwitcTrapRcvr3, Timeout=Timeout, atiPort=atiPort, atiSysTftpIPAddress=atiSysTftpIPAddress, atiSysPowerupCount=atiSysPowerupCount, BridgeId=BridgeId, atiActiveAgingTime=atiActiveAgingTime, atiSysTftpFilename=atiSysTftpFilename, atiSysBrcastCutoffRate=atiSysBrcastCutoffRate, atiSwitchManager=atiSwitchManager, atiSwitchSTPStatus=atiSwitchSTPStatus, atiPortDuplexStatus=atiPortDuplexStatus)
