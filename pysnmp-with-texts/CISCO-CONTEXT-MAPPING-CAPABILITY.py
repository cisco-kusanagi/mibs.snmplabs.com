#
# PySNMP MIB module CISCO-CONTEXT-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-CONTEXT-MAPPING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:53:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
Counter32, MibIdentifier, ModuleIdentity, TimeTicks, Counter64, NotificationType, ObjectIdentity, Integer32, Gauge32, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoContextMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 564))
ciscoContextMappingCapability.setRevisions(('2008-08-22 00:00', '2008-03-24 00:00', '2005-05-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoContextMappingCapability.setRevisionsDescriptions(('Added ciscoContextMappingIOSXRV3R7FCICRS1', 'Added ciscoContextMappingCapV12R02SG', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoContextMappingCapability.setLastUpdated('200808220000Z')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoContextMappingCapability.setDescription('Agent capabilities for the CISCO-CONTEXT-MAPPING-MIB.')
ciscoContextMappingCapV12R02S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setProductRelease('Cisco IOS 12.2S')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02S = ciscoContextMappingCapV12R02S.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingCapV12R02S.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
ciscoContextMappingCapV12R02SG = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setProductRelease('Cisco IOS 12.2SG')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingCapV12R02SG = ciscoContextMappingCapV12R02SG.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingCapV12R02SG.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
ciscoContextMappingIOSXRV3R7FCICRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 564, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setProductRelease('Cisco IOS XR 3.7FCI for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoContextMappingIOSXRV3R7FCICRS1 = ciscoContextMappingIOSXRV3R7FCICRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoContextMappingIOSXRV3R7FCICRS1.setDescription('CISCO-CONTEXT-MAPPING-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-CONTEXT-MAPPING-CAPABILITY", ciscoContextMappingCapability=ciscoContextMappingCapability, ciscoContextMappingCapV12R02SG=ciscoContextMappingCapV12R02SG, ciscoContextMappingCapV12R02S=ciscoContextMappingCapV12R02S, PYSNMP_MODULE_ID=ciscoContextMappingCapability, ciscoContextMappingIOSXRV3R7FCICRS1=ciscoContextMappingIOSXRV3R7FCICRS1)
