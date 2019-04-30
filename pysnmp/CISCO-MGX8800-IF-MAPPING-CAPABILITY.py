#
# PySNMP MIB module CISCO-MGX8800-IF-MAPPING-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MGX8800-IF-MAPPING-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:50:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
Gauge32, ModuleIdentity, TimeTicks, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, iso, Unsigned32, Integer32, ObjectIdentity, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "TimeTicks", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "iso", "Unsigned32", "Integer32", "ObjectIdentity", "IpAddress", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMgx8800IfMappingCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 278))
ciscoMgx8800IfMappingCapability.setRevisions(('2002-08-01 00:00',))
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setLastUpdated('200208010000Z')
if mibBuilder.loadTexts: ciscoMgx8800IfMappingCapability.setOrganization('Cisco Systems, Inc.')
cmiMappingCapabilityMgxV3R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setProductRelease('MGX8850 Release 3.0.00')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityMgxV3R00 = cmiMappingCapabilityMgxV3R00.setStatus('current')
cmiMappingCapabilityRpmxfV12R02 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 278, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setProductRelease('IOS Release 12.2(8)T2.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmiMappingCapabilityRpmxfV12R02 = cmiMappingCapabilityRpmxfV12R02.setStatus('current')
mibBuilder.exportSymbols("CISCO-MGX8800-IF-MAPPING-CAPABILITY", PYSNMP_MODULE_ID=ciscoMgx8800IfMappingCapability, ciscoMgx8800IfMappingCapability=ciscoMgx8800IfMappingCapability, cmiMappingCapabilityMgxV3R00=cmiMappingCapabilityMgxV3R00, cmiMappingCapabilityRpmxfV12R02=cmiMappingCapabilityRpmxfV12R02)
