#
# PySNMP MIB module NV-ATKK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NV-ATKK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, NotificationType, Counter32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, mib_2, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, MibIdentifier, Integer32, Bits, enterprises, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Counter32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "mib-2", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "MibIdentifier", "Integer32", "Bits", "enterprises", "Unsigned32")
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
if mibBuilder.loadTexts: atiSysSerialno.setDescription('Serial number.')
atiSysTftpIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysTftpIPAddress.setDescription('TFTP Server IP address.')
atiSysTftpFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysTftpFilename.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysTftpFilename.setDescription('TFTP file name.')
atiSysPowerupCount = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiSysPowerupCount.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysPowerupCount.setDescription('Powerup Count.')
atiSysBrcastCutoffRate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysBrcastCutoffRate.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysBrcastCutoffRate.setDescription('Broadcast Cutoff Rate. (0..100000)')
atiSysGatewayIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSysGatewayIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSysGatewayIPAddress.setDescription('Gateway IP address.')
atiPortTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 3, 2), )
if mibBuilder.loadTexts: atiPortTable.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortTable.setDescription('The port setup table.')
atiPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1), ).setIndexNames((0, "NV-ATKK-MIB", "atiPort"))
if mibBuilder.loadTexts: atiPortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortEntry.setDescription('The port setup entry.')
atiPort = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPort.setStatus('mandatory')
if mibBuilder.loadTexts: atiPort.setDescription('A number from 1 to number of ports on the switch.')
atiPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortStatus.setDescription('Port status.')
atiPortDuplexStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half", 1), ("full", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortDuplexStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortDuplexStatus.setDescription('Port duplex status.')
atiPortForwardedFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortForwardedFrames.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortForwardedFrames.setDescription('Number of frames received on this port and forwarded to another port on the system module for processing.')
atiPortRcvdLocalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atiPortRcvdLocalFrames.setStatus('mandatory')
if mibBuilder.loadTexts: atiPortRcvdLocalFrames.setDescription('Number of frames received where the destination is on this port.')
atiSwitchIPAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchIPAddress.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchIPAddress.setDescription('Since bridges can now be accessed without an IP address, there needs to be a way to find out there addresses.')
atiSwitchSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchSubnetMask.setDescription("The switch's submask.")
atiActiveAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiActiveAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: atiActiveAgingTime.setDescription('Active Aging Time.')
atiPurgeAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPurgeAgingTime.setStatus('mandatory')
if mibBuilder.loadTexts: atiPurgeAgingTime.setDescription('Purge Aging Time.')
atiSwitchSTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchSTPStatus.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchSTPStatus.setDescription("The switch's Spanning Tree status, enter ON or OFF.")
atiSwitchManager = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitchManager.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitchManager.setDescription('The 1th SNMP Trap Destination.')
atiSwitcTrapRcvr1 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr1.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitcTrapRcvr1.setDescription('The 1th SNMP Trap Destination.')
atiSwitcTrapRcvr2 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr2.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitcTrapRcvr2.setDescription('The 2th SNMP Trap Destination.')
atiSwitcTrapRcvr3 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr3.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitcTrapRcvr3.setDescription('The 3th SNMP Trap Destination.')
atiSwitcTrapRcvr4 = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 3, 3, 6, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiSwitcTrapRcvr4.setStatus('mandatory')
if mibBuilder.loadTexts: atiSwitcTrapRcvr4.setDescription('The 4th SNMP Trap Destination.')
mibBuilder.exportSymbols("NV-ATKK-MIB", atiSysSerialno=atiSysSerialno, atiPortForwardedFrames=atiPortForwardedFrames, atiSwitcTrapRcvr2=atiSwitcTrapRcvr2, atiSwitchSubnetMask=atiSwitchSubnetMask, atiSwitchSTPStatus=atiSwitchSTPStatus, atiSwitch=atiSwitch, atiSwitchManager=atiSwitchManager, c3716TR=c3716TR, atiPortDuplexStatus=atiPortDuplexStatus, atiSwitcTrapRcvr1=atiSwitcTrapRcvr1, atiPortTable=atiPortTable, atiSwitchIPAddress=atiSwitchIPAddress, atiSwitcTrapRcvr4=atiSwitcTrapRcvr4, Timeout=Timeout, atiSysGatewayIPAddress=atiSysGatewayIPAddress, atiSwitcTrapRcvr3=atiSwitcTrapRcvr3, atiSysPowerupCount=atiSysPowerupCount, MacAddress=MacAddress, BridgeId=BridgeId, atiSysTftpIPAddress=atiSysTftpIPAddress, atiPortRcvdLocalFrames=atiPortRcvdLocalFrames, atiSysTftpFilename=atiSysTftpFilename, atiPortStatus=atiPortStatus, atiSysBrcastCutoffRate=atiSysBrcastCutoffRate, atiPurgeAgingTime=atiPurgeAgingTime, atiPortEntry=atiPortEntry, atiActiveAgingTime=atiActiveAgingTime, atiPort=atiPort, atiSystemConfig=atiSystemConfig)
