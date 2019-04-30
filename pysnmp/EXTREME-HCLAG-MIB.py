#
# PySNMP MIB module EXTREME-HCLAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-HCLAG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Unsigned32, Gauge32, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, NotificationType, Bits, ModuleIdentity, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Unsigned32", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "NotificationType", "Bits", "ModuleIdentity", "IpAddress", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
extremeHclag = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 38))
if mibBuilder.loadTexts: extremeHclag.setLastUpdated('1212061000Z')
if mibBuilder.loadTexts: extremeHclag.setOrganization('Extreme Networks, Inc.')
class HclagGroupId(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 32)

class HclagMemberPort(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

extremeHclagTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1), )
if mibBuilder.loadTexts: extremeHclagTable.setStatus('current')
extremeHclagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1), ).setIndexNames((0, "EXTREME-HCLAG-MIB", "extremeHclagGroup"), (0, "EXTREME-HCLAG-MIB", "extremeHclagMemberPort"))
if mibBuilder.loadTexts: extremeHclagEntry.setStatus('current')
extremeHclagGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 1), HclagGroupId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagGroup.setStatus('current')
extremeHclagMemberPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 2), HclagMemberPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagMemberPort.setStatus('current')
extremeHclagAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagAdminState.setStatus('current')
extremeHclagLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagLinkState.setStatus('current')
extremeHclagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 38, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeHclagStatus.setStatus('current')
mibBuilder.exportSymbols("EXTREME-HCLAG-MIB", HclagMemberPort=HclagMemberPort, PYSNMP_MODULE_ID=extremeHclag, extremeHclagMemberPort=extremeHclagMemberPort, extremeHclag=extremeHclag, extremeHclagStatus=extremeHclagStatus, HclagGroupId=HclagGroupId, extremeHclagLinkState=extremeHclagLinkState, extremeHclagAdminState=extremeHclagAdminState, extremeHclagTable=extremeHclagTable, extremeHclagGroup=extremeHclagGroup, extremeHclagEntry=extremeHclagEntry)
