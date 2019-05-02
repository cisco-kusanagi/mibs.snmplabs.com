#
# PySNMP MIB module CISCO-RADIUS-AUTH-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-AUTH-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Gauge32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, Bits, IpAddress, MibIdentifier, ObjectIdentity, iso, TimeTicks, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "Bits", "IpAddress", "MibIdentifier", "ObjectIdentity", "iso", "TimeTicks", "Unsigned32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRadiusAuthClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 494))
ciscoRadiusAuthClientCapability.setRevisions(('2006-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-radius@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapability.setDescription('The capabilities description of RADIUS-AUTH-CLIENT-MIB')
ciscoRadiusAuthClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 494, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAuthClientCapV330CRS1 = ciscoRadiusAuthClientCapV330CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusAuthClientCapV330CRS1.setDescription('RADIUS-AUTH-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RADIUS-AUTH-CLIENT-CAPABILITY", ciscoRadiusAuthClientCapV330CRS1=ciscoRadiusAuthClientCapV330CRS1, PYSNMP_MODULE_ID=ciscoRadiusAuthClientCapability, ciscoRadiusAuthClientCapability=ciscoRadiusAuthClientCapability)
