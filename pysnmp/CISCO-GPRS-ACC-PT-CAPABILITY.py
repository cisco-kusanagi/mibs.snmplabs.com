#
# PySNMP MIB module CISCO-GPRS-ACC-PT-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GPRS-ACC-PT-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, AgentCapabilities, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "AgentCapabilities", "ModuleCompliance")
Bits, NotificationType, Gauge32, Counter32, IpAddress, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, iso, MibIdentifier, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cgprsAccPtCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 298))
cgprsAccPtCapability.setRevisions(('2003-04-08 17:50',))
if mibBuilder.loadTexts: cgprsAccPtCapability.setLastUpdated('200304081750Z')
if mibBuilder.loadTexts: cgprsAccPtCapability.setOrganization('Cisco Systems, Inc.')
cgprsAccPtCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX & 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M4 = cgprsAccPtCapabilityV12R2M4.setStatus('current')
cgprsAccPtCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 298, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cgprsAccPtCapabilityV12R2M8 = cgprsAccPtCapabilityV12R2M8.setStatus('current')
mibBuilder.exportSymbols("CISCO-GPRS-ACC-PT-CAPABILITY", cgprsAccPtCapability=cgprsAccPtCapability, cgprsAccPtCapabilityV12R2M4=cgprsAccPtCapabilityV12R2M4, PYSNMP_MODULE_ID=cgprsAccPtCapability, cgprsAccPtCapabilityV12R2M8=cgprsAccPtCapabilityV12R2M8)
