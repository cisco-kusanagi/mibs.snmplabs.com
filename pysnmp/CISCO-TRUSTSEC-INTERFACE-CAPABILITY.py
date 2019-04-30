#
# PySNMP MIB module CISCO-TRUSTSEC-INTERFACE-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-INTERFACE-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:57:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "AgentCapabilities")
iso, NotificationType, ModuleIdentity, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Integer32, Counter64, Bits, Gauge32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Integer32", "Counter64", "Bits", "Gauge32", "MibIdentifier", "Unsigned32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
ciscoTrustSecInterfaceCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 597))
ciscoTrustSecInterfaceCapability.setRevisions(('2012-09-04 00:00', '2010-10-30 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setLastUpdated('201209040000Z')
if mibBuilder.loadTexts: ciscoTrustSecInterfaceCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecInterfaceCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV12R0250SYPCat6k = ciscoTrustSecInterfaceCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecInterfaceCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 597, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                     series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecInterfaceCapV15R0101SYPCat6k = ciscoTrustSecInterfaceCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-INTERFACE-CAPABILITY", ciscoTrustSecInterfaceCapV15R0101SYPCat6k=ciscoTrustSecInterfaceCapV15R0101SYPCat6k, ciscoTrustSecInterfaceCapability=ciscoTrustSecInterfaceCapability, PYSNMP_MODULE_ID=ciscoTrustSecInterfaceCapability, ciscoTrustSecInterfaceCapV12R0250SYPCat6k=ciscoTrustSecInterfaceCapV12R0250SYPCat6k)
