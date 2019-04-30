#
# PySNMP MIB module CISCO-CONTEXT-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONTEXT-MAPPING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
iso, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, Counter64, NotificationType, MibIdentifier, Gauge32, Counter32, Bits, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "Counter64", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "Bits", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoContextMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 564))
ciscoContextMappingCapability.setRevisions(('2008-08-22 00:00', '2008-03-24 00:00', '2005-05-20 00:00',))
if mibBuilder.loadTexts: ciscoContextMappingCapability.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setOrganization('Cisco Systems, Inc.')
ciscoContextMappingCapV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setStatus('current')
ciscoContextMappingCapV12R02SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setProductRelease('Cisco IOS 12.2SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setStatus('current')
ciscoContextMappingIOSXRV3R7FCICRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setProductRelease('Cisco IOS XR 3.7FCI for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setStatus('current')
mibBuilder.exportSymbols("CISCO-CONTEXT-MAPPING-CAPABILITY", ciscoContextMappingCapV12R02S=ciscoContextMappingCapV12R02S, ciscoContextMappingIOSXRV3R7FCICRS1=ciscoContextMappingIOSXRV3R7FCICRS1, ciscoContextMappingCapV12R02SG=ciscoContextMappingCapV12R02SG, PYSNMP_MODULE_ID=ciscoContextMappingCapability, ciscoContextMappingCapability=ciscoContextMappingCapability)
