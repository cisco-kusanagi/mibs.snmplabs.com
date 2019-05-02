#
# PySNMP MIB module CISCO-RADIUS-ACC-CLIENT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RADIUS-ACC-CLIENT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:10:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Counter64, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, TimeTicks, Counter32, NotificationType, ModuleIdentity, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "TimeTicks", "Counter32", "NotificationType", "ModuleIdentity", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRadiusAccClientCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 493))
ciscoRadiusAccClientCapability.setRevisions(('2006-03-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setLastUpdated('200603060000Z')
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-radius@cisco.com')
if mibBuilder.loadTexts: ciscoRadiusAccClientCapability.setDescription('The capabilities description of RADIUS-ACC-CLIENT-MIB')
ciscoRadiusAccClientCapV330CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 493, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAccClientCapV330CRS1 = ciscoRadiusAccClientCapV330CRS1.setProductRelease('Cisco IOS XR release 3.3.0 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoRadiusAccClientCapV330CRS1 = ciscoRadiusAccClientCapV330CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoRadiusAccClientCapV330CRS1.setDescription('RADIUS-ACC-CLIENT-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-RADIUS-ACC-CLIENT-CAPABILITY", ciscoRadiusAccClientCapV330CRS1=ciscoRadiusAccClientCapV330CRS1, PYSNMP_MODULE_ID=ciscoRadiusAccClientCapability, ciscoRadiusAccClientCapability=ciscoRadiusAccClientCapability)
