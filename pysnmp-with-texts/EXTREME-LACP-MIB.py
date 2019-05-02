#
# PySNMP MIB module EXTREME-LACP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-LACP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:08:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, Bits, Integer32, ObjectIdentity, MibIdentifier, Unsigned32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "Unsigned32", "ModuleIdentity", "IpAddress")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
extremeLacp = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 19))
if mibBuilder.loadTexts: extremeLacp.setLastUpdated('0502151530Z')
if mibBuilder.loadTexts: extremeLacp.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeLacp.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeLacp.setDescription('Ethernet Automatic Protection Switching information.')
class LacpGroupId(DisplayString):
    description = "This represents the LACP's LAG group id."
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class LacpMemberPort(TextualConvention, Unsigned32):
    description = "This represents a LACP LAG's member-port."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeLacpTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1), )
if mibBuilder.loadTexts: extremeLacpTable.setStatus('current')
if mibBuilder.loadTexts: extremeLacpTable.setDescription('This table contains LACP information about all LACP LAGs on this device.')
extremeLacpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1), ).setIndexNames((0, "EXTREME-LACP-MIB", "extremeLacpGroup"), (0, "EXTREME-LACP-MIB", "extremeLacpMemberPort"))
if mibBuilder.loadTexts: extremeLacpEntry.setStatus('current')
if mibBuilder.loadTexts: extremeLacpEntry.setDescription('An individual entry of this table contains LACP information related to that LACP LAG.')
extremeLacpGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 1), LacpGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpGroup.setStatus('current')
if mibBuilder.loadTexts: extremeLacpGroup.setDescription("This represents the LACP LAG (Link Aggregation Group's) identifier.")
extremeLacpMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 2), LacpMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpMemberPort.setStatus('current')
if mibBuilder.loadTexts: extremeLacpMemberPort.setDescription('This represents a member port within the LAG.')
extremeLacpAggStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 19, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeLacpAggStatus.setStatus('current')
if mibBuilder.loadTexts: extremeLacpAggStatus.setDescription('This represents if the member port has been added to the aggregator or not.')
mibBuilder.exportSymbols("EXTREME-LACP-MIB", extremeLacpGroup=extremeLacpGroup, extremeLacpMemberPort=extremeLacpMemberPort, PYSNMP_MODULE_ID=extremeLacp, extremeLacpEntry=extremeLacpEntry, LacpGroupId=LacpGroupId, extremeLacp=extremeLacp, LacpMemberPort=LacpMemberPort, extremeLacpAggStatus=extremeLacpAggStatus, extremeLacpTable=extremeLacpTable)
