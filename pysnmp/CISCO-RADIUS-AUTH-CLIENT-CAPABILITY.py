#
# PySNMP MIB module CISCO-RADIUS-AUTH-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-AUTH-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:53:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, Gauge32, IpAddress, ObjectIdentity, Counter64, Bits, NotificationType, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "IpAddress", "ObjectIdentity", "Counter64", "Bits", "NotificationType", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRadiusAuthClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 494))
ciscoRadiusAuthClientCapability.setRevisions(('2006-03-06 00:00',))
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setOrganization('Cisco Systems, Inc.')
ciscoRadiusAuthClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 494, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-RADIUS-AUTH-CLIENT-CAPABILITY", ciscoRadiusAuthClientCapability=ciscoRadiusAuthClientCapability, PYSNMP_MODULE_ID=ciscoRadiusAuthClientCapability, ciscoRadiusAuthClientCapV330CRS1=ciscoRadiusAuthClientCapV330CRS1)
