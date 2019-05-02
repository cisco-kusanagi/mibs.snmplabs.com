#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX8800-IF-MAPPING-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:07:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
TimeTicks, ModuleIdentity, Unsigned32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Bits, MibIdentifier, Counter32, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Unsigned32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Bits", "MibIdentifier", "Counter32", "ObjectIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMgx8800IfMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 278))
ciscoMgx8800IfMappingCapability.setRevisions(('2002-08-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setLastUpdated('200208010000Z')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-wanatm@cisco.com')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setDescription('The Agent Capabilities for CISCO-MGX8800-IF-MAPPING-MIB. - The cmiMappingCapabilityMgxV3R00 is for MGX8850 Release 3.0.00. - The cmiMappingCapabilityRpmxfV12R02 is for RPM-XF module.')
cmiMappingCapabilityMgxV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setStatus('current')
if mibBuilder.loadTexts: cmiMappingCapabilityMgxV3R00.setDescription('Agent capabilities for MGX8850.')
cmiMappingCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2(8)T2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setStatus('current')
if mibBuilder.loadTexts: cmiMappingCapabilityRpmxfV12R02.setDescription('Agent capabilities for RPM-XF module.')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-CAPABILITY", ciscoMgx8800IfMappingCapability=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityMgxV3R00=cmiMappingCapabilityMgxV3R00, PYSNMP_MODULE_ID=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityRpmxfV12R02=cmiMappingCapabilityRpmxfV12R02)
