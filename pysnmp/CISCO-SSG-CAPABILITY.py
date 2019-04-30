#
# PySNMP MIB module CISCO-SSG-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SSG-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, Integer32, Counter32, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, iso, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "Integer32", "Counter32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "iso", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSsgCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 1500))
ciscoSsgCapability.setRevisions(('2004-08-13 00:00',))
if mibBuilder.loadTexts: ciscoSsgCapability.setLastUpdated('200408130000Z')
if mibBuilder.loadTexts: ciscoSsgCapability.setOrganization('Cisco Systems, Inc.')
ciscoSsgCapabilityV12R03RevT = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 1500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setProductRelease('Cisco IOS 12.3T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSsgCapabilityV12R03RevT = ciscoSsgCapabilityV12R03RevT.setStatus('current')
mibBuilder.exportSymbols("CISCO-SSG-CAPABILITY", ciscoSsgCapabilityV12R03RevT=ciscoSsgCapabilityV12R03RevT, PYSNMP_MODULE_ID=ciscoSsgCapability, ciscoSsgCapability=ciscoSsgCapability)
