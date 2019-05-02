#
# PySNMP MIB module CISCO-SYSTEM-EXT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SYSTEM-EXT-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:13:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, Counter64, ObjectIdentity, NotificationType, Unsigned32, TimeTicks, IpAddress, Integer32, Gauge32, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks", "IpAddress", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoSysExtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 569))
ciscoSysExtCapability.setRevisions(('2008-08-19 00:00', '2005-09-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoSysExtCapability.setRevisionsDescriptions(('Added ciscoSysExtCapabilityGssV02R00 agent capabilities for Global Site Selector(GSS) release 2.0.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: ciscoSysExtCapability.setLastUpdated('200808190000Z')
if mibBuilder.loadTexts: ciscoSysExtCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoSysExtCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-san@cisco.com')
if mibBuilder.loadTexts: ciscoSysExtCapability.setDescription('Agent capabilities for CISCO-SYSTEM-EXT-MIB.')
ciscoSysExtCapabilityMDS3R0 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setProductRelease('Cisco MDS 3.0(1)')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityMDS3R0 = ciscoSysExtCapabilityMDS3R0.setStatus('current')
if mibBuilder.loadTexts: ciscoSysExtCapabilityMDS3R0.setDescription('Cisco System Extension MIB capabilities.')
ciscoSysExtCapabilityGssV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 569, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setProductRelease('Global Site Selector(GSS) 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSysExtCapabilityGssV02R00 = ciscoSysExtCapabilityGssV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoSysExtCapabilityGssV02R00.setDescription('GSS 2.0 CISCO-SYSTEM-EXT-MIB capabilities')
mibBuilder.exportSymbols("CISCO-SYSTEM-EXT-CAPABILITY", ciscoSysExtCapabilityGssV02R00=ciscoSysExtCapabilityGssV02R00, ciscoSysExtCapability=ciscoSysExtCapability, ciscoSysExtCapabilityMDS3R0=ciscoSysExtCapabilityMDS3R0, PYSNMP_MODULE_ID=ciscoSysExtCapability)
