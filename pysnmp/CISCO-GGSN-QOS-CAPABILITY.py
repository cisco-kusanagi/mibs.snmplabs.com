#
# PySNMP MIB module CISCO-GGSN-QOS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-GGSN-QOS-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, TimeTicks, ModuleIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Gauge32, Counter32, iso, IpAddress, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Gauge32", "Counter32", "iso", "IpAddress", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoGgsnQosCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 295))
ciscoGgsnQosCapability.setRevisions(('2003-04-08 16:00',))
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setLastUpdated('200304081600Z')
if mibBuilder.loadTexts: ciscoGgsnQosCapability.setOrganization('Cisco Systems, Inc.')
ciscoGgsnQosCapabilityV12R2M4 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setProductRelease('Cisco IOS 12.2(4)MX, 12.2(8)YY')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M4 = ciscoGgsnQosCapabilityV12R2M4.setStatus('current')
ciscoGgsnQosCapabilityV12R2M8 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 295, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setProductRelease('Cisco IOS 12.2(8)YW')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGgsnQosCapabilityV12R2M8 = ciscoGgsnQosCapabilityV12R2M8.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-QOS-CAPABILITY", PYSNMP_MODULE_ID=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M8=ciscoGgsnQosCapabilityV12R2M8, ciscoGgsnQosCapability=ciscoGgsnQosCapability, ciscoGgsnQosCapabilityV12R2M4=ciscoGgsnQosCapabilityV12R2M4)
