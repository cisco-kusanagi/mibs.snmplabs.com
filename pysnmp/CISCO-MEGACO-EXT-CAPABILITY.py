#
# PySNMP MIB module CISCO-MEGACO-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MEGACO-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, NotificationType, Integer32, Gauge32, IpAddress, Counter32, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "NotificationType", "Integer32", "Gauge32", "IpAddress", "Counter32", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMegacoExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 376))
ciscoMegacoExtCapability.setRevisions(('2004-01-19 00:00',))
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setLastUpdated('200401190000Z')
if mibBuilder.loadTexts: ciscoMegacoExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoMegacoExtCapabilityV5R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 376, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setProductRelease('MGX8850 Release 5.0.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMegacoExtCapabilityV5R00 = ciscoMegacoExtCapabilityV5R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-MEGACO-EXT-CAPABILITY", ciscoMegacoExtCapability=ciscoMegacoExtCapability, PYSNMP_MODULE_ID=ciscoMegacoExtCapability, ciscoMegacoExtCapabilityV5R00=ciscoMegacoExtCapabilityV5R00)
