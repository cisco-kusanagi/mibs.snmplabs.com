#
# PySNMP MIB module CISCO-SYSTEM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSTEM-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter32, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, ObjectIdentity, IpAddress, iso, ModuleIdentity, Integer32, MibIdentifier, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "ObjectIdentity", "IpAddress", "iso", "ModuleIdentity", "Integer32", "MibIdentifier", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSysExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 569))
ciscoSysExtCapability.setRevisions(('2008-08-19 00:00', '2005-09-23 00:00',))
if mibBuilder.loadTexts: ciscoSysExtCapability.setLastUpdated('200808190000Z')
if mibBuilder.loadTexts: ciscoSysExtCapability.setOrganization('Cisco Systems, Inc.')
ciscoSysExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setStatus('current')
ciscoSysExtCapabilityGssV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setProductRelease('Global Site Selector(GSS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setStatus('current')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-CAPABILITY", ciscoSysExtCapability=ciscoSysExtCapability, PYSNMP_MODULE_ID=ciscoSysExtCapability, ciscoSysExtCapabilityMDS3R0=ciscoSysExtCapabilityMDS3R0, ciscoSysExtCapabilityGssV02R00=ciscoSysExtCapabilityGssV02R00)
