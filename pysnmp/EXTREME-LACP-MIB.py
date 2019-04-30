#
# PySNMP MIB module EXTREME-LACP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-LACP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:54:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, Counter64, ObjectIdentity, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Gauge32, Counter32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "Counter64", "ObjectIdentity", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Gauge32", "Counter32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
extremeLacp = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 19))
if mibBuilder.loadTexts: extremeLacp.setLastUpdated('0502151530Z')
if mibBuilder.loadTexts: extremeLacp.setOrganization('Extreme Networks, Inc.')
class LacpGroupId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class LacpMemberPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeLacpTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1), )
if mibBuilder.loadTexts: extremeLacpTable.setStatus('current')
extremeLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1), ).setIndexNames((0, "EXTREME-LACP-MIB", "extremeLacpGroup"), (0, "EXTREME-LACP-MIB", "extremeLacpMemberPort"))
if mibBuilder.loadTexts: extremeLacpEntry.setStatus('current')
extremeLacpGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 1), LacpGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpGroup.setStatus('current')
extremeLacpMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 2), LacpMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpMemberPort.setStatus('current')
extremeLacpAggStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpAggStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-LACP-MIB", extremeLacpGroup=extremeLacpGroup, LacpGroupId=LacpGroupId, extremeLacpAggStatus=extremeLacpAggStatus, extremeLacpEntry=extremeLacpEntry, extremeLacpTable=extremeLacpTable, LacpMemberPort=LacpMemberPort, extremeLacpMemberPort=extremeLacpMemberPort, PYSNMP_MODULE_ID=extremeLacp, extremeLacp=extremeLacp)
