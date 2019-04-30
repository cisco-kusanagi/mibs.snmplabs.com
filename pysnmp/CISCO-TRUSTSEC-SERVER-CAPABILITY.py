#
# PySNMP MIB module CISCO-TRUSTSEC-SERVER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TRUSTSEC-SERVER-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:58:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Integer32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, Gauge32, ModuleIdentity, ObjectIdentity, NotificationType, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "Gauge32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibIdentifier", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
ciscoTrustSecServerCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 596))
ciscoTrustSecServerCapability.setRevisions(('2012-09-07 00:00', '2010-10-30 00:00',))
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setLastUpdated('201209070000Z')
if mibBuilder.loadTexts: ciscoTrustSecServerCapability.setOrganization('Cisco Systems, Inc.')
ciscoTrustSecServerCapV12R0250SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setProductRelease('Cisco IOS 12.2(50)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV12R0250SYPCat6k = ciscoTrustSecServerCapV12R0250SYPCat6k.setStatus('current')
ciscoTrustSecServerCapV15R0101SYPCat6k = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 596, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setProductRelease('Cisco IOS 15.1(1)SY on Catalyst 6000/6500\n                    series devices.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoTrustSecServerCapV15R0101SYPCat6k = ciscoTrustSecServerCapV15R0101SYPCat6k.setStatus('current')
mibBuilder.exportSymbols("CISCO-TRUSTSEC-SERVER-CAPABILITY", ciscoTrustSecServerCapV12R0250SYPCat6k=ciscoTrustSecServerCapV12R0250SYPCat6k, ciscoTrustSecServerCapability=ciscoTrustSecServerCapability, PYSNMP_MODULE_ID=ciscoTrustSecServerCapability, ciscoTrustSecServerCapV15R0101SYPCat6k=ciscoTrustSecServerCapV15R0101SYPCat6k)
