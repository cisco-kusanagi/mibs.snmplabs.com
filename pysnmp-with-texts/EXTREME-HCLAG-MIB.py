#
# PySNMP MIB module EXTREME-HCLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-HCLAG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:08:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, ModuleIdentity, NotificationType, TimeTicks, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, Bits, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ModuleIdentity", "NotificationType", "TimeTicks", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "Bits", "Gauge32", "MibIdentifier")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
extremeHclag = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 38))
if mibBuilder.loadTexts: extremeHclag.setLastUpdated('1212061000Z')
if mibBuilder.loadTexts: extremeHclag.setOrganization('Extreme Networks, Inc.')
if mibBuilder.loadTexts: extremeHclag.setContactInfo('www.extremenetworks.com')
if mibBuilder.loadTexts: extremeHclag.setDescription('Ethernet Health Check Link-Aggregation')
class HclagGroupId(DisplayString):
    description = 'This represents the Health Check LAG group id.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class HclagMemberPort(TextualConvention, Unsigned32):
    description = "This represents a Health Check LAG's member-port."
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeHclagTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1), )
if mibBuilder.loadTexts: extremeHclagTable.setStatus('current')
if mibBuilder.loadTexts: extremeHclagTable.setDescription('This table contains HCLAG information about all Health Check LAGs on this device.')
extremeHclagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1), ).setIndexNames((0, "EXTREME-HCLAG-MIB", "extremeHclagGroup"), (0, "EXTREME-HCLAG-MIB", "extremeHclagMemberPort"))
if mibBuilder.loadTexts: extremeHclagEntry.setStatus('current')
if mibBuilder.loadTexts: extremeHclagEntry.setDescription('An individual entry of this table contains information related to that Health Check LAG.')
extremeHclagGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 1), HclagGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagGroup.setStatus('current')
if mibBuilder.loadTexts: extremeHclagGroup.setDescription("This represents the LAG (Link Aggregation Group's) identifier.")
extremeHclagMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 2), HclagMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagMemberPort.setStatus('current')
if mibBuilder.loadTexts: extremeHclagMemberPort.setDescription('This represents a member port within the LAG.')
extremeHclagAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagAdminState.setStatus('current')
if mibBuilder.loadTexts: extremeHclagAdminState.setDescription('This represents if the member port has been enabled for health checking')
extremeHclagLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagLinkState.setStatus('current')
if mibBuilder.loadTexts: extremeHclagLinkState.setDescription('This represents state of member ports physical link.')
extremeHclagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagStatus.setStatus('current')
if mibBuilder.loadTexts: extremeHclagStatus.setDescription('This represents if the member port has been added to the aggregator or not.')
mibBuilder.exportSymbols("EXTREME-HCLAG-MIB", HclagGroupId=HclagGroupId, PYSNMP_MODULE_ID=extremeHclag, extremeHclag=extremeHclag, HclagMemberPort=HclagMemberPort, extremeHclagStatus=extremeHclagStatus, extremeHclagEntry=extremeHclagEntry, extremeHclagGroup=extremeHclagGroup, extremeHclagMemberPort=extremeHclagMemberPort, extremeHclagTable=extremeHclagTable, extremeHclagLinkState=extremeHclagLinkState, extremeHclagAdminState=extremeHclagAdminState)
