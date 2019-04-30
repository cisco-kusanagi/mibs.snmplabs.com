#
# PySNMP MIB module CISCO-WAN-MODULE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-MODULE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 18:04:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ciscoWanAgentCapability, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWanAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
ModuleIdentity, iso, Integer32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Integer32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoWanModuleCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 160, 99999))
ciscoWanModuleCapability.setRevisions(('2002-03-06 00:00',))
if mibBuilder.loadTexts: ciscoWanModuleCapability.setLastUpdated('200203060000Z')
if mibBuilder.loadTexts: ciscoWanModuleCapability.setOrganization('Cisco Systems, Inc.')
ciscoWanModuleCapabilityV2R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 99999, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV2R00 = ciscoWanModuleCapabilityV2R00.setProductRelease('MGX8850 Release 2.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV2R00 = ciscoWanModuleCapabilityV2R00.setStatus('current')
ciscoWanModuleCapabilityV21R60 = AgentCapabilities((1, 3, 6, 1, 4, 1, 351, 160, 99999, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV21R60 = ciscoWanModuleCapabilityV21R60.setProductRelease('MGX8850 Release 2.1.60')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoWanModuleCapabilityV21R60 = ciscoWanModuleCapabilityV21R60.setStatus('current')
mibBuilder.exportSymbols("CISCO-WAN-MODULE-CAPABILITY", ciscoWanModuleCapability=ciscoWanModuleCapability, PYSNMP_MODULE_ID=ciscoWanModuleCapability, ciscoWanModuleCapabilityV2R00=ciscoWanModuleCapabilityV2R00, ciscoWanModuleCapabilityV21R60=ciscoWanModuleCapabilityV21R60)
