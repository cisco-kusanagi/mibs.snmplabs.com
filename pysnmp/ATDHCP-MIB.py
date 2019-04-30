#
# PySNMP MIB module ATDHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATDHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
alliedTelesyn, atiProduct, atswitchMib, mibObject = mibBuilder.importSymbols("ATSWTCH2-MIB", "alliedTelesyn", "atiProduct", "atswitchMib", "mibObject")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, enterprises, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Unsigned32, MibIdentifier, IpAddress, Integer32, TimeTicks, Gauge32, ModuleIdentity, NotificationType, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "enterprises", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Unsigned32", "MibIdentifier", "IpAddress", "Integer32", "TimeTicks", "Gauge32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Timeout(Integer32):
    pass

atswitchDHCPGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11))
atswitchDHCPSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1))
atswitchDHCPTimerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2))
atswitchDHCPCurrentDHCPClientAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPCurrentDHCPClientAddress.setStatus('mandatory')
atswitchDHCPSubnetMask = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPSubnetMask.setStatus('mandatory')
atswitchDHCPCurrentRelayAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPCurrentRelayAgentAddress.setStatus('mandatory')
atswitchDHCPNextDHCPServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPNextDHCPServerAddress.setStatus('mandatory')
atswitchDHCPLeaseTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPLeaseTimer.setStatus('mandatory')
atswitchDHCPReacquisitionTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPReacquisitionTimer.setStatus('mandatory')
atswitchDHCPExpirationTimer = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atswitchDHCPExpirationTimer.setStatus('mandatory')
mibBuilder.exportSymbols("ATDHCP-MIB", Timeout=Timeout, atswitchDHCPCurrentDHCPClientAddress=atswitchDHCPCurrentDHCPClientAddress, atswitchDHCPSysGroup=atswitchDHCPSysGroup, atswitchDHCPGroup=atswitchDHCPGroup, atswitchDHCPLeaseTimer=atswitchDHCPLeaseTimer, atswitchDHCPCurrentRelayAgentAddress=atswitchDHCPCurrentRelayAgentAddress, atswitchDHCPNextDHCPServerAddress=atswitchDHCPNextDHCPServerAddress, atswitchDHCPReacquisitionTimer=atswitchDHCPReacquisitionTimer, BridgeId=BridgeId, atswitchDHCPExpirationTimer=atswitchDHCPExpirationTimer, atswitchDHCPSubnetMask=atswitchDHCPSubnetMask, MacAddress=MacAddress, atswitchDHCPTimerGroup=atswitchDHCPTimerGroup)
