#
# PySNMP MIB module CISCO-MEGACO-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEGACO-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
ModuleIdentity, ObjectIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Unsigned32, iso, Integer32, Bits, Counter64, IpAddress, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Unsigned32", "iso", "Integer32", "Bits", "Counter64", "IpAddress", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMegacoExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 376))
ciscoMegacoExtCapability.setRevisions(('2004-01-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMegacoExtCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setLastUpdated('200401190000Z')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice-gateway@cisco.com')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setDescription('The agent capabilities for CISCO-MEGACO-EXT-MIB.')
ciscoMegacoExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 376, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setStatus('current')
if mibBuilder.loadTexts: ciscoMegacoExtCapabilityV5R00.setDescription('Megaco extension MIB capabilities for VXSM in release 5.0.0.')
mibBuilder.exportSymbols("CISCO-MEGACO-EXT-CAPABILITY", ciscoMegacoExtCapability=ciscoMegacoExtCapability, PYSNMP_MODULE_ID=ciscoMegacoExtCapability, ciscoMegacoExtCapabilityV5R00=ciscoMegacoExtCapabilityV5R00)
