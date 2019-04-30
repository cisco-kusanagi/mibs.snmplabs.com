#
# PySNMP MIB module CISCO-RADIUS-ACC-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-ACC-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, IpAddress, ObjectIdentity, Bits, MibIdentifier, TimeTicks, ModuleIdentity, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "IpAddress", "ObjectIdentity", "Bits", "MibIdentifier", "TimeTicks", "ModuleIdentity", "iso", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRadiusAccClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 493))
ciscoRadiusAccClientCapability.setRevisions(('2006-03-06 00:00',))
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setOrganization('Cisco Systems, Inc.')
ciscoRadiusAccClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 493, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAccClientCapV330CRS1 = ciscoRadiusAccClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAccClientCapV330CRS1 = ciscoRadiusAccClientCapV330CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-RADIUS-ACC-CLIENT-CAPABILITY", ciscoRadiusAccClientCapability=ciscoRadiusAccClientCapability, PYSNMP_MODULE_ID=ciscoRadiusAccClientCapability, ciscoRadiusAccClientCapV330CRS1=ciscoRadiusAccClientCapV330CRS1)
